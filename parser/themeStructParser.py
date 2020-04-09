import json

themeStruct = {
    "foreground":{},
    "background":{},
    "fontStyle":{},
    "colors": {}
}

sortedStruct = {
    "foreground":{},
    "background":{},
    "fontStyle":{},
    "colors": {}
}

colorMap = {
}

with open('example.json') as example:
    data = json.load(example)

# Parsing rules for foreground
for rule in data['rules']:
    if rule['foreground'] not in themeStruct['foreground']:
        themeStruct['foreground'][rule['foreground']] = list()
    themeStruct['foreground'][rule['foreground']].append(rule['token'])

# Parsing rules for background
for rule in data['rules']:
    if 'background' in rule:
        if rule['background'] not in themeStruct['background']:
            themeStruct['background'][rule['background']] = list()
        themeStruct['background'][rule['background']].append(rule['token'])

# Parsing rules for fontStyle
for rule in data['rules']:
    if 'fontStyle' in rule:
        if rule['fontStyle'] not in themeStruct['fontStyle']:
            themeStruct['fontStyle'][rule['fontStyle']] = list()
        themeStruct['fontStyle'][rule['fontStyle']].append(rule['token'])

# Parsing colors and removing the '#'
for color in data['colors']:
    if color[1:] not in themeStruct['colors']:
        themeStruct['colors'][data['colors'][color][1:]] = list()
    themeStruct['colors'][data['colors'][color][1:]].append(color)

# Rename colors
i = 0
for color in themeStruct['foreground']:
    i += 1
    sortedStruct['foreground']["color_" + str(i).zfill(2)] = themeStruct['foreground'][color]
    colorMap["color_" + str(i).zfill(2)] = color
for color in themeStruct['colors']:
    i += 1
    sortedStruct['colors']["color_" + str(i).zfill(2)] = themeStruct['colors'][color]
    colorMap["color_" + str(i).zfill(2)] = color
for color in themeStruct['background']:
    i += 1
    sortedStruct['background']["color_" + str(i).zfill(2)] = themeStruct['background'][color]
    colorMap["color_" + str(i).zfill(2)] = color
i = 0
for fontStyle in themeStruct['fontStyle']:
    i += 1
    sortedStruct['fontStyle']["fontStyle_" + str(i).zfill(2)] = themeStruct['fontStyle'][fontStyle]


with open('themeExample.json', 'w') as newFile:
    newFile = json.dump(themeStruct, newFile, indent=4, sort_keys=True)
with open('themeStruct.json', 'w') as newFile:
    newFile = json.dump(sortedStruct, newFile, indent=4, sort_keys=True)
with open('colorMap.json', 'w') as newFile:
    newFile = json.dump(colorMap, newFile, indent=4, sort_keys=True)
