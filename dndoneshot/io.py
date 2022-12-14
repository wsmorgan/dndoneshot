"""Handles file reading and writing for the one shot helper."""

import json
import os
from os import path
from dndoneshot import msg

def read_in_config(path_to_config):
    """Reads in the input config file.

    Args:
        path_to_config (str): The full path to the config file.

    Returns:
        A dictionary with the necessary fields for the code to run.
    """

    if not path.isfile(path_to_config):
        msg.err("File {} not found.".format(path_to_config))
        raise IOError("{} file not found.".format(path_to_config))

    with open(path_to_config, "r") as f:
        data = json.load(f)

    
    return data
