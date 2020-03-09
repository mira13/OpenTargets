import json
import sys
import statistics
import urllib.request


targetScore = []
diseaseScore = []
sampleList = []


def targetAnalysis(targetName, targetList):
	vTarStddev, vTarMean, vTarMax, vTarMin = stand_dev(targetList)
	print("Standart deviation for target {} = {}".format(targetName, vTarStddev))
	print("Mean for target {} = {}".format(targetName, vTarMean))
	print("Max for target {} = {}".format(targetName, vTarMax))
	print("Min for target {} = {}".format(targetName, vTarMin))

def diseaseAnalysis(diseaseName, diseaseList):
	vDisStddev, vDisMean, vDisMax, vDisMin = stand_dev(diseaseList)
	print("Standart deviation for disease {} = {}".format(diseaseName, vDisStddev))
	print("Mean for disease {} = {}".format(diseaseName, vDisMean))
	print("Max for disease {} = {}".format(diseaseName, vDisMax))
	print("Min for disease {} = {}".format(diseaseName, vDisMin))

def getData():
	url = 'https://platform-api.opentargets.io/v3/platform/public/association/filter'
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())

	return data

data = getData()

def stand_dev(val):
	stddev = statistics.stdev(val)
	meanv = statistics.mean(val)
	maxv = max(val)
	minv = min(val)
	return stddev, meanv, maxv, minv

def addToList(list, value):
	list.append(value)

def processData():
	for value in data['data']:
		print(json.dumps(value['id'], indent=4, sort_keys=True))
		
def runTests():
	print("Tests are ok!")
	
def findTarget(target):
	targetList = []
	for value in data['data']:
		if (value['target']['id'] == target):
			addToList(targetList, value['association_score']['overall'])
	return targetList
	

def findDisease(disease):
	diseaseList = []
	for value in data['data']:
		if (value['disease']['id'] == disease):
			addToList(diseaseList, value['association_score']['overall'])
	return diseaseList

def generalAnalysis():
	print("General Analysis")
	generalList = []
	for value in data['data']:
		addToList(generalList, value['association_score']['overall'])
	return generalList

def AllFileAnalyze():
	generalList = generalAnalysis()
	vStddev, vMean, vMax, vMin = stand_dev(generalList)
	print("Standart deviation = {}".format(vStddev))
	print("Mean = {}".format(vMean))
	print("Max = {}".format(vMax))
	print("Min = {}".format(vMin))
