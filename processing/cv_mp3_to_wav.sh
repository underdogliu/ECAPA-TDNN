#!/bin/bash

set -e
. ./path.sh

srcdir=data/commonvoice_new
tardir=data/commonvoice_new_wavs

cmd=run.pl
nj=40

. ./utils/parse_options.sh

mkdir -p ${srcdir}/split$nj/log ${tardir}/wavs

scp_args=""
for i in $(seq $nj); do
    scp_args="$scp_args $srcdir/split$nj/train_list.$i.txt "
done

utils/split_scp.pl $srcdir/train_list.txt $scp_args

$cmd JOB=1:$nj $srcdir/split$nj/log/mp3_to_wav.JOB.log \
    python3 processing/cv_mp3_to_wav.py $srcdir/split$nj/train_list.JOB.txt $tardir/wavs ${tardir}/train_list.JOB.txt

for i in $(seq $nj); do
    cat ${tardir}/train_list.$i.txt
done > ${tardir}/train_list.txt
