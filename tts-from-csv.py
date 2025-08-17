import os
import argparse
import pandas as pd
import torch
from styletts2_inference.models import StyleTTS2
from utils import synthesize
import soundfile as sf

DIR_CURRENT = os.getcwd()

args = argparse.ArgumentParser()
args.add_argument('--csv', type=str, dest='file', required=True, help='Path to csv file to process with columns: tts; or tts,speed')
args.add_argument('--voice', type=str, dest='voice', default='Анастасія Павленко.pt', help='File name of voice from voices directory')
args = args.parse_args()

if not os.path.isfile(args.file):
    raise FileNotFoundError(args.file)

voice = DIR_CURRENT + '/voices/' + args.voice
if not os.path.isfile(voice):
    raise FileNotFoundError('No such voice: ' + voice)

DIR_OUTPUTS = DIR_CURRENT + '/outputs/'
if not os.path.isdir(DIR_OUTPUTS):
    os.mkdir(DIR_OUTPUTS)

df = pd.read_csv(args.file)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = StyleTTS2(hf_path='patriotyk/styletts2_ukrainian_multispeaker', device=device)

is_speed_in_csv = False
speed = 1
if 'speed' in df.columns:
    is_speed_in_csv = True

for index, row in df.iterrows():
    if is_speed_in_csv:
        speed = row['speed']
    sr, wav = synthesize(model, voice, row['tts'], speed)
    sf.write(DIR_OUTPUTS + f"{index}.wav", wav, sr)