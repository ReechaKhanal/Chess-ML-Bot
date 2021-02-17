from collections import defaultdict;
import pandas as pd;

class getDetailedData():
	
	def __init__(self):
		pass

	def startParsingDataFrame(self, df):

		move_dict = {'Player': [],
					 'My Move': [],
					'Opponent Move': []}

		for index, row in df.iterrows():

			player = row['PlayerColor']
			moves = row['moves']

			if player == 1:
				i = 0
				while i < len(moves)-1:
					myMove = moves[i+0];
					opponentMove = moves[i+1];
					
					move_dict['Player'].append(player);
					move_dict['My Move'].append(myMove);
					move_dict['Opponent Move'].append(opponentMove);

					i = i + 2

			else:
				prev = ''
				i = 0
				while i < len(moves)-1:
					myMove = prev
					opponentMove = moves[i]
					prev = moves[i+1]

					move_dict['Player'].append(player);
					move_dict['My Move'].append(myMove);
					move_dict['Opponent Move'].append(opponentMove);

					i = i + 2

		df = pd.DataFrame.from_dict(move_dict)
		return df