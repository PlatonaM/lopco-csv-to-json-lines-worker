"""
   Copyright 2021 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import os
import uuid
import json
import requests


dep_instance = os.getenv("DEP_INSTANCE")
job_callback_url = os.getenv("JOB_CALLBACK_URL")
input_file = os.getenv("source_csv")
delimiter = os.getenv("delimiter")
sub_tab_headers = os.getenv("sub_table_headers").split(",")
sub_tab_delimiters = os.getenv("sub_table_delimiters").split(",")
data_cache_path = "data_cache"


sub_tab_maps = dict()
for item in sub_tab_headers:
    item = item.split(":")
    header = item[1].split(";")
    sub_tab_maps[item[0]] = {pos: header[pos] for pos in range(len(header))}

output_file = uuid.uuid4().hex

print("converting ...")
with open("{}/{}".format(data_cache_path, input_file), "r") as in_file:
    with open("{}/{}".format(data_cache_path, output_file), "w") as out_file:
        line_count = 0
        first_line = in_file.readline().strip().split(delimiter)
        line_len = len(first_line)
        line_map = dict()
        for pos in range(line_len):
            line_map[pos] = first_line[pos]
        for line in in_file:
            line = line.strip().split(delimiter)
            new_line = dict()
            for pos in range(line_len):
                field = line_map[pos]
                if field not in sub_tab_maps:
                    new_line[field] = line[pos]
                else:
                    sub_tabs = line[pos]
                    new_line[field] = list()
                    if sub_tabs:
                        sub_tabs = sub_tabs.split(sub_tab_delimiters[1])
                        for sub_tab in sub_tabs:
                            sub_tab = sub_tab.split(sub_tab_delimiters[0])
                            sub_tab_map = sub_tab_maps[field]
                            sub_dict = dict()
                            for _pos in range(len(sub_tab)):
                                sub_dict[sub_tab_map[_pos]] = sub_tab[_pos]
                            new_line[field].append(sub_dict)
            out_file.write(json.dumps(new_line) + "\n")
            line_count += 1


with open("{}/{}".format(data_cache_path, output_file), "r") as file:
    for x in range(5):
        print(file.readline().strip())
print("total number of lines written: {}".format(line_count))

try:
    resp = requests.post(
        job_callback_url,
        json={dep_instance: {"output_file": output_file}}
    )
    if not resp.ok:
        raise RuntimeError(resp.status_code)
except Exception as ex:
    try:
        os.remove("{}/{}".format(data_cache_path, output_file))
    except Exception:
        pass
    raise ex
