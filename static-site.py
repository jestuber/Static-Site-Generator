# static-site.py
#
# Usage:
# $ mkdir ~/my-new-blog
# $ cd ~/my-new blog
# $ python ~/Code/static-site.py bootstrap
# Generates site structure
#
# $ python ~/Code/static-site.py generate
# Converts entries in /content to html and moves them to /output

import argparse
import os
from shutil import copyfile
from utils import create_dir




parser = argparse.ArgumentParser()
parser.add_argument("action", help="'bootstrap' for new site, 'generate' to update files")
args = parser.parse_args()
print args.action



if args.action == 'bootstrap':
    # TODO check if site is already bootstrapped
    # TODO bootstrap static,template,content,pages files
    folders = ['static','templates','content','content/entries','content/pages','output']
    for folder in folders:
        create_dir(folder)
        src_folder = os.path.dirname(os.path.abspath(__file__)) + '/' + folder
        src_files = os.listdir(src_folder)
        for file_name in src_files:
            full_file_name = os.path.join(src_folder,file_name)
            full_dest_name = os.path.join(folder,file_name)
            if (os.path.isfile(full_file_name)):
                copyfile(full_file_name, full_dest_name)

    

elif args.action == 'generate':
    # TODO implement generator
    print('hi')

else:
    # TODO fail with  help message
    print('fail')



