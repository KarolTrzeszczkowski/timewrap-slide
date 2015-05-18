#!/usr/bin/env python


from gimpfu import *

def timewrap_slide(img, drawable, v) :
    layers=img.layers
    n=len(img.layers)
    for k in range(n):
        layers[k].translate(-50+k*v,0)

register(
    "python_fu_Timewrap_slide",
    "Timewrap Slide",
    "You have animation as image with frames as layers. You use this plugin to give every frame translation so you can make smooth camera slide on your timelapse movie.",
    "Licho-Karol Trzeszczkowski",
    "Licho",
    "2015",
    "<Image>/Filters/Test/Timewrap Slide",
    "*",
    [
        (PF_INT, "v", "Predkosc", 10)
    ],
    [],
    timewrap_slide)
    
main()
