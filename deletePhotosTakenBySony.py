import pathlib
import exifread
import random


folderPath = pathlib.Path(r'D:\iphonePhotos')
copyto = pathlib.Path(r'D:\deneme')

p = folderPath.glob('**/*')
files = [x for x in p if x.is_file()]

for f in files:
    fx = open(f, 'rb')
    exifTags = exifread.process_file(fx,details=False,strict=False)
    if "Image Make" in exifTags:
        imageMake = exifTags['Image Make']
        if (str(imageMake) == 'SONY'):
            print(f)
            fx.close()
            if (copyto / f.name).is_file():
                print('zaten var')
                y = f.name.split('.')[0] + str(random.randint(0, 100)) + f.name.split('.')[1]
                print('new name random' + y)
                f.rename(copyto / y)
            else:
                f.rename(copyto / f.name)


