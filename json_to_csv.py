import csv
import json
import time


def extract_dict_from_text(text):
    # 从文本中提取字典数据
    extracted_dicts = []
    tokens = text.split()
    for i, token in enumerate(tokens):
        try:
            dict_str = ""
            if token.startswith("{"):
                # 寻找字典的结尾位置
                count = 0
                for j in range(i, len(tokens)):
                    dict_str += tokens[j]
                    count += tokens[j].count("{")
                    count -= tokens[j].count("}")
                    if count == 0:
                        break
            if dict_str:
                # 将字符串转换为字典对象并添加到提取的字典列表中
                extracted_dicts = json.loads(dict_str)
                print("[+] json数据提取成功！✨")
                # print(extracted_dicts)
                print("------------------------------------")
                break
        except SyntaxError:
            pass
    return extracted_dicts


def count_duplicate_dicts(dict_list):
    unique_dicts = set(map(str, dict_list))
    return len(dict_list) - len(unique_dicts)


def print_dict_structure(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(f"{' ' * indent}{key}:")
            print_dict_structure(value, indent + 2)
        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
            print(f"{' ' * indent}{key} (list) - {len(value)} elements:")
            print_dict_structure(value[0], indent + 2)
        else:
            print(f"{' ' * indent}{key}")


def search_dict(data, search_key):
    if search_key in data and isinstance(data[search_key], list):
        print(f"[√] 找到键名对应数据：{search_key}")
        return data[search_key]
    else:
        for key, value in data.items():
            if isinstance(value, dict):
                found = search_dict(value, search_key)
                if found:
                    return found


def write_dict_to_csv(data_list, filename):
    # 将字典数据写入CSV文件
    if not data_list:
        return
    nums = len(data_list)
    print(f"[√] 检测到{nums}条数据")
    keys = data_list[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data_list)


def print_dict_keys(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(f"{' ' * indent}{key}:")
            print_dict_keys(value, indent + 2)
        else:
            print(f"{' ' * indent}{key}")


filename = input("[*] 请输入待处理文件名：")
with open(filename, 'r', encoding="utf-8") as file:
    file_data = file.read()
# 提取字典数据
extracted_dict = extract_dict_from_text(file_data)
# 打印字典的键和子键树形结构
print("\n[+] 数据结构解析如下👏")
print("------------------------------------")
print_dict_structure(extracted_dict)
print("------------------------------------")


def get_selected_data(extracted_dict):
    # 获取选择的数据
    # 输入键名并检索数据
    search_key = input("[*] 请输入要检索的键名(如：data)：")
    selected_data = search_dict(extracted_dict, search_key)
    return selected_data


# 获取当前时间戳
timestamp = int(time.time())

# 将时间戳转换为字符串
timestamp_str = str(timestamp)

selected_data = get_selected_data(extracted_dict)

if selected_data:
    filename = f"selected_data{timestamp_str}.csv"
    write_dict_to_csv(selected_data, filename)
    print(f"[+] 数据已写入文件：{filename}，请查看😀")
else:
    print("[-] 所选键的值不是一个由相同结构的字典组成的列表😢")
