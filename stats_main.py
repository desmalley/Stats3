from flask import Flask
from My_Goog_Pack import goog_funcs as goog
from markupsafe import escape
from flask import render_template
import pprint as pp

from stats_classes import student, group


lol=goog.get_goog_data()
topics=lol[0]

lod=goog.lists_to_dicts(lol)

#pp.pprint(lod)    


students=[]
for row in lod:
    new_student=student(row)
    students.append(new_student)

#for student in students:
#    print(student.art_level)


print(group(students))
