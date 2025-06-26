import sys 

from PIL import Image 

images=[Image.open(arg) for arg in sys.argv[1:]]

images[0].save(
    "makima.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
)