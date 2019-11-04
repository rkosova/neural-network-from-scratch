from data_reader import Reader

# Initialize reader
reader = Reader()

#Read CSV data
reader.csv('data/color_data.csv')

#Format to X and y columns
X, y = reader.X_y_split(reader.data, 4)

X_train, X_test, y_train, y_test = reader.split_train_test(X, y)

print(X_train)
print(y_train)
print(len(X_train))
print(len(y_train))

print(X_test)
print(y_test)
print(len(X_test))
print(len(y_test))