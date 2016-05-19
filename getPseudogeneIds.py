import os
ids=set()
for file in os.listdir("C:/Users/Andre/Desktop/Work files/Dothistroma/Ate pseudogenisation files/pseudogene_data_dotse"):
    ids.add(file[6:12])
for id in ids:
    print id
