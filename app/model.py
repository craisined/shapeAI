from keras import models, layers
import numpy as np

model = models.load_model("model/shape_model.keras")
labels = ["circle ○", "rectangle ▭", "square □", "triangle △"]
def run_model(image):
    img = np.expand_dims(image, axis=0)
    prediction = np.argmax(model.predict(img))
    return labels[prediction]

if __name__=="__main__":
    print(run_model(input("Image path: ")))