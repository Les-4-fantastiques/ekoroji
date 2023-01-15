import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

# Charger le modèle pré-entraîné
model = keras.models.load_model('trained_model.h5')

# Lire l'image à partir du fichier
image = Image.open('image.jpg')

# Convertir l'image en un tableau numpy
image_array = np.array(image)

# Redimensionner l'image pour qu'elle corresponde à l'entrée attendue par le modèle
image_array = np.expand_dims(image_array, axis=0)

# Effectuer la prédiction
predictions = model.predict(image_array)

# Obtenir la classe prédite avec le score le plus élevé
predicted_class = np.argmax(predictions[0])

print("La classe prédite pour cette image est:", predicted_class)