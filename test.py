import glob

for filename in glob.iglob('*.jpg', recursive=True):
    print(filename)