# use_strip.py
from pathlib import Path
data_folder = Path("./L12/source/data/text.d/")
file_to_open = data_folder / "some_words.xyz"
with open(file_to_open, 'r') as f:
    for line in f:
        print(line.rstrip("-"))
