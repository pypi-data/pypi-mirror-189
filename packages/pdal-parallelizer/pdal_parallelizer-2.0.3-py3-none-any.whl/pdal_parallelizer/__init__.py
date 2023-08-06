import json
import logging
import os
import os.path
import click
import pdal
from dask import config as cfg
from dask.distributed import LocalCluster, Client, progress
from distributed.diagnostics import MemorySampler
from os import listdir
from . import do
from . import file_manager
from . import cloud
from . import tile
from matplotlib import pyplot as plt
import sys
import ntpath
from os.path import join
from math import ceil


def query_yes_no(question, default='no'):
    valid = {'yes': True, 'y': True, 'ye': True, 'no': False, 'n': False}
    if default is None:
        prompt = ' [y/n] '
    elif default == 'yes':
        prompt = ' [Y/n] '
    elif default == 'no':
        prompt = ' [y/N] '
    else:
        raise ValueError(f'Invalid default answer: {default}')

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write('Please respond with "yes" or "no" (or "y" or "n").\n')


def config_dask(n_workers, threads_per_worker, timeout):
    """Make some configuration to avoid workers errors due to heartbeat or timeout problems. Set the number of cores
    to process the pipelines """
    if not timeout:
        timeout = input('After how long of inactivity do you want to kill your worker (timeout)\n')

    cfg.set({'interface': 'lo'})
    cfg.set({'distributed.scheduler.worker-ttl': None})
    cfg.set({'distributed.comm.timeouts.connect': timeout})
    cluster = LocalCluster(n_workers=n_workers, threads_per_worker=threads_per_worker, silence_logs=logging.ERROR)
    client = Client(cluster)
    return client


def process_pipelines(
        config,
        input_type,
        timeout=None,
        n_workers=3,
        threads_per_worker=1,
        dry_run=None,
        diagnostic=False,
        tile_size=(256, 256),
        buffer=None,
        remove_buffer=None,
        bounding_box=None,
        merge_tiles=False,
        remove_tiles=False
):
    # Assertions
    assert type(config) is str
    assert input_type == "single" or input_type == "dir"
    if timeout:
        assert type(timeout) is int
    assert type(n_workers) is int
    assert type(threads_per_worker) is int
    if dry_run:
        assert type(dry_run) is int
    assert type(diagnostic) is bool
    assert type(tile_size) is tuple and len(tile_size) == 2
    if buffer:
        assert type(buffer) is int
    if remove_buffer:
        assert type(remove_buffer) is bool
    if bounding_box:
        assert type(bounding_box) is tuple
        assert len(bounding_box) == 4
    assert type(merge_tiles) is bool
    assert type(remove_tiles) is bool

    with open(config, 'r') as c:
        config_file = json.load(c)
        input_dir = config_file.get('input')
        output = config_file.get('output')
        temp = config_file.get('temp')
        pipeline = config_file.get('pipeline')

    if n_workers >= os.cpu_count():
        answer = query_yes_no(
            f'\nWARNING - You choose to launch {n_workers} workers but your machine has only {os.cpu_count()}'
            f' CPUs, please reduce the number of workers.\nDo you want to continue ?'
        )
        if not answer:
            return

    if input_type == 'single':
        if tile_size == (256, 256):
            answer = query_yes_no(
                f'WARNING - You are using the default value of the tile_size option (256 by 256 meters). Please '
                f'check if your points cloud\'s dimensions are greater than this value.\nDo you want to continue ? '
            )
            if not answer:
                return

        infos = cloud.compute_quickinfo(input_dir)
        bounds = infos['summary']['bounds']
        distX, distY = (
            int(bounds['maxx'] - bounds['minx']),
            int(bounds['maxy'] - bounds['miny'])
        )

        nTilesX = ceil(distX / tile_size[0])
        nTilesY = ceil(distY / tile_size[0])

        if nTilesX * nTilesY > n_workers:
            answer = query_yes_no(
                f'WARNING - With this size of tiles and this number of workers, each worker will have more than one task'
                f' and it can blow up the distributed memory. Please choose a larger size for your tiles or increase '
                f'your number of workers.\nDo you want to continue ?'
            )
            if not answer:
                return

    if not os.path.exists(temp):
        os.mkdir(temp)

    if not os.path.exists(output):
        os.mkdir(output)

    # If there is some temp file in the temp directory, these are processed
    if len(listdir(temp)) != 0:
        click.echo(
            f'Something went wrong during previous execution, there is some temp files in your temp '
            f'directory.\nBeginning of the execution\n')
        # Get all the deserialized pipelines
        pipeline_iterator = file_manager.getSerializedPipelines(temp_directory=temp)
        # Process pipelines
        delayed = do.process_serialized_pipelines(temp_dir=temp, iterator=pipeline_iterator)
    else:
        click.echo('Beginning of the execution\n')
        # If the user don't specify the dry_run option
        if not dry_run:
            # If the user wants to process a single file, it is split. Else, get all the files of the input directory
            iterator = do.splitCloud(filepath=input_dir,
                                     output_dir=output,
                                     json_pipeline=pipeline,
                                     tile_bounds=tile_size,
                                     buffer=buffer,
                                     remove_buffer=remove_buffer,
                                     bounding_box=bounding_box) if input_type == 'single' \
                else file_manager.getFiles(input_directory=input_dir)
            # Process pipelines
            delayed = do.process_pipelines(output_dir=output, json_pipeline=pipeline, temp_dir=temp, iterator=iterator,
                                           is_single=(input_type == 'single'))
        else:
            # If the user wants to process a single file, it is split and get the number of tiles given by the user.
            # Else, get the number of files we want to do the test execution (not serialized)
            iterator = do.splitCloud(filepath=input_dir,
                                     output_dir=output,
                                     json_pipeline=pipeline,
                                     tile_bounds=tile_size,
                                     nTiles=dry_run,
                                     buffer=buffer,
                                     remove_buffer=remove_buffer,
                                     bounding_box=bounding_box) if input_type == 'single' \
                else file_manager.getFiles(input_directory=input_dir, nFiles=dry_run)
            # Process pipelines
            delayed = do.process_pipelines(output_dir=output, json_pipeline=pipeline, iterator=iterator,
                                           dry_run=dry_run, is_single=(input_type == 'single'))

    client = config_dask(n_workers=n_workers, threads_per_worker=threads_per_worker, timeout=timeout)

    click.echo('Parallelization started.\n')

    if diagnostic:
        ms = MemorySampler()
        with ms.sample(label='execution', client=client):
            delayed = client.compute(delayed)
            progress(delayed)
        ms.plot()
    else:
        delayed = client.compute(delayed)
        progress(delayed)

    del delayed

    file_manager.getEmptyWeight(output_directory=output)

    if merge_tiles and len(listdir(output)) > 1:
        input_filename = ntpath.basename(input_dir).split('.')[0]
        writers = tile.get_writers(tile.load_pipeline(pipeline))
        merge = cloud.merge(output, input_filename, writers)
        if merge is not None:
            merge_ppln = pdal.Pipeline(merge)
            merge_ppln.execute()

        if remove_tiles:
            for f in os.listdir(output):
                if f.split('.')[0] != input_filename:
                    os.remove(join(output, f))

    plt.savefig(output + '/memory-usage.png') if diagnostic else None
