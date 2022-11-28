import json

favourite={'title': 'The witcher',
'year': 1988,
'type':'fantasy',
'characters':['Geralt','Ciri'],
'cool': True
}

json_file = open('favourite.json', 'w')
json.dump(favourite, json_file, indent = 4)

json_file.close()