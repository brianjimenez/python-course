#!/bin/bash

rm -rf *.so *.c
python setup.py build_ext --inplace
