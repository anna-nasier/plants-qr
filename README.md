## Installation 

### Create python venv
Create a virtual environment with required libraries: 

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Install Arial font

The text below qr code is written in Arial font. To install it on Debian/Ubuntu, run this in terminal: 
```
sudo apt install ttf-mscorefonts-installer
sudo fc-cache -f
```

## Usage 

Input a url and a name for generated qr image when calling the script and enjoy your qr code. 

`python qr_generator.py url name`

You can add a text below the QR code by using `-t ` flag. 