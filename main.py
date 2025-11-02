import os
import shutil

text_files =[]
pdf_files = []

path_main = input("give me a folder path to organize ")


name_sub_text = "text files"
path_sub_text = os.path.join(path_main , name_sub_text)

name_sub_pdf = "pdf files"
path_sub_pdf = os.path.join(path_main , name_sub_pdf)

if any(f.endswith(".txt") for f in os.listdir(path_main)):
    if not os.path.exists(path_sub_text):
        os.mkdir(path_sub_text)

if any(f.endswith(".pdf") for f in os.listdir(path_main)):
    if not os.path.exists(path_sub_pdf):
        os.mkdir(path_sub_pdf)


for f in os.listdir(path_main):
    if f.endswith(".txt") :
        source = os.path.join(path_main, f)
        destination = path_sub_text
        shutil.move(source , destination)
        text_files.append(f)
    elif f.endswith(".pdf") :
        source = os.path.join(path_main, f)
        destination = path_sub_pdf
        shutil.move(source , destination)
        pdf_files.append(f)


