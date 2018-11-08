#!/usr/bin/env bash

# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

rm -rf build/

rm -rf dist/

rm -rf *.egg-info/

rm -rf blocksWorld/*.pyc

rm -rf blocksWorld/__pycache__

rm -rf ./.pytest_cache/

rm -rf ./.eggs/

rm -rf blocksWorld.egg-info

rm -rf data

rm -rf data_result

rm -rf data_expected

find . -iname .DS_Store -delete
