# IMPORTANT!!! this is ffmpeg-python package, not ffmpeg, install it with
# pip install ffmpeg-python

import os
import sys

# original ffmpeg is required to use this package tho - install it with
# sudo apt-get update
# sudo apt install ffmpeg
import ffmpeg

sys.path.append("..")

instruments = ['guitar']  # 'piano', 'trumpet'
modes = ['medium', 'hard']
tempo_mods = [2.0, 3.5]

ex_types = ['dom_7', 'int', 'triads']

all_playlists = [
    ['zas', '1_kw_sek', '2_ter_kw', '3_sek'],
    ['2_m', '2_w', '3_m', '3_w', '4', '4_5_tryt', '5', '6_m', '6_w', '7_m', '7_w', '8'],
    ['dur_z', 'dur_6', 'dur_64', 'mol_z', 'mol_6', 'mol_64', 'zmn_z', 'zmn_6', 'zmn_64', 'zwiek']
]

all_options = [
    ['down', 'up'],
    ['down', 'up', 'harm'],
    ['down', 'up', 'harm', 'down_h', 'up_h']
]

i = 0
for mode, tempo_mod in zip(modes, tempo_mods):
    os.mkdir("../sounds/" + mode)
    for instrument in instruments:
        os.mkdir("../sounds/" + mode + '/' + instrument)
        for playlist, options, ex_type in zip(all_playlists, all_options, ex_types):
            os.mkdir("../sounds/" + mode + '/' + instrument + '/' + ex_type)
            for option in options:
                os.mkdir("../sounds/" + mode + '/' + instrument + '/' + ex_type + '/' + option)
                for ex in playlist:
                    curr_path = "../sounds/" + mode + '/' + instrument + '/' + ex_type + '/' + option + '/' + ex
                    easy_path = "../sounds/easy/" + instrument + '/' + ex_type + '/' + option + '/' + ex
                    os.mkdir(curr_path)
                    for file in os.listdir("../sounds/easy/" + instrument + '/' + ex_type + '/' + option + '/' + ex):
                        (
                            ffmpeg
                            .input(easy_path + '/' + file)
                            .filter('atempo', tempo_mod)
                            .output(curr_path + '/' + file)
                            .run()
                        )
                        i += 1

print(i)
