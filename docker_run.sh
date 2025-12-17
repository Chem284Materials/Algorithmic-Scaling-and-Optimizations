#!/bin/sh

docker run --rm -it -v $(pwd):/repo -p 8888:8888 chem284/lab2