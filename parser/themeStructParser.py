import json

themeStruct = {
}
sortedStruct = {
}
with open('example.json') as example:
    data = json.load(example)

# Parsing rules
for rule in data['rules']:
        if rule['foreground'] not in themeStruct:
            themeStruct[rule['foreground']] = list()
        themeStruct[rule['foreground']].append(rule['token'])

# Parsing colors and removing the '#'
for color in data['colors']:
        if color[1:] not in themeStruct:
            themeStruct[data['colors'][color][1:]] = list()
        themeStruct[data['colors'][color][1:]].append(color)

# Rename colors
i = 0
for color in themeStruct:
    i += 1
    sortedStruct["color_" + str(i).zfill(2)] = themeStruct[color]

with open('themeStruct.json', 'w') as newFile:
    newFile = json.dump(sortedStruct, newFile, indent=4, sort_keys=True)
