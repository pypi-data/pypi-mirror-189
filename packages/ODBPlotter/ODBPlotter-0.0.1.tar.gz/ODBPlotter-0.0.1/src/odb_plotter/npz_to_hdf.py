#!/usr/bin/env python3

# Author: CJ Nguyen
# Takes  .npz files generated by `odb_to_npz.py` and converts it to a compressed hdf5 file that follows the same hierarchical format.
#
# Usage: <script name> <optional: npz_directory>
# Where <npz_directory> is optional. If specified it should point to the directory that contains the outputted .npz files. Otherwise, will find the `tmp_npz` folder in the current working directory.

import os
import numpy as np
import h5py
from nptyping import NDArray


def npz_to_hdf(output_file: str, npz_dir: str = "tmp_npz") -> None:

    # To my knowledge, h5py does not ship type hints
    with h5py.File(output_file, "w") as hdf5_file:
        root: str
        files: list[str]
        for root, _, files in os.walk(npz_dir, topdown=True):
            filename: str
            for filename in files:
                item: str = os.path.join(root, filename)
                read_npz_to_hdf(item, npz_dir, hdf5_file)


def read_npz_to_hdf(item: str, npz_dir: str, hdf5_file) -> None:
    npz: NDArray = np.load(item)
    arr: NDArray = npz[npz.files[0]]
    item_name: str = os.path.splitext(item)[0].replace(npz_dir, "")
    hdf5_file.create_dataset(item_name, data=arr, compression="gzip")
