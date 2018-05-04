#!/usr/bin/env bash
cp -r ../../web .
docker build . -t "my_pdb_web:1.0.0"
rm -fr web
