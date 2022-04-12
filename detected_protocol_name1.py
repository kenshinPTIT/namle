import json
import glob,os ,pandas as pd 
val = {}
data =[]
dataList = []
# files = glob.glob('/home/anh/Downloads/Telegram Desktop/24_5e_be_5c_a1_49/24:5e:be:5c:a1:49/*', recursive=True)
# files = glob.glob('/home/luongquan/Desktop/Json_python/manhan/*', recursive=True)

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append (os.path.abspath(f))
    return all_files

songs = get_files ('/home/namlv/Documents/Study/Project_LANNET/24_5e_be_5c_a1_49.tar (2)/24:5e:be:5c:a1:49')


# filepath = songs[0]
# df = pd.read_json(filepath,lines = True)
# song_list = []
# for song in songs:
#     with open(song) as doc:
#         # exp = json.load(doc)
#         song_list.append(exp)

# song_list[:2]
json_obj = json.dumps(data, indent = 4)
with open('qdata.json', 'w') as file:
    file.write(json_obj)


for single_file in songs:
    dataList.append(single_file)
newdataList = sorted(dataList)


for single_file in newdataList:
    with open(single_file) as json_file:
        try:
            appData = json.load(json_file)
            nameValue2 = []
            for key in appData['flows']:
                for i in range(0, len(appData['flows'][key])):
                    for key2 in appData['flows'][key][i]:
                        if(key2 == 'detected_application_name'):
                            nameValue2.append(appData['flows'][key][i][key2])


            formatlist = list(dict.fromkeys(nameValue2))

            def count(name1,name2):
                dem = 0
                for key in appData['flows']:
                    for i in range(0, len(appData['flows'][key])):
                        if appData['flows'][key][i][name2] == name1:
                            dem += 1 
                return dem

            def push(value,count):
                val[value] = count

            def out(name):
                for i in range(0, len(formatlist)):
                    push(formatlist[i],count(formatlist[i],name))

            out('detected_application_name')

            # json_obj = json.dumps(val, indent = 4)
            # with open('appData.json', 'w') as file:
            #     file.write(json_obj)
            
            def write_json(new_data, filename='qdata.json'):
                with open(filename,'r+') as file:
                    # First we load existing data into a dict.
                    file_data = json.load(file)
                    # Join new_data with file_data inside emp_details
                    file_data.append(new_data)
                    # Sets file's current position at offset.
                    file.seek(0)
                    # convert back to json.
                    json.dump(file_data, file, indent = 4)
            write_json(val)
# python object to be appended
        except KeyError:
            print(f'Skipping')


# print(appData['flows'][namekey[0]][0]['detected_application_name'])



# def count(name,name2):
#     dem = 0
#     for j in range(0,len(data)):
#         for i in data[j]['flow']:
#             if i == name2:
#                 if data[j]['flow'][i] == name:
#                     dem += 1
#     return dem

# def push(name,y):
#     val = {}
#     val['name'] = name
#     val['y'] = y
#     mlist.append(val)

# push('Unknown',count('Unknown','detected_application_name'))
# push('2100.netify.zalo',count('2100.netify.zalo','detected_application_name'))

# with open('data.json', 'w') as file:
#     file.write(val)
