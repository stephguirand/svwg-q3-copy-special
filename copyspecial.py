#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """
stephguirand
Help from demo, lessons and activities, youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about assignment
in study group.
"""

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    paths = []
    dir_list = os.listdir(dirname)  # list of paths in that dir
    for file_name in dir_list:
        if re.findall(r'__\w+__', file_name):
            paths.append(os.path.abspath(os.path.join(dirname, file_name)))
    return paths


def copy_to(path_list, dest_dir):
    """Given a list of files copies to a new directory."""
    abs_path = os.path.abspath(dest_dir)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    for path in path_list:
        shutil.copy(path, abs_path)


def zip_to(path_list, dest_zip):
    """Given a list of files adds them to a zipfile."""
    file_list = ""
    for path in path_list:
        file_list += path + " "
    try:
        subprocess.call(["zip", "-j", dest_zip] + path_list)
    except OSError as e:
        print(e)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument(
        'dest_dir', help='returns special files from given directory')
    # return parser
    ns = parser.parse_args(args)
    from_dir = ns.dest_dir
    todir = ns.todir
    tozip = ns.tozip

    if not ns:
        parser.print_usage()
        sys.exit(1)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    special_paths = get_special_paths(from_dir)
    if todir:
        copy_to(special_paths, todir)
    elif tozip:
        zip_to(special_paths, tozip)
    else:
        for path in special_paths:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
