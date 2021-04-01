import os

fname = "zaragoza.jpg"

pht   = "photography"
#pht   = "lego"

clr   = "white"
#clr   = "black"

direction = "SouthEast"

watermark = "../logos/" + pht + "_" + clr + ".png"
inputimg  = "fotos/" + fname
outputimg = "watermarked/" + fname

scale = "60%"

shcommand = "composite -dissolve 100 -gravity " + direction + " " + watermark + " -resize " + scale + " " + inputimg + " " + outputimg
os.system(shcommand)
