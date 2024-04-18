import numpy as np
from PIL import Image

im1 = Image.open("flag.png")
im2 = Image.open("notflag.png")
k = Image.open("key.png")

im1np = np.array(im1)*255
im2np = np.array(im2)*255
knp = np.array(k)*255

enc1 = np.bitwise_xor(im1np, knp).astype(np.uint8)
enc2 = np.bitwise_xor(im2np, knp).astype(np.uint8)
Image.fromarray(enc1).save('flag_enc.png')
Image.fromarray(enc2).save('notflag_enc.png')
