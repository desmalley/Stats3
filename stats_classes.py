


def level_check(level):
    if level:    
        return int(level)
    else: 
        return 0


class student:
    def __init__(self, stud_dict):
        self.data=stud_dict
        self.name=stud_dict['First Name']
        self.code_level=level_check(stud_dict['Code Level'])
        self.art_level=level_check(stud_dict['What is your art level'])
        self.shop_level=level_check(stud_dict['Shop Level'])
        self.fab_level=level_check(stud_dict['Fab Level'])
        self.writing_level=level_check(stud_dict['Writing Level'])
        self.personality=stud_dict['My personality code is']

    def __repr__(self):
        return '''name={}
        code level={}
        art level={}
        shop level={}
        fab level={}
        writing level={}
        Personality Code= {}
        '''.format(self.name,self.code_level,self.art_level,self.shop_level,self.fab_level,self.writing_level,self.personality)

class group:
    def __init__(self, students):
        self.students=students
        self.names=[student.name for student in students]         
        self.code_ranked=sorted(students, key = lambda i: i.code_level) 
        self.art_ranked=sorted(students, key = lambda i: i.art_level)        
        self.shop_ranked=sorted(students, key = lambda i: i.shop_level)         
        self.fab_ranked=sorted(students, key = lambda i: i.fab_level)
        self.writing_ranked=sorted(students, key = lambda i: i.writing_level) 
            
    def __repr__(self, top_num=5):
        top_coders=[coder.name for coder in self.code_ranked[:top_num]]
        top_artists=[artist.name for artist in self.art_ranked[:top_num]]
        top_shoppers=[shopper.name for shopper in self.shop_ranked[:top_num]]
        top_fabbers=[fabber.name for fabber in self.fab_ranked[:top_num]]
        top_writers=[writer.name for writer in self.writing_ranked[:top_num]]
    
    
        return '''Group Stats
        members= {}
        top coders={}
        top artists={}
        top makers={}
        top fabbers={}
        top writers={}
        '''.format(self.names,top_coders,top_artists,top_shoppers,top_fabbers,top_writers)        
        