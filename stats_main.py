from flask import Flask
from My_Goog_Pack import goog_funcs as goog
from markupsafe import escape
from flask import render_template
import pprint as pp

from stats_classes import student, group


lol=goog.get_goog_data()
topics=lol[0]

lod=goog.lists_to_dicts(lol)

#Gather students
students=[]
for row in lod:
    new_student=student(row)
    students.append(new_student)

my_group=group(students)
#Helper functions
def find_stud(username, group_obj):
    for student in group_obj.students:  
        if username.lower() in student.name.lower():
            return student
    

#Start Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Bello, World!'

#@app.route('/index')
#def compare():
#        return render_template('compare.html',topics=topics, lol=lol[1:])

@app.route('/user/<username>')
def show_user_profile(username):
        
        my_stud=find_stud(username, my_group)
        print(my_stud)
        return render_template('spec.html',my_stud=my_stud)




