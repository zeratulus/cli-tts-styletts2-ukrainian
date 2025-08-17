# CLI tool for TTS generation from CSV file with StyleTTS2 Ukrainian

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://vshymanskyy.github.io/StandWithUkraine/)

**Installation:**
>pip install -r requirements.txt

If you want to try this code with CUDA enabled, install torch with following command:
> pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

Or use this page for getting of latest or specified version of torch:  
> https://pytorch.org/get-started/locally/

**How to use**:
> python tts-from-csv.py --csv samples.csv

> python tts-from-csv.py --csv samples.csv --voice "Михайло Тишин.pt"

- See csv file example > samples.csv

This code use following model
> https://huggingface.co/spaces/patriotyk/styletts2-ukrainian/tree/main

Thanks to https://huggingface.co/patriotyk for great Ukrainian TTS model and a lot of voices, some code parts taken from here:

> https://huggingface.co/spaces/patriotyk/styletts2-ukrainian