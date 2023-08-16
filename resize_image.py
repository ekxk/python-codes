#%%
import os
from PIL import Image

path_load = 'inputs/1/'
path_save = 'outputs/1/'

file_names = os.listdir(path_load)
for i,file in enumerate(file_names):
    f_img = path_load+"/"+file
    img = Image.open(f_img)
    size = 1200,630
    img.thumbnail(size, Image.Resampling.LANCZOS) # to keep aspect ratio
    output_file_name = os.path.join(path_save, "small_" + file)
    img.save(output_file_name, "JPEG", quality = 95,dpi=(72, 72))

#%%
