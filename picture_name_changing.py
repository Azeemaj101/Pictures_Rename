import os
dic = []
f = 1
image_dir = r"F:\pic1"
all_files = os.listdir(image_dir)
dic = all_files

for i in all_files:
    path = os.path.join(image_dir,i)
    a = f"{f}.jpg"
    p = os.path.join(image_dir, a)
    f = f+1
    os.rename(path, p)
