import os
import json
import csv
import pickle

PATH = "."
temp_dict_list = []


def get_data(path):
    for root, dirs, files in os.walk(path):
        data = get_objects(root, dirs, files, temp_dict_list)
    return data


def get_objects(root, dirs, files, temp_dict_list):
    temp_dict = {}
    temp_root = root.split('\\')[-1]
    temp_dict["name"] = temp_root
    temp_dict['type'] = "dir"
    temp_dict["parent"] = root
    temp_dict['size'] = os.path.getsize(str(root))
    temp_dict_list.append(temp_dict)
    for f in files:
        temp_dict = {}
        temp_dict["name"] = f
        temp_dict['type'] = "file"
        temp_dict["parent"] = root
        temp_dict['size'] = os.path.getsize(str(os.path.join(root, f)))
        temp_dict_list.append(temp_dict)
    return temp_dict_list


def write_data(data):
    with open('test.json', 'w', encoding="utf-8") as outfile:
        for d in data:
            json.dump(d, outfile, indent=1)

    headers = list(data[0])
    with open("test.csv", "w", encoding='utf-8') as outfile:
        file_writer = csv.DictWriter(outfile, delimiter=";", lineterminator="\r", fieldnames=headers)
        file_writer.writeheader()
        for d in data:
            file_writer.writerow(d)

    with open('test.pickle', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    data = get_data(PATH)
    write_data(data)