"""
Tile class.

A tile is composed of :
- Its path (filepath)
- A directory to store the results files (output_dir)
- A pdal pipeline (json_pipeline)
- A name (optional) (name)
- Its limits (optional) (bounds)
"""

import sys
import pdal
import json
import os
from . import cloud
from . import bounds


def load_pipeline(pipeline):
    with open(pipeline, 'r') as ppln:
        p = json.load(ppln)
    return p


def get_readers(pipeline):
    return list(filter(lambda x: x['type'].startswith('readers'), pipeline))


def get_writers(pipeline):
    return list(filter(lambda x: x['type'].startswith('writers'), pipeline))


class Tile:
    def __init__(self, filepath, output_dir, json_pipeline, name=None, bounds=None, buffer=None, remove_buffer=False, cloud_object=None):
        self.filepath = filepath
        self.output_dir = output_dir
        self.json_pipeline = json_pipeline

        if name:
            self.name = name
        else:
            self.name = os.path.basename(self.filepath).split('.')[0]

        self.buffer = buffer
        self.remove_buffer = remove_buffer

        if self.buffer:
            self.bounds_without_buffer, self.bounds, self.assign = bounds.buffer(self.buffer)
        else:
            self.bounds = bounds

        self.cloud = cloud_object

    def getName(self):
        return self.name

    def pipeline(self, single_file):
        """Assign a pipeline to the tile"""
        output_dir = self.output_dir

        p = load_pipeline(self.json_pipeline)

        # Create the name of the temp file associated to the pipeline
        temp_name = 'temp__' + self.getName()
        output_filename = f'{output_dir}/{self.getName()}'
        # Get the reader and the writer
        reader = get_readers(p)
        writer = get_writers(p)
        try:
            compression = writer[0]['compression']
            extension = '.laz' if compression == 'laszip' or compression == 'lazperf' else '.las'
        except KeyError:
            # Get the extension for the output
            extension = '.' + writer[0]['type'].split('.')[1] + '.las' if writer[0]['type'].split('.')[1] == 'copc' else '.' + writer[0]['type'].split('.')[1]

        # If there is a buffer
        if self.buffer:
            # If the writer is 'writers.copc' or 'writer.laz' or 'writers.copc'
            if writer[0]['type'].split('.')[1] in ['las', 'laz', 'copc']:
                # Insert the filter to assign the wittheld flag to the buffer
                p.insert(1, self.assign)
        if self.remove_buffer:
            # Remove the buffer
            p.insert(len(p) - 1, bounds.removeBuffer(self.bounds_without_buffer))

        if self.cloud:
            # If there is the ferry filter attribute in the tile instance
            if not self.cloud.classFlags:
                # Insert the filter to add the ClassFlags dimension
                p.insert(1, cloud.addClassFlags())

        # The pipeline must contain a reader AND a writer
        if not reader:
            sys.exit("Please add a reader to your pipeline.")
        elif not writer:
            sys.exit("Please add a writer to your pipeline.")

        # If the input is a single file
        if single_file:
            # Add a crop filter to divide the cloud in small tiles
            p.insert(1, cloud.crop(self.bounds))

        # Add the filename option in the pipeline's reader to get the right file
        reader[0]['filename'] = self.filepath
        # Add the filename option in the pipeline's writer to write the result in the right file
        writer[0]['filename'] = output_filename + extension

        p = pdal.Pipeline(json.dumps(p))

        return p, temp_name

    def split(self, distTileX, distTileY, nTiles=None):
        """Split the tile in small parts of given sizes"""
        current_minx = self.bounds.minx
        current_maxx = current_minx + distTileX if current_minx + distTileX <= self.bounds.maxx else self.bounds.maxx
        current_miny = self.bounds.miny
        current_maxy = current_miny + distTileY if current_miny + distTileY <= self.bounds.maxy else self.bounds.maxy
        # If it's a dry run, 'cpt' will count the number of tiles created
        cpt = 0

        while current_maxx <= self.bounds.maxx and current_maxy <= self.bounds.maxy and (cpt < nTiles if nTiles else True):
            # Create the bounds for the small tile
            b = bounds.Bounds(current_minx, current_miny, current_maxx, current_maxy)
            # Create its name (minx_miny)
            name = str(int(b.minx)) + '_' + str(int(b.miny))
            # Create the tile
            t = Tile(filepath=self.filepath, output_dir=self.output_dir, json_pipeline=self.json_pipeline, name=name, bounds=b, buffer=self.buffer, remove_buffer=self.remove_buffer, cloud_object=self.cloud)
            # Add the width given by the user to shift right to create a new tile
            current_minx += distTileX
            current_maxx += distTileX

            # If the current maxx value exceeds the right edge of the cloud
            if current_maxx >= self.cloud.bounds.maxx:
                # And if there is a piece of cloud non-processed
                if t.bounds.maxx < self.cloud.bounds.maxx:
                    # Calculate the offset distance
                    dist = self.cloud.bounds.maxx - t.bounds.maxx
                    # Shift
                    current_maxx = t.bounds.maxx + dist
                else:
                    # Return to the left edge to create new tiles
                    current_minx = self.bounds.minx
                    current_maxx = current_minx + distTileX
                    # Move down from the height value given by the user
                    current_miny += distTileY
                    current_maxy += distTileY

            # If the current maxy value exceeds the top edge of the cloud
            if current_maxy > self.cloud.bounds.maxy:
                # And if there is a piece of cloud non-processed
                if t.bounds.maxy < self.cloud.bounds.maxy:
                    # Calculate the offset distance
                    dist = self.cloud.bounds.maxy - t.bounds.maxy
                    # Shift
                    current_maxy = t.bounds.maxy + dist

            cpt += 1
            yield t

    def __str__(self):
        if self.bounds:
            return f'{self.bounds} - {self.filepath}'
        else:
            return f'{self.filepath}'
