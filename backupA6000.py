import os
import time
# import pathlib
import exifread
import glob
import shutil
import os.path


# cameraPath = "C:\\Users\\metin\\Desktop\\import\\"
cameraPath = "E:\\"
outputPath = "C:\\Users\\metin\\Desktop\\output\\"
outputPath = "/Users/metinelitas/Foto-Video/A6000"
cameraPath = "/Volumes/NO NAME"



def copyFileToDirectory(directoryName,fileName):
    directoryToCopy = os.path.join(outputPath,directoryName)
    # print("dir to copy:" + directoryToCopy)
    if os.path.exists(directoryToCopy) != 1:
        print("Create dir: " + directoryToCopy)
        os.mkdir(directoryToCopy)

    print("Copying " +  fileName + " --->" + directoryToCopy)
    shutil.copy(fileName, directoryToCopy)
    

def copyMtsFiles():
    for r, d, f in os.walk(cameraPath):
        for file in f:
            if file.endswith(".MTS"):
                fileFullPath = os.path.join(r, file) 
                modifiedTime = time.gmtime(os.path.getmtime(fileFullPath))
                imageTakenDay = modifiedTime.tm_mday.__str__()
                imageTakenMonth = modifiedTime.tm_mon.__str__()
                imageTakenYear = modifiedTime.tm_year.__str__()
                if (len(imageTakenMonth) == 1):
                    imageTakenMonth = "0"+imageTakenMonth
                if (len(imageTakenDay) == 1):
                    imageTakenDay = "0"+imageTakenDay
                directoryName = imageTakenYear+"-"+imageTakenMonth+"-"+imageTakenDay
                copyFileToDirectory(directoryName,fileFullPath)

def copyImageFiles():
    for r, d, f in os.walk(cameraPath):
        for file in f:
            if file.endswith(".JPG"):
                fileFullPath = os.path.join(r, file) 
                # print(fileFullPath)
                f = open(fileFullPath, 'rb')
                exifTags = exifread.process_file(f,details=False)
                imageDateTimeValue = exifTags['Image DateTime']
                splittedDateTimeData = str(imageDateTimeValue).split(":")
                imageTakenDay = splittedDateTimeData[2].split(" ")[0]
                imageTakenMonth = splittedDateTimeData[1]
                imageTakenYear = splittedDateTimeData[0]
                directoryName = imageTakenYear+"-"+imageTakenMonth+"-"+imageTakenDay
                copyFileToDirectory(directoryName,fileFullPath)
                # RAW
                rawFileName = os.path.join(r, file.split('.')[0] + '.ARW')
                if (os.path.isfile(rawFileName)):
                    directoryName = directoryName + '/' + 'RAW'
                    copyFileToDirectory(directoryName,rawFileName)
            


copyImageFiles()
copyMtsFiles()

