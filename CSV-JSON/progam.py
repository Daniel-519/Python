import os
import json


def main():
    filename = os.path.join('data', 'ymm.csv')
    data = get_data_csv(filename)
    data = sorted(data, key=lambda x: (x[0], x[1]))
    total_count = len(data)
    item_count = 0
    result = []
    make = []
    model = []
    for item in data:
        if item_count == total_count - 1:
            model.append({'name': item[2], 'id': '-'.join(item[2].lower().split(' '))})
            make.append({'name': item[1], 'id': item[1].lower(), 'models': model})
            result.append({'name': item[0], 'id': item[0].lower(), 'make': make})
        else:
            if item[0] == data[item_count+1][0]:
                if item[1].lower() == data[item_count + 1][1].lower():
                    model.append({'name': item[2], 'id': '-'.join(item[2].lower().split(' '))})
                    item_count += 1
                    continue
                else:
                    model.append({'name': item[2], 'id': '-'.join(item[2].lower().split(' '))})
                    added_model = model.copy()
                    make.append({'name': item[1], 'id': item[1].lower(), 'models': added_model})
                    model.clear()
                    item_count += 1
                    continue
            else:
                model.append({'name': item[2], 'id': '-'.join(item[2].lower().split(' '))})
                added_model = model.copy()
                make.append({'name': item[1], 'id': item[1].lower(), 'models': added_model})
                added_make = make.copy()
                result.append({'name': item[0], 'id': item[0].lower(), 'make': added_make})
                model.clear()
                make.clear()
                item_count += 1
                continue
    # print(result)
    file_write(result)


def get_data_csv(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        lines = []
        for line in fin:
            line_data = line.strip().split(',')
            if len(line_data) > 1:
                lines.append(line_data)
        return lines


def file_write(result):
    with open(os.path.join('data', 'output.json'), 'w') as fout:
        json.dump(result, fout, indent=4)


if __name__ == '__main__':
    main()
