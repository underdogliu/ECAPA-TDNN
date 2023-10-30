"""
Prepare commonvoice dataset, training list and the wav files
train_list:
$spkid $wav_path

Note: here spkid == wav_path because we do not have speaker
IDs for commonvoice.

wav files: in a folder of wavs
"""

import os
import sys


if __name__ == "__main__":
    cv_database = sys.argv[1]
    out_dir = sys.argv[2]
    train_tsv = cv_database + "/train.tsv"

    # create training list
    with open(train_tsv, "r") as t, open(out_dir + "/train_list.txt", "w") as o:
        for line in t:
            line_sp = line.split()
            mp3_path = line_sp[2]
            utt_name = mp3_path.split("/")[-1].split(".")[0]
            o.write("{} {}\n".format(utt_name, mp3_path))
