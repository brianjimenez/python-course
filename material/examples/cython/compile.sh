rm -rf *.so *.c
python setup.py build_ext --inplace
rm -rf build/
