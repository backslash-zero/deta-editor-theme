import json

with open('parser/colorMap.json') as file:
    colorMap = json.load(file)
with open('parser/themeStruct.json') as file:
    themeStruct = json.load(file)

theme = {
    "rules": [],
    "colors": {}
}

appended = False

for color in colorMap:
    if color == 'base':
        theme['base'] = colorMap[color]
    if color == 'inherit':
        theme['inherit'] = colorMap[color]
    if color in themeStruct['foreground']:
        for token in themeStruct['foreground'][color]:
            for colorBack in themeStruct['background']:
                for tokenBack in themeStruct['background'][colorBack]:
                    if tokenBack == token:
                        tmp = {'background': colorMap[colorBack], 'foreground': colorMap[color], 'token': token}
                        theme['rules'].append(tmp)
                        appended = True
            if appended == False:
                tmp = {'foreground': colorMap[color], 'token': token}
                theme['rules'].append(tmp)
            else:
                appended = True
    if color in themeStruct['colors']:
        theme['colors'][themeStruct['colors'][color]] = '#' + colorMap[color]
# need to handle style

with open('theme.json', 'w') as newFile:
    newFile = json.dump(theme, newFile, indent=4, sort_keys=True)
    #if color in colorMap['background']
    #if color in colorMap['colors']
