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
import codecs
import markdown
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile
from utils import create_dir

#Jinja2
env = Environment(loader=FileSystemLoader('templates'))
#Markdown
md = markdown.Markdown(extensions = ['markdown.extensions.meta'])


parser = argparse.ArgumentParser()
parser.add_argument("action", help="'bootstrap' for new site, 'generate' to update files")
args = parser.parse_args()
print args.action



if args.action == 'bootstrap':
    # TODO check if site is already bootstrapped
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
    # TODO implement metadata
    # TODO implement other templates
    folders = ['content/','content/entries/','content/pages/']
    for folder in folders:
        src_files = os.listdir(folder)
        for file_name in src_files:
            if file_name[-3:] == '.md':
                input_file = codecs.open(folder + file_name, mode="r", encoding="utf-8")
                text = input_file.read()
                html = md.convert(text)

                template = env.get_template('entry.html')
                new_file = template.render(content=html, meta=md.Meta)

                subfolder = "output/" + folder.split('/')[1]
                create_dir(subfolder)
                out_full_name = subfolder + '/' + file_name[:-3] + ".html"  # good god this is horrid
                output_file = codecs.open(out_full_name, "w", 
                          encoding="utf-8", 
                          errors="xmlcharrefreplace"
                )
                output_file.write(new_file)
                
    print('hi')

else:
    # TODO fail with  help message
    print('fail')



