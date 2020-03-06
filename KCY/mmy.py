import csv
import json

with open('temp.json', 'r+') as jsonfile:
    array = []
    with open("mmy.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)    
        next(reader)
        for row in reader:
            array.append(row)
    array.sort(key=lambda x: x[0], reverse=False)

    data = {}
    for row in array:
        data['name'] = row[0]
        data['id'] = row[0].replace(' ', '-')
        data['make'] = []
        data['make'].append({'name': row[1], 'id': row[1].replace(' ', '-').lower(), 'models': []})
        data['make'][0]['models'].append({'name': row[2], 'id': row[2].replace(' ', '-').lower()})    
        json.dump(data, jsonfile)
        jsonfile.write('\n')
    
    jsonfile.flush()
    jsonfile.seek(0)
    things = [json.loads(line) for line in jsonfile]

    new_things = {}
    for thing in things:        
        thing_id = thing['id']
        try:
            old_thing = new_things[thing_id]
        except KeyError:
            new_things[thing_id] = thing
        else:
            old_thing['make'].extend(thing['make'])
    new_things = new_things.values()

with open('mmy.json', 'r+') as f:
    f.truncate(0)
#     for thing in new_things:
#         f.write(json.dumps(thing) + '\n')
    for line in new_things:
        final_things = {}
        for col in line['make']:        
            col_id = col['id']
            try:
                old_col = final_things[col_id]
            except KeyError:
                final_things[col_id] = col
            else:
                old_col['models'].extend(col['models'])
        final_things = final_things.values()
        line['make'] = list(final_things)
        f.write(json.dumps(line) + ',\n')
