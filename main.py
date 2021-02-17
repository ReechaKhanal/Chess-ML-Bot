from normalizeData import normalizeData
from dataPreProcessing import dataPreProcessing

def main():
	nd = normalizeData()
	df = nd.getNormalizedFile()

	dpp = dataPreProcessing()
	df = dpp.startDataPreProcessing(df)

	df.to_csv("NormalizedFile.csv", index=False)
	#(nd.getNormalizedFile()).to_csv("NormalizedFile.csv")

if __name__ == '__main__':
	main()