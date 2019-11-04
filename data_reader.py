import random

class Reader():
	def csv(self, file):
		with open(file, 'r') as csv_file:
			self.data = csv_file.read()

		return self.data


	def X_y_split(self, data, columns):
		self.split_data = data.replace("\n", ",").split(",")
		y = []
		X = []
		y_column = 0

		for i in range(int(len(self.split_data)/columns)):
			y_column += (columns-1)
			X_columns = y_column - (columns-1)
			X.append(self.split_data[X_columns:y_column])
			y.append(self.split_data[y_column])
			y_column += 1

		for color_lists in range(len(X)):
			for color in range(len(X[color_lists])):
				X[color_lists][color] = int(X[color_lists][color])

		for colors in range(len(y)):
			y[colors] = int(y[colors])
		
		return X, y


	#def train, test split
	def split_train_test(self, X, y, randomized=True, train_size = 0.6):
		X_train_set = []
		y_train_set = []
		X_test_set = []
		y_test_set = []

		if randomized:
			reached_end = False
			already_called = []
			# for i in range(int(len(X)*(train_size))):
			while reached_end == False:	
				rand = random.randint(0, len(X)-1)
				if rand not in already_called:
					X_train_set.append(X[rand])
					y_train_set.append(y[rand])
					already_called.append(rand)

				if len(already_called) == round(len(X)*train_size):
					reached_end = True

		else: 
			for i in range(int(len(X) * (train_size))):
				X_train_set.append(X[i])
				y_train_set.append(y[i])

		for j in range(len(X)):
			if j not in already_called:
				X_test_set.append(X[j])
				y_test_set.append(y[j])

		return X_train_set, X_test_set, y_train_set, y_test_set
