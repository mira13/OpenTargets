import ProcessingToolboxA as pta
import sys
import subprocess

if __name__ == "__main__":

	if len (sys.argv) > 3:
		print ("Error. There are too many parametrs.")
		sys.exit (1)
	else:
		if (len (sys.argv) == 1):
			print ("Default config")
			pta.AllFileAnalyze()
		elif (len (sys.argv) == 2):
			param_name = sys.argv[1]
			if (param_name == "--test"):
				print ("Run tests!")
				subprocess.run(["python", "./TestA/test_TestA.py"])
			else:
				print ("Error. Undefined parametr.")
		elif (len (sys.argv) == 3):
			param_name = sys.argv[1]
			param_value = sys.argv[2]
			if (param_name == "-t"):
				print ("Run target analysis for {}".format(param_value))
				targetList = pta.findTarget(param_value)
				pta.targetAnalysis(param_value, targetList)
			elif (param_name == "-d"):
				print ("Run diseas analysis for {}".format(param_value))
				diseaseList = pta.findDisease(param_value)
				pta.diseaseAnalysis(param_value, diseaseList)
			else:
				print ("Error. Undefined parametr.")
				sys.exit (1)
