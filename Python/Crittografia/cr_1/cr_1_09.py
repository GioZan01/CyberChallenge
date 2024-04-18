import numpy as np
from PIL import Image

im1 = Image.open("file_challenges/flag_enc.png")
im2 = Image.open("file_challenges/notflag_enc.png")

enc1 = np.bitwise_xor(im1, im2).astype(np.uint8)
Image.fromarray(enc1).save('flag.png')
