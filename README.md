# shapeAI

_Forked from [@quentinbkk's shape ai](https://github.com/quentinbkk/shapeAI)_

Shape AI is a web app utilizing a classifier model to identify user drawn geometric shapes. Currently, the model can identify drawn squares, rectangles, circles, and triangles.

**[Try it live ✏️](https://quentinai.craisin.tech)**

## Running the App 🏃
### Docker 🐋
```bash
git clone https://github.com/craisined/shapeAI
cd shapeAI
docker build -t shapeAI .
docker run -p 3000:3000 shapeAI
```
### Manually 🖥️
```bash
git clone https://github.com/craisined/shapeAI
cd shapeAI
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd app
gunicorn -b 0.0.0.0:3000 app:app
```

## Model Training 💪
OpenCV is used to synthetically generate training data in ```training/generate_shapes.py```.
Data is stored in ```training/data``` - modify the folder to add training cases.
Run ```training/train.py``` to train the model - exports to ```shape_model.keras```.

## Technical Overview 👨‍💻
### Abilities
1. High training accuracy - model consistently trains with accuracy > 99%
2. Fast speed - model has sub 50ms response times
3. Synthetic data and preproccessing - generates training data and sends user drawing from website to language model
### Frameworks
1. Model built with Tensorflow and Keras
2. Image manipulation built using OpenCV and Pillow
3. Backend built using Flask
4. Frontend built using vanilla HTML, CSS, JS
### Changes from original fork
1. Web UI and Flask backend added
2. Synthetic training data altered to produce a more human friendly model
### WIP
1. Low accuracy on certain cases - further improve synthetic shape generation
2. Add confidence for classification - do not display a result if confidence is low
3. Imporve mobile UI to further prevent scroll while drawing
4. Expand dataset to various alphanumerical characters
