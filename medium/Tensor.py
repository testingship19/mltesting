#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow import keras


# In[2]:


data= keras.datasets.fashion_mnist


# In[3]:


(train_images, train_labels),(test_images, test_labels) = data.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# In[4]:


train_images = train_images/255.0
test_images = test_images/255.0


# In[6]:


model = keras.Sequential([
              keras.layers.Flatten(input_shape=(28, 28)),
              keras.layers.Dense(128, activation='relu'),
              keras.layers.Dense(10, activation='softmax')])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("tested acc: ", test_acc)


# In[15]:


prediction = model.predict(test_images)
for i in range(5):
  
    plt.imshow(test_images[i],cmap=plt.cm.binary)
    plt.xlabel("Actual : " + class_names[test_labels[i]])
    plt.title("Prediction" + class_names[np.argmax(prediction[i])])
    plt.show()



# In[ ]:




