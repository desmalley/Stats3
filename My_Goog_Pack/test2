lol=[["name","age","favorite color"]["daniel","41", "blue"]["jeff","13", "orange"]["Neal","17"]]

topics=lol[0]
rows=lol[1:]

lod=[]
print(range(topics))
for row in rows:
    stud_dict={}
    for topic_index in range(topics):
        if row[topic_index]:
            key=topics[topic_index]
            value=row[topic_index]
            stud_dict.update({key:value})   
        else:
            key=topics[topic_index]
            value=None
            stud_dict.update({key:value})            
    lod.append(stud_dict)

print(lod)
