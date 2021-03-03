seahawks_offense = ['Wilson', 'Metkalf', 'Lockett', 'Carson', 'Moore', 'Dissly', ]

hanson = ['Zac', 'Taylor', 'Isaac', ]

# python lists
seahawks_offense_copy = seahawks_offense.copy()
# seahawks_offense_copy.append('Prince')
# print(seahawks_offense_copy)
# seahawks_offense_copy.pop()
# print(seahawks_offense_copy)

# names_for_jerseys = []
# for name in seahawks_offense:
#     names_for_jerseys.append(name.upper())

# print(names_for_jerseys)

# python dictionaries
seahawks_offense = [{'Wilson': "QB"}, {'Metkalf': "WR"}, ]

{
    "Wilson": [{"QBR": 101}, {"TD": 289}]
}

hanson = {
    'Zac': ['drums'], 
    'Taylor': ["piano", "lead vocals"], 
    'Isaac': ["guitar"],
}

# print(hanson.get('Tristan'))
# print(hanson["Tristan"])

hanson['Tristan'] = ['trumpet']

for name, instrument in hanson.items():
    print(f'{name} plays the {instrument[0]}')
