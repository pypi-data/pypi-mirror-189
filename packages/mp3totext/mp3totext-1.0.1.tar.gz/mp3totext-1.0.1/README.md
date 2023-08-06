# Python3 projects
## mp3totext
### About
- A simple text from speech extractor (mp3 -> wav -> txt) for Polish language
### Usage
- You can either install the package with `pip3 install -e .` and execute `python3 -m mp3totext`
- Or run it directly (the dependencies needs to be fullfilled) like any other script `./mp3totext.py`
- For help you can pass `-h` attribute
- If you want to print out what's saved in .txt files you can pass `--debug` attribute
- You **must** place mp3's inside the **mp3** folder - if there are no mp3's program will raise error
- Any left out wav files inside **wav** folder will symbolize that there was an error with speech recognition
