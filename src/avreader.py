#!/usr/bin/python
# Purpose: This module has functions that go to a URL and download movie times
# Licence:     GPL
#-------------------------------------------------------------------------------
import re
import os
import argparse
import nltk
# nltk.download('punkt')
import pandas as pd
import random
from PIL import Image, ImageDraw

import image_manipulation as imm




def read_f(f):
    return pd.read_csv(f)


def pick_random_sentence(df):
    return df.sample()['sentence']


def get_image(filename):
    im = Image.open(os.path.join("data", "images", "word_images", filename))
    return im 

def image_available(token, images_df):

    print(token)
    for idx, imagetk in enumerate(images_df['tokens']):
        if token.lower() == imagetk.lower():
            print('found', token, imagetk)
            fn = images_df['filename'][idx]
            print(fn)
            return get_image(fn)

    return 0 #nothing found


def create_image_list(sentence, images, tokens, bigrm):

    im_list = []
    for t in tokens:

        if image_available(t, images):
            im_list.append(image_available(t, images))
        else:
            #if word is not present, draw it
            im_list.append(imm.draw_word(t))

    # im_list.append(images.sample()['filename'])
    # im_list.append(images.sample()['filename'])

    return im_list


def render(sentence, images):
    s = sentence.tolist()
    print(s[0])
    tokens = nltk.word_tokenize(s[0])
    print(tokens)
    bigrm = nltk.bigrams(tokens)
    print(*map(' '.join, bigrm), sep=', ')

    im_list = create_image_list(sentence, images, tokens, bigrm)
    imm.concat_images(im_list)

    return None


if __name__ == '__main__':


    # Instantiate the parser
    parser = argparse.ArgumentParser(description='MP3 Downloader description')
    # Optional positional argument
    parser.add_argument('opt_pos_arg', type=int, nargs='?',
                        help='An optional integer positional argument')
    # Switch
    parser.add_argument('--dl_flag', action='store_true',
                        help='Flag indicating whether to download')

    args = parser.parse_args()


    output_directory = "output"

    sents = read_f("data/text/sentences_v0.1.csv")
    images =   read_f("data/word_image_map.csv")


    #Randomize
    sent = pick_random_sentence(sents)

    #Render a set of images
    render(sent, images)
    

    print(images.shape)
    print("Done")




## TTD:
# Len(tokens) - comic panel spots...
# Add the word to the bottom if found...
# Negate images
# 2. Look for trigrams
# 4. Randomize the sentence
# POS tagging
# Word stemming
# 5. Gender detector.
