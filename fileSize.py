import pathlib

folder = pathlib.Path(r'C:\home\deneme')

p = folder.glob('**/*')

totalSize = 0 

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
    
for index,filepath in enumerate (p): 
    if (filepath.is_file()):
        totalSize += filepath.stat().st_size
        print('file:' + str(filepath.name) + ' size: ' + str(filepath.stat().st_size))
        print('total size: ' + sizeof_fmt(totalSize))


