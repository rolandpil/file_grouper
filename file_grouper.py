import os
import re

#directory the program will iterate
iter_dir = ''

os.chdir(iter_dir)

logged_type = []

def handler(file):
    #get suffix
    file_match = re.search("(?:.+\.)([0-z]+)",file)

    if file_match != None:
        suffix = file_match.group(1)
        target_dir = os.path.join(iter_dir,suffix)
        og_path = os.path.join(iter_dir,file)
        new_path = os.path.join(target_dir,file)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        os.rename(og_path,new_path)


for file in os.listdir(iter_dir):
    fname = os.fsdecode(file)

    #this filters out directories
    if os.path.isfile(fname):
        handler(fname)