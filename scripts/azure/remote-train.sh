#!/bin/bash

rm -rf $HOME/src/lets-do-the-numbers
pushd $HOME/src
git clone git@github.com:delqn/lets-do-the-numbers.git
cd ./lets-do-the-numbers
git pull --rebase origin master
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH
make train
git commit -m 'Newly trained model' model.*
git push origin master
