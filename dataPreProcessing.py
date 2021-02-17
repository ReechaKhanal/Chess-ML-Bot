import pandas
class dataPreProcessing():

	def __init__(self):
		pass

	def startDataPreProcessing(self, df):
		
		# drop all columns deemed unessential as of now
		df = df.drop(['Event', 'Site', 'Date', 'UTCDate', 'UTCTime', 'TimeControl', 'ECO', 'Termination'], axis=1)
		df = df.drop(['WhiteElo', 'BlackElo', 'WhiteRatingDiff', 'BlackRatingDiff', 'Variant', 'Result'], axis=1)
		
		
		# modifycolumns "White"	and "Black"
		df.loc[df['White'] == ' "Rkitty"', 'NW'] = 1
		df.loc[df['White'] != ' "Rkitty"', 'NW'] = 0

		df.loc[df['Black'] == ' "Rkitty"', 'NB'] = 1
		df.loc[df['Black'] != ' "Rkitty"', 'NB'] = 0

		return df