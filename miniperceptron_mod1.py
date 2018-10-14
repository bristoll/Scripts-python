from csv import reader

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights


# extrar datos de entrenamiento del csv
archivo = "datos_entrenamiento.csv"
dataset = load_csv(archivo)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
str_column_to_int(dataset, len(dataset[0])-1)

#valores para el perceptron
l_rate = 0.1
n_epoch = 5
weights = train_weights(dataset, l_rate, n_epoch)

datos_problema = [7.627531214,2.759262235]#Datos de los que queremos obtener una prediccion
prediccion= predict(datos_problema,weights)
if prediccion > 0:
	resultado = "verdadero"
else:
	resultado = "falso"
print(weights)
print("El modelo predice que los datos tendran como resultado: " + resultado)
