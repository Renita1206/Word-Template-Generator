from docxtpl import DocxTemplate

doc = DocxTemplate("Assignment Template.docx")
course = input("Enter Course Name: ")
code = input("Enter Course Code: ")
title = input("Enter Assignment Tite: ")
assignment = input('Naming Convention: ') + '.docx'
path = 'C:\\Users\\Renita Kurian\\Downloads\\Assignment Files\\'
context = { 'course_name' : course, 'course_code': code, 'title': title}
doc.render(context)
doc.save(path+assignment)