import torch
from verbalizer import Verbalizer
from ukrainian_word_stress import Stressifier, StressSymbol
import re
from unicodedata import normalize
from ipa_uk import ipa

device = 'cuda' if torch.cuda.is_available() else 'cpu'

stressify = Stressifier()
verbalizer = Verbalizer(device=device)

def split_to_parts(text):
    split_symbols = '.?!:'
    parts = ['']
    index = 0
    for s in text:
        parts[index] += s
        if s in split_symbols and len(parts[index]) > 150:
            index += 1
            parts.append('')
    return parts

def verbalize(text):
    parts = split_to_parts(text)
    verbalized = ''
    for part in parts:
        if part.strip():
            verbalized += verbalizer.generate_text(part) + ' '
    return verbalized


def synthesize(model, voice, text, speed = 1):
    print("*** saying ***")
    print(text)
    print("*** end ***")

    result_wav = []
    for t in split_to_parts(text):

        t = t.strip()
        t = t.replace('"', '')
        if t:
            t = t.replace('+', StressSymbol.CombiningAcuteAccent)
            t = normalize('NFKC', t)

            t = re.sub(r'[᠆‐‑‒–—―⁻₋−⸺⸻]', '-', t)
            t = re.sub(r' - ', ': ', t)
            ps = ipa(stressify(t))

            if ps:
                tokens = model.tokenizer.encode(ps)
                style = torch.load(voice)

                wav = model(tokens, speed=speed, s_prev=style)
                result_wav.append(wav)

    return 24000, torch.concatenate(result_wav).cpu().numpy()