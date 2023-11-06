#!/bin/bash

set -e
. ./path.sh

srcdir=data/commonvoice_eval
tardir=data/commonvoice_wavs

cmd=run.pl
nj=40

. ./utils/parse_options.sh

mkdir -p ${srcdir}/split$nj/log ${tardir}/wavs

scp_args=""
for i in $(seq $nj); do
    scp_args="$scp_args $srcdir/split$nj/veri_test.$i.txt "
done

utils/split_scp.pl $srcdir/veri_test.txt $scp_args

$cmd JOB=1:$nj $srcdir/split$nj/log/mp3_to_wav.JOB.log \
    python3 processing/cv_mp3_to_wav.py $srcdir/split$nj/veri_test.JOB.txt $tardir/wavs ${tardir}/veri_test.JOB.txt

for i in $(seq $nj); do
    cat ${tardir}/veri_test.$i.txt
done > ${tardir}/veri_test.txt
