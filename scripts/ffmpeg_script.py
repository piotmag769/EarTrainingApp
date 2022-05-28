import os
import ffmpeg
import sys

sys.path.append("..")

# stream = ffmpeg.input('input.mp4')
# (
#     ffmpeg
#     .input('D:\\Piotrek\\Studia\\AGH\\Semestr 4\\Python\\EarTrainingApp\\sounds\\easy\\guitar\\dom_7\\down\\1_kw_sek\\D-ks-1-d.wav')
#     .filter('a', 'atempo:0.5')
#     .output('output.mp4')
#     .run()
# )

instruments = ['guitar']  # 'piano', 'trumpet'
modes = ['medium', 'hard']
tempo_mod = [0.5, 0.25]

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
for mode in modes:
    os.mkdir("../sounds/" + mode)
    for instrument in instruments:
        os.mkdir("../sounds/" + mode + '/' + instrument)
        for playlist, options, ex_type in zip(all_playlists, all_options, ex_types):
            os.mkdir("../sounds/" + mode + '/' + instrument + '/' + ex_type)
            for option in options:
                os.mkdir("../sounds/" + mode + '/' + instrument + '/' + ex_type + '/' + option)
                for ex in playlist:
                    os.mkdir("../sounds/" + mode + '/' + instrument + '/' + ex_type + '/' + option + '/' + ex)
                    i += 1

print(i)

# for mode in modes:
#     for instrument in instruments:
#         for folder in os.listdir("../sounds/easy/" + instrument):
#             print(folder)
