from docxtpl import DocxTemplate
import docx
import os
from docx.shared import Inches

doc = DocxTemplate("Assignment Template.docx")
course = input("Enter Course Name: ")
code = input("Enter Course Code: ")
title = input("Enter Assignment Title: ")
assignment = input('Naming Convention: ') + '.docx'
path = 'C:\\Users\\Renita Kurian\\Downloads\\Assignment Files\\'
context = { 'course_name' : course, 'course_code': code, 'title': title}
doc.render(context)
full_path = path+assignment
doc.save(full_path)

add_ss = input("Do you want to add screenshots?(Enter 1): ")
if(add_ss=='1'):
    doc = docx.Document(full_path)

    pathOfFolder = 'C:\\Users\\Renita Kurian\\Downloads\\Assignment Files\\Screenshots'
    folders = os.listdir(pathOfFolder)

    folders = sorted(folders)

    for i in folders:
        #print(pathOfFolder+'\\'+i)
        doc.add_picture(pathOfFolder+'\\'+i, width=Inches(7), height=Inches(3.5))
doc.save(full_path)

print("Assignment has been added to folder")
input()