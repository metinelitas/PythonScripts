import pathlib
import exifread
import hashlib
import random
from datetime import datetime


# =============== VARIABLE DEFS ===============
duplicates = []
dupFileNames = []
hash_keys = dict()

folderPath = pathlib.Path(r'D:\iphonePhotos')
copyto = pathlib.Path(r'D:\Duplicates')
organizedPath = pathlib.Path(r'D:\AdamGibi')
pngPath = pathlib.Path(r'D:\AdamGibi\GIF')

# p1 = folderPath.glob('**/*.HEIC')

p = folderPath.glob('**/*.GIF')

p = folderPath.glob('**/*.mp4')
p = folderPath.glob('**/*')

# p = sorted(p1) + sorted(p2)
# x = sorted(p)


# =============== FUNCTION DEFS ===============

def getNewFilePathForDuplicateFiles(fileName):
    return fileName.split('.')[0] + '_' + str(random.randint(0, 1000)) + '.' + fileName.split('.')[1]

def listFileNamesOnly(p):
    for index,filepath in enumerate (p):
        if (filepath.is_file()):
            print('Name:   ' + str(filepath))

def putToFolderAccordingToFileExtension(p,dirToCopy):
    for index,filepath in enumerate (p):
        if (dirToCopy / filepath.name).is_file():
            print('zaten var')
            y = getNewFilePathForDuplicateFiles(filepath.name)
            filepath.rename(dirToCopy / y)
            print('new name random' + y)
        else:
            filepath.rename(dirToCopy / filepath.name)

def findAndRelocateDuplicateFiles(p,dirToCopy):
    for index,filepath in enumerate (p):
        print('checking' + '\t idx: ' + str(index) + 'name: ' + str(filepath))
        with open(filepath,'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
            f.close()
            if filehash not in hash_keys:
                hash_keys[filehash] = index
            else:
                duplicates.append((index,hash_keys[filehash]))
                print("dup found:" + str(filepath) + 'is same with idx:' + str(hash_keys[filehash]))
                if (dirToCopy / filepath.name).is_file():
                    print('zaten var')
                    y = filepath.name.split('.')[0] + '_' + str(random.randint(0, 1000)) + '.' + filepath.name.split('.')[1]
                    filepath.rename(dirToCopy / y)
                    print('new name random' + y)
                else:
                    filepath.rename(dirToCopy / filepath.name)

def putToFolderAccordingToDate(p,dirToCopy):
    for index,filepath in enumerate (p):
        with open(filepath,'rb') as fid:
            print('checking ' + str(filepath))
            exifTags = exifread.process_file(fid,details=False)
            try:
                imageDateTimeValue = exifTags['Image DateTime']
                splittedDateTimeData = str(imageDateTimeValue).split(":")
                imageTakenDay = splittedDateTimeData[2].split(" ")[0]
                imageTakenMonth = splittedDateTimeData[1]
                imageTakenYear = splittedDateTimeData[0]
            except:
                print("Cannot read from exif. Use file creation time instead.")
                mod = filepath.stat().st_mtime
                x = datetime.fromtimestamp(mod)
                imageTakenDay = str(x.day).zfill(2)
                imageTakenMonth = str(x.month).zfill(2)
                imageTakenYear = str(x.year)

            fid.close()

            newDirectoryName = dirToCopy / (imageTakenYear+"-"+imageTakenMonth+"-"+imageTakenDay)
            newDirectoryName.mkdir(parents=True, exist_ok=True)

            if (newDirectoryName / filepath.name).is_file():
                print('zaten var')
                y = getNewFilePathForDuplicateFiles(filepath.name)
                filepath.rename(newDirectoryName / y)
                print('new name random' + y)
            else:
                filepath.rename(newDirectoryName / filepath.name)


# =============== MAIN ===============

listFileNamesOnly(p)