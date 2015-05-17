#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def timewrap_slide(img, drawable) :
    layers=img.layers
    n=len(img.layers)
    for k in range(n):
        layers[k].translate(-50+k*10,0)

register(
    "python_fu_Timewrap_slide",
    "Timewrap Slide",
    "You have animation as image with frames as layers. You use this plugin to give every frame translation so you can make smooth camera slide on your timelapse movie.",
    "Licho-Karol Trzeszczkowski",
    "Licho",
    "2015",
    "<Image>/Filters/Test/Hello world",
    "*",
    [
        (PF_IMAGE, "img", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    timewrap_slide)
    
main()
