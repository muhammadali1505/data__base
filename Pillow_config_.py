"""
pip install pillow
"""

from PIL import Image
# im = Image.open("")
im = Image.open("")
# print(im)
# im.show()
out = im.resize((128,128)) # rasm olchami
angle = 45
out = im.rotate(angle)
