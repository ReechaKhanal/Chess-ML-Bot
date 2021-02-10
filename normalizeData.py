from collections import defaultdict;
import pandas as pd

class normalizeData():

	def init(self):
		pass

	def getNormalizedFile(self):

		# convert the data in form of a dictionary
		all_columns, data_dict = self.readFile()

		# change data_dict to contain all_columns:
		data_dict = self.modifyDataDict(all_columns, data_dict)

		# get a finalized and easy to use dictionary
		data_dict = self.getFinalizedDataDict(all_columns, data_dict)

		# convert dictionary to dataframe
		df = pd.DataFrame.from_dict(data_dict)

		return df


	def getFinalizedDataDict(self, all_columns, data_dict):

		final_dict = defaultdict(list)

		for index, inner_dict in data_dict.items():

			for key, value in inner_dict.items():

				final_dict[key].append(value)

		return final_dict


	def modifyDataDict(self, all_columns, data_dict):

		for index, inner_dict in data_dict.items():

			for column_name in all_columns:
				if column_name not in inner_dict:

					inner_dict[column_name] = None

			data_dict[index] = inner_dict

		return data_dict



	def readFile(self):

		# read all lines from the input line
		inputFile = open('ChessDataReecha.pgn', 'r')
		lines = inputFile.readlines()
		file_length = len(lines)
		all_columns = set()
		all_columns.add("moves")

		index = 0
		column_data, total_data = {}, {}

		for line in lines:

			line.replace("\n", "")
			line = line.strip()

			if line == "":
				pass

			elif line.endswith("0-1") or line.endswith("1-0") or line.endswith("1/2-1/2"):
				column_data["moves"] = line
				total_data[index] = column_data
				index = index+1
				column_data = {}

			else:
				line = line.replace("[", "")
				line = line.replace("]", "")

				index_of_seperation = line.index(' ')
				key, value = line[:index_of_seperation], line[index_of_seperation:]
				all_columns.add(key)
				column_data[key] = value
		
		
		return all_columns, total_data