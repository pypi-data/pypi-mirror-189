#!/usr/bin/env bash
if [[ -z $1 ]]; then
    echo "$0 <ver>"
    exit 1
fi
ver=$1
env=$PWD/${ver}
curl -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
trap '{ rm -f miniconda.sh; }' EXIT
bash miniconda.sh -b -p ${env}
${env}/bin/conda install -y "python=3.9"

${env}/bin/pip install -r requirements.txt --no-cache-dir git+https://gitlab.ssec.wisc.edu/pveglio/yori.git@${ver}
