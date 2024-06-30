
import cv2 
import sys 
import numpy as np 
import qrcode
from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def add_white_space_to_bottom(image):
    width, height = image.size
    add_h = int(height * 0.15)
    new_height = height + add_h
    new_image = Image.new('RGB', (width, new_height), 'white')
    new_image.paste(image, (0, 0))
    return new_image, add_h

def add_text(image, text: str, add_height):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    fontsize = 1
    img_fraction = 0.8

    font = ImageFont.truetype("arial.ttf", fontsize)
    while font.getsize(text)[0] < img_fraction*image.size[0]:
        fontsize += 1
        font = ImageFont.truetype("Arial.ttf", size = fontsize)
    tw, th = font.getsize(text)
    x = (width - tw)/2
    y = height - add_height - th/2
    draw.text((x,y), text, fill = "black", font = font)
    return image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type = str, help = "Input the url to generate qr code from")
    parser.add_argument('output', type = str, help = 'Name of output qr image')
    parser.add_argument('-t', '--text', type = str, help = 'Add text below the qr code')
    parser.add_argument('-p', '--path', type = str, help = 'Path to save qr code img')
    args = parser.parse_args()
    url = args.url
    output = args.output
    path = args.path
    text = args.text
    qr = qrcode.make(url)
    if text is not None:
        qr, add_h = add_white_space_to_bottom(qr)
        qr = add_text(qr, text, add_h)
    # qr.show()
    if path is not None: 
        path = os.path.join(path, output +'.png')
        qr.save(path)
    else: 
        qr.save(output + '.png')
if __name__ == "__main__":
    main()
