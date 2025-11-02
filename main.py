import os
import shutil


dict_items = {"images" : [".jpg" , ".png"] ,
              "text files" : [".txt"] , 
              "pdf files" : [".pdf"] ,
              "word files" : [".docx"]
                }

path_main = input("give me a folder path to organize ")


for folder , extension in dict_items.items() :
    if not os.path.exists(os.path.join(path_main , folder)) :
        os.mkdir(os.path.join(path_main , folder))
            

for item in os.listdir(path_main) :
    for folder , extension in dict_items.items() :
        if item.endswith(tuple(extension)) :
            source = os.path.join(path_main , item)
            destination = os.path.join(path_main , folder)
            shutil.move(source , destination)
        

