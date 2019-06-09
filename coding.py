import keras
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
model_img=Sequential()
model_img.add(Conv2D(32,3,4,input_shape=(64,64,3),activation='relu'))
model_img.add(MaxPooling2D(pool_size=(2,2)))
model_img.add(Flatten())

model_img.add(Dense(100,activation='sigmoid'))
model_img.add(Dense(3,activation='softmax'))
model_img.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen=ImageDataGenerator(rescale=1./255)
x_train=train_datagen.flow_from_directory(r"D:\Face detection\training",target_size=(64,64),batch_size=32,class_mode='categorical')
x_test=test_datagen.flow_from_directory(r"D:\Face detection\testing",target_size=(64,64),batch_size=32,class_mode='categorical')
print(x_train.class_indices)
model_img.fit_generator(x_train,samples_per_epoch=320,epochs=100,nb_val_samples=100)
model_img.save("smart security systems using image recoginition.h5")

