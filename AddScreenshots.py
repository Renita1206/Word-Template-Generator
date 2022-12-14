import docx
import os
full_path = input("Path to Assignment(Including file name): ")
doc = docx.Document(full_path)

pathOfFolder = input("Path to Screenshots folder: ")
folders = os.listdir(pathOfFolder)

folders = sorted(folders)

for i in folders:
    #print(pathOfFolder+'\\'+i)
    doc.add_picture(pathOfFolder+'\\'+i)
doc.save(full_path)