import json

print('Dit zijn de namen, codes en types van elk station:')

with open('test1.json', 'r') as json_file:
    data = json.load(json_file)

    usd_rates = dict()
    for lange_station in data['payload']:


        print((lange_station['namen']['lang']) + ' - ', (lange_station['code']) + '     :',
              (lange_station['stationType']))

    for i in data['payload']:
        station = i['namen']['lang']
        lang = i['lng']
        usd_rates[lang] = station
    print('\n''Het meest oostelijk gelegen station is:', usd_rates[13.4346995])

