def getJSONObjectFromLine(l):
    import json
    data = json.loads(l)

    return data

def getDataFromJSONObject(data):
    targetId_disease_Id = data['target']['id']+'&'+data['disease']['id']
    score = data['scores']['association_score']

    return targetId_disease_Id, score

def convertVal2List(dictionary):
    for key in dictionary:
        if (type(dictionary[key]) == list):
            continue
        else:
            value = dictionary[key]
            dictionary[key] = [value]

    return dictionary

def PutDataIntoDataStructure(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
    result = convertVal2List(dictionary)

    return result

def WriteResultAsCSV(dictionary):
    import csv
    outputf = '.\TestB\\output.csv'
    with open(outputf, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(dictionary)

def median_Top3(List):
    from statistics import median
    SortedTrimList = sorted(List, reverse=True)[:3]
    Mn = median(List)
    SortedTrimList.append(Mn)

    return SortedTrimList

def NormalizeResult(dict):
    output = {}
    for key in dict:
        output[key] = median_Top3(dict[key])

    return output

def processLine(dictionary, line):
    data = getJSONObjectFromLine(line)
    id, score = getDataFromJSONObject(data)
    PutDataIntoDataStructure(dictionary, id, score)

    return dictionary
