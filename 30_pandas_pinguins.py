import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
# sns.pairplot(penguins, hue="species")
# plt.show()
print(penguins)
penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
print(penguins_filtered)
penguins_features = penguins_filtered.drop(columns=['species'])

import pandas as pd
target = pd.get_dummies(penguins_filtered['species'])
#print(target.head(20))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(penguins_features, target, test_size=0.2, random_state=0, shuffle=True, stratify=target)

from tensorflow import keras
from numpy.random import seed
seed(1)
from tensorflow.random import set_seed
set_seed(2)

# inputs = keras.Input(shape=X_train.shape[1])
# hidden_layer = keras.layers.Dense(10, activation="relu")(inputs)
# output_layer = keras.layers.Dense(3, activation="softmax")(hidden_layer)
# model = keras.Model(inputs=inputs, outputs=output_layer)

inputs = keras.Input(shape=X_train.shape[1])
hidden_layer1 = keras.layers.Dense(10, activation="relu")(inputs)
hidden_layer2 = keras.layers.Dense(10, activation="relu")(hidden_layer1)
output_layer = keras.layers.Dense(3, activation="softmax")(hidden_layer2)
model = keras.Model(inputs=inputs, outputs=output_layer)

model.summary()
model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
history = model.fit(X_train, y_train, epochs=100)
sns.lineplot(x=history.epoch, y=history.history['loss'])
plt.show()

y_pred = model.predict(X_test)
prediction = pd.DataFrame(y_pred, columns=target.columns)

predicted_species = prediction.idxmax(axis="columns")

from sklearn.metrics import confusion_matrix

true_species = y_test.idxmax(axis="columns")

matrix = confusion_matrix(true_species, predicted_species)
print(matrix)

# Convert to a pandas dataframe
confusion_df = pd.DataFrame(matrix, index=y_test.columns.values, columns=y_test.columns.values)

# Set the names of the x and y axis, this helps with the readability of the heatmap.
confusion_df.index.name = 'True Label'
confusion_df.columns.name = 'Predicted Label'

sns.heatmap(confusion_df, annot=True)
plt.show()
