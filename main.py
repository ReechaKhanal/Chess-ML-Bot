from normalizeData import normalizeData

def main():
	nd = normalizeData()
	(nd.getNormalizedFile()).to_csv("NormalizedFile.csv")


if __name__ == '__main__':
	main()