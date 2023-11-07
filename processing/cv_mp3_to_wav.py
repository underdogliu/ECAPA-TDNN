"""
Convert commonvoice mp3 file to wav files
sample command:
    ffmpeg -hide_banner -loglevel error -i foo.mp3 -vn -acodec pcm_s16le -ac 1 -ar 16000 -f wav foo.wav
"""

import os
import sys
import soundfile as sf

if __name__ == "__main__":
    src_train_list = sys.argv[1]
    tar_wavdir = sys.argv[2]
    tar_train_list = sys.argv[3]

    with open(src_train_list, "r") as s, open(tar_train_list, "w") as w:
        for line in s:
            utt_name, session_id, mp3_path = line.split()
            wav_path = tar_wavdir + "/{}.wav".format(utt_name)
            command = "ffmpeg -hide_banner -loglevel error -i {} -vn -acodec pcm_s16le -ac 1 -ar 16000 -f wav {}".format(
                mp3_path, wav_path
            )
            os.system(command)

            # after writing the wav path, try using soundfile to read it
            # if the reading is not successful, it will not be put into
            # the file list
            try:
                audio, sr = sf.read(wav_path)
                w.write("{} {} {}\n".format(utt_name, session_id, wav_path))
            except:
                continue
