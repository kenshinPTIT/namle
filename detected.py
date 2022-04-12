from importlib.resources import path
import json
import os
from simplejson import load

def is_json(json_string):
  try:
    json.loads(json_string)
  except ValueError as e:
    return False
  return True

# with open("AppIP.json", 'r') as fp:
with open("NewAppIP.json", 'r') as fp:

    AppData = json.load(fp)

for filename in os.listdir("24:5e:be:5c:a1:49"):
# for filename in os.listdir("NewData"):
    with open(os.path.join("24:5e:be:5c:a1:49", filename), 'r') as f:
    # with open(os.path.join("NewData", filename), 'r') as f:
        text = f.read()
        if is_json(text) == True:
            listObj = json.loads(text)
            for flow_entry in  listObj['flows']['br-lan']:
                if flow_entry['detected_application_name'] in AppData:
                    # print(flow_entry['detected_application_name'])
                    if flow_entry['other_ip'] not in AppData[flow_entry['detected_application_name']]['ip_list']:
                        print(flow_entry['other_ip'])
                        new_ip_data_set = {flow_entry['other_ip']: flow_entry['other_port']}
                        AppData[flow_entry['detected_application_name']]['ip_list'].update(new_ip_data_set)
                    if "host_server_name" in flow_entry:
                        if flow_entry['host_server_name'] not in AppData[flow_entry['detected_application_name']]['host_server_name'] :
                            print(flow_entry['host_server_name'])
                            AppData[flow_entry['detected_application_name']]['host_server_name'].append(flow_entry['host_server_name'])
                else:
                    ip = { flow_entry['other_ip']: flow_entry['other_port']}
                    if "host_server_name" in flow_entry:
                        host = [flow_entry['host_server_name']]
                    else:
                        host = []
                    new_data_set =  { flow_entry['detected_application_name'] : { "ip_list" : ip, "host_server_name" : host } }
        else:
            print("This file is not in json fomat",filename)

x_file_name = 'NewAppIP.json'
with open(x_file_name, 'w') as json_file:
    str_rp = str(AppData)
    str_rp = str_rp.replace("'",'"')
    json_file.write(str_rp)