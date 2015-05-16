import gimpfu
gimp.image_list()

images=gimp.image_list()
img=images[0]
img.layers
layers=img.layers
len(img.layers)
for k in range(10):
    layers[k].translate(-50+k*10,0)

 

