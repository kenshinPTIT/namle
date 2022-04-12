import json
import glob,os
from simplejson import load

listDeProName = []
listDeProNameok = []
dataList = []
listServer = []
listServerOk = []
dictServer = dict()

def is_json(json_string):
    try:
        json.loads(json_string)
    except ValueError as e:
        return False
    return True

def ktra(s):
    ok = False
    for x in listDeProNameok:
        if (s==x):
            ok = True
            break
    return(ok)

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append (os.path.abspath(f))
    return all_files
songs = get_files ('/home/namlv/Documents/Study/Project_LANNET/24_5e_be_5c_a1_49.tar (2)/24:5e:be:5c:a1:49')


for single_file in songs:
    dataList.append(single_file)
newdataList = sorted(dataList)

# for x in range(len(newdataList)):
#     f = open(newdataList[x])
#     data = json.load(f)
#     for u in data["flows"]:
#         print(u)   

# for x in range(len(newdataList)):
#     f = open(newdataList[x])
#     data = json.load(f)
#     for u in data['flows']['br-lan']:
#         detected_protocol_name = u['detected_protocol_name']
#         print(detected_protocol_name)

# f = open(newdataList[1])
# data = json.load(f)
# for u in data['flows']['br-lan']:
#     detected_protocol_name = u['detected_protocol_name']
#     print(detected_protocol_name)

for file in newdataList:
    with open(file) as json_file:
        t = json_file.read()
        if is_json(t):
            data = json.loads(t)
            try:
                for u in data['flows']['br-lan']:
                    try:
                        for i in range(0, len(u)):
                            try:
                                data_name = data['flows']['br-lan'][i]['detected_application_name']
                                listDeProName.append(data_name)
                            except:
                                print("skipping_1")
                    except:
                        print("skipping_2")
            except:
                print("skipping_3")

for x in listDeProName:
    if(ktra(x) == False):
        listDeProNameok.append(x)

for x in listDeProNameok:
    NumAppe = listDeProName.count(x)
    data_dict = {
            "detected_protocol_name" : x,
            "number of appearances" : NumAppe
        }
    print(x, "ok")
    with open("detected_protocol_name123.json", 'a+') as file:
        json.dump(data_dict, file, sort_keys=True, indent=4)
        file.write(",\n")
        