import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ----- PARAMETERS -----
IMG_SIZE = 64
NUM_CLASSES = 4  # circle, square, rectangle, triangle

# ----- BUILD THE MODEL -----
def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)),
        MaxPooling2D(2,2),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Flatten(),
        Dense(64, activation='relu'),
        Dense(NUM_CLASSES, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# ----- PREPARE TRAINING DATA -----
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    '/Users/quentingeoffroy/Desktop/shape_notepad/data/train',
    target_size=(IMG_SIZE, IMG_SIZE),
    color_mode='grayscale',
    batch_size=16,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_generator = datagen.flow_from_directory(
    '/Users/quentingeoffroy/Desktop/shape_notepad/data/train',
    target_size=(IMG_SIZE, IMG_SIZE),
    color_mode='grayscale',
    batch_size=16,
    class_mode='categorical',
    subset='validation'
)

# ----- TRAIN THE MODEL -----
model = build_model()
model.summary()

model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)

# ----- SAVE THE MODEL -----
model.save("model/shape_model.h5")
print("✅ Model saved as model/shape_model.h5")
