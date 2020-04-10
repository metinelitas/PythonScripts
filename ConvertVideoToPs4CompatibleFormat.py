import subprocess
import sys

fileName = "Charlotte de Witte _ Tomorrowland Belgium 2019 - W2-RF60iDaoEPw.mkv"
fileNameWithoutExtension = fileName.split(".")[0]
fileNameExtension = fileName.split(".")[1]

print(fileNameWithoutExtension)
outputName = fileNameWithoutExtension + "_aac" + "." + fileNameExtension
subprocess.run(["ffmpeg", "-i", fileName, "-codec:v", "copy", "-codec:a", "aac" , outputName])