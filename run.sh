#!/bin/bash

commonvoice_path=/Database/Mozilla_CommonVoice/cv-corpus-11.0-2022-09-21/en/
musan_path=/Database/musan
rir_path=./RIRS_NOISES/simulated_rirs

save_path=exp/exp_commonvoice1

python3 trainECAPAModel.py \
    --train_list data/commonvoice_wavs/train_list.txt \
    --train_path ./ \
    --eval_list data/commonvoice_wavs/veri_test.txt \
    --eval_path ./ \
    --musan_path $musan_path \
    --rir_path $rir_path \
    --save_path $save_path
