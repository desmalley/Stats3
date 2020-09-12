import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


json_key='stats-3-apr-2020-eabd06cd7b45.json'
file_name='Student Initial Info (Responses)'
username_col= 1#username column index in sheet (python style starting at 0)

scope = [ 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key,scope)
gc = gspread.authorize(credentials)


#********SHEET API LIST FUNCS*************************************
#*****************************************************************
def get_goog_data():
    wks= gc.open(file_name).sheet1 #gives first sheet of this file
    #pprint(wks.get_all_records())
    lol=[]
    for row in range(len(wks.get_all_records())+1):
        #print(wks.row_values(row+1))
        lol.append(wks.row_values(row+1))
    return lol
#wks.append_row(["into first col","into second col"])

def find_user(username,list_of_lists):
        user_list=[]
        for elem in list_of_lists:
            if username in elem[username_col]:     
#                if username == elem[username_col]: #strict
                user_list=elem
        return user_list
        
def make_same_len(topic_list,user_list):
    for entry in range(len(topic_list)-len(user_list)):
        user_list.append("not included")
    return user_list        

def convert_to_dict(my_list_short, keys):
        my_dict={}
        my_list=make_same_len(keys, my_list_short)
        for index in range(len(keys)):
                my_dict.update({keys[index]:my_list[index]})
        return my_dict
        
#********SHEET API DICT FUNCS*************************************       
#*****************************************************************        
def lists_to_dicts(list_of_lists):
    topics=list_of_lists[0]
    topic_num=len(topics)
    rows=list_of_lists[1:]
    list_of_dicts=[]
    for row in rows:
        stud_dict={}
        for topic_index in range(topic_num):
            try:
                key=topics[topic_index]
                value=row[topic_index]
                stud_dict.update({key:value})  
            except IndexError:
                key=topics[topic_index]
                value=None
                stud_dict.update({key:value})  
        list_of_dicts.append(stud_dict)
    return list_of_dicts
        
def find_user_dict(username,list_of_dicts):
    user_dict={}
    for elem in list_of_dicts:
        if username in elem['First Name'].lower() or username in elem['Last Name'].lower():     
#                if username == elem[username_col]: #strict
            user_dict=elem
    return user_dict        
        