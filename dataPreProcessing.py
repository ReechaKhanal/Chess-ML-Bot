import pandas
class dataPreProcessing():

	def __init__(self):
		pass

	def startDataPreProcessing(self, df):
		
		# drop all columns deemed unessential as of now
		df = df.drop(['Event', 'Site', 'Date', 'UTCDate', 'UTCTime', 'TimeControl', 'ECO', 'Termination'], axis=1)
		df = df.drop(['WhiteElo', 'BlackElo', 'WhiteRatingDiff', 'BlackRatingDiff', 'Variant', 'Result'], axis=1)
		
		
		# add a 
		df.loc[df['White'] == ' "Rkitty"', 'PlayerColor'] = 1
		df.loc[df['White'] != ' "Rkitty"', 'PlayerColor'] = 0

		# We no longer need the columns 'White' & 'Black'
		df = df.drop(['White', 'Black'],  axis=1)

		return df