class normalizeData():

	def init(self):
		pass

	def getNormalizedFile(self):

		# convert the data in form of a dictionary
		data_dict = self.readFile()

		# get 'excel' rows from dictionary

	def readFile(self):

		# read all lines from the input line
		inputFile = open('ChessDataReecha.pgn', 'r')
		lines = inputFile.readlines()
		file_length = len(lines)

		index = 0
		column_data, total_data = {}, {}

		for line in lines:

			line.replace("\n", "")
			line = line.strip()

			if line == "":
				pass

			elif line.endswith("0-1") or line.endswith("1-0"):
				column_data["moves"] = line
				total_data[index] = column_data
				index = index+1
				column_data = {}

			else:
				line = line.replace("[", "")
				line = line.replace("]", "")

				index_of_seperation = line.index(' ')
				key, value = line[:index_of_seperation], line[index_of_seperation:]

				column_data[key] = value
		return total_data