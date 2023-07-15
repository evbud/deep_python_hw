"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку."""

import csv
import pickle


def print_pickle_from_csv(file_csv: str) -> None:
    with open(file_csv, 'r', encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter='\t')

        csv_dict_list = []
        for i, (level, user_id, user_name, hash_val) in enumerate(csv_data):
            if i:
                csv_dict_list.append({
                    'level': level,
                    'ID': user_id,
                    'name': user_name,
                    'hash': hash_val,
                })

        print(f'{csv_dict_list = }')
        csv_dict_pickle = pickle.dumps(csv_dict_list, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{csv_dict_pickle = }')


def print_pickle_from_csv_rl(file_name):
    with open(file_name, encoding='utf-8') as file:
        csv_data = file.readlines()

    data_fields = csv_data[0][:-1].split('\t')
    csv_dict_list = []
    for item in csv_data[1:]:
        level, id_num, name, hash_vol = item[:-1].split('\t')
        csv_dict_list.append({
            data_fields[0]: level,
            data_fields[1]: id_num,
            data_fields[2]: name,
            data_fields[3]: hash_vol
        })

    print(f'{csv_dict_list = }\n{pickle.dumps(csv_dict_list) = }')


if __name__ == '__main__':
    print_pickle_from_csv('task_06.csv')
    print_pickle_from_csv_rl('task_06.csv')
