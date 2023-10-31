"""
Convert commonvoice mp3 file to wav files
sample command:
    ffmpeg -hide_banner -loglevel error -i foo.mp3 -vn -acodec pcm_s16le -ac 1 -ar 16000 -f wav foo.wav
"""

import os
import sys


if __name__ == "__main__":
    src_train_list = sys.argv[1]
    tar_wavdir = sys.argv[2]
    tar_train_list = sys.argv[3]

    with open(src_train_list, "r") as s, open(tar_train_list, "w") as w:
        for line in s:
            utt_name, mp3_path = line.split()
            wav_path = tar_wavdir + "/{}.wav".format(utt_name)
            command = "ffmpeg -hide_banner -loglevel error -i {} -vn -acodec pcm_s16le -ac 1 -ar 16000 -f wav {}".format(
                mp3_path, wav_path
            )
            os.system(command)
            w.write("{} {}\n".format(utt_name, wav_path))
