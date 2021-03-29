import os

fname = "greatwall.jpg"
pht   = "photography"
clr   = "white"
direction = "SouthWest"

watermark = "logos/" + pht + "_" + clr + ".png"
inputimg  = "art/fotos/" + fname
outputimg = "watermarked/" + fname

scale = "60%"
shcommand = "composite -dissolve 100 -gravity " + direction + " " + watermark + " -resize " + scale + " " + inputimg + " " + outputimg
os.system(shcommand)
