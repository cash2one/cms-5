#!/bin/sh

cd ../../cbbweb

find ./ -name '*.pyc' | xargs -i rm -rf {}

