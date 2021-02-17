from normalizeData import normalizeData
from dataPreProcessing import dataPreProcessing
from getDetailedData import getDetailedData

def main():
	nd = normalizeData()
	df = nd.getNormalizedFile()

	dpp = dataPreProcessing()
	df = dpp.startDataPreProcessing(df)

	dd = getDetailedData()
	df = dd.startParsingDataFrame(df)

	df.to_csv("DetailedFile.csv", index = False)
	
	# At this point, I have a detailed dataframe containing one move at a row
	# Next Step:
	# Evaluate every single move and convert it into a encoded format
	
if __name__ == '__main__':
	main()