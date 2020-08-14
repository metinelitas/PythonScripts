import hashlib
import os

duplicates = []
hash_keys = dict()

print("hello")
dir1 = "/Users/metinelitas/Downloads"
dir2 = "/Users/metinelitas/Foto-Video/A/"


os.chdir(dir1)
os.getcwd()

file_list = os.listdir()

for index,filename in enumerate (os.listdir(dir1)):
	with open(filename,'rb') as f:
		filehash = hashlib.md5(f.read()).hexdigest()
		if filehash not in hash_keys:
			hash_keys[filehash] = index
		else:
			duplicates.append((index,hash_keys[filehash]))
			print("dup found:" + filename)

for index in duplicates:
	os.remove(file_list[index[0]])
