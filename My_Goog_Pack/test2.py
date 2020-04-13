lol=[["name","age","favorite color"],["daniel","41", "blue"],["jeff","13", "orange"],["Neal","17"]]



def list_of_dicts(list_of_lists):
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
