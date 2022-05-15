from PIL import Image
import os

if not 'ltl' in os.listdir():
    os.mkdir('ltl')

# CROP, b/w filter
# for i in os.listdir('.'):
#     if i.endswith('.jpg'):
#         img = Image.open(i)
#         width, height = img.size
#         left = (width - 1080) / 2
#         top = (height - 1080) / 2
#         right = (height + 1080) / 2
#         bottom = (height + 1080) / 2
#         img = img.convert(mode='L').crop((left, top, right, bottom))
#         img.save('ltl\\' + i[:-4] + '.jpg')


# RESIZE, b/w filter

for i in os.listdir('.'):
    if i.endswith('.jpg'):
        img = Image.open(i)

        img = img.convert(mode='L').resize((1080, 1080))
        img.save('ltl\\' + i[:-4] + '.jpg')
