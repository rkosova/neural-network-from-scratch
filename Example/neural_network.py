from data_reader import Reader

# Initialize reader
reader = Reader()

#Read CSV data
reader.csv('data.csv')

#Format to X and y columns
X, y = reader.X_y_split(reader.data, 4)

X_train, X_test, y_train, y_test = reader.split_train_test(X, y)
