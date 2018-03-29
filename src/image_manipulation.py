#!/usr/bin/python
# Purpose: This module has functions that go to a URL and download movie times
# Licence:     GPL
#-------------------------------------------------------------------------------
import os
from PIL import Image, ImageDraw, ImageFont

BASEWD, BASEHT = 200, 200


#resources: http://webpagepublicity.com/free-fonts-g.html#Free%20Fonts


def draw_word(token):
	'''	If a word is not available, just echo it as an image '''

	img = Image.new('RGBA', (BASEWD, BASEHT), 'white') #blank canvas

	draw = ImageDraw.Draw(img)
	fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')

	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype(os.path.join(fonts_path, 'Garrison ExtraBold Sans BOLD.ttf'), 24)

	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((BASEWD/2, BASEHT/2),token,(0,0,0),font=font)

	return img


def concat_images(im_list):

    """ place all the images in the list - next to one another """


    #loop through and calculate total imagew and imageht

    out_width, out_ht = 100, 100 #starting

    for im in im_list:
        #im = Image.open(fn)
        iw, ih = im.size[0], im.size[1]
        out_ht = max(out_ht, ih) # if wider, increase overall ht
        out_width += iw 

    out = Image.new('RGBA', (out_width, out_ht), 'white') #blank canvas
    
    currw = 0
    for im in im_list:
        #im = Image.open(fn)
        iw, ih = im.size[0], im.size[1]
        out.paste(im, (currw, 0, currw+iw, ih ))
        currw += iw


    #save image
    # TODO: need to resize if image is too small or too large...
    newname = "visualized_sentence.jpg"
    out.save(os.path.join("output" , newname))

    return(out)



# TODO
# Negate words. (Don't drink, doesn't understand)
# create images for T-shirt + Name = person. (Jim, Mary, John, Ram etc.)