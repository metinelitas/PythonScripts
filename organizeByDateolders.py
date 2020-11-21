from pathlib import Path
import exifread
import shutil
from datetime import datetime


fileExtensions = ['.MOV', '.mov', 'MP4', '.GIF', '.jpg', '.JPEG', '.JPG', '.HEIC', '.heic', '.PNG']

fld = Path(r'/Users/metinelitas/Foto-Video/Yedeklendi/iphon')

list = fld.iterdir()

for p in list:        
    if (p.suffix in fileExtensions):
        print ('filename:' + str(p))
        with open(p, mode='rb') as fid:
            exifTags = exifread.process_file(fid,details=False)
            try:
                imageDateTimeValue = exifTags['Image DateTime']
                splittedDateTimeData = str(imageDateTimeValue).split(":")
                imageTakenDay = splittedDateTimeData[2].split(" ")[0]
                imageTakenMonth = splittedDateTimeData[1]
                imageTakenYear = splittedDateTimeData[0]
            except:
                print("Cannot read from exif. Use file creation time instead.")
                mod = p.stat().st_mtime
                x = datetime.fromtimestamp(mod)
                imageTakenDay = str(x.day).zfill(2)
                imageTakenMonth = str(x.month).zfill(2)
                imageTakenYear = str(x.year)

            directoryName = p.parent / (imageTakenYear+"-"+imageTakenMonth+"-"+imageTakenDay)
            print(directoryName)
            Path(directoryName).mkdir(parents=True, exist_ok=True)
            p.rename(directoryName / p.name)





