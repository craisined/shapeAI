# shapeAI

shapeAI is a machine learning tool that generates a large synthetic dataset of basic geometric shapes and leverages this data to train predictive models. The tool enables users to draw shapes (circle, triangle, square, rectangle) on an interactive notepad, and the model classifies the drawing with high accuracy.


**Key Features**

1. Synthetic Data Generation: Automatically creates a scalable library of drawn shapes with controlled noise, rotation, and size variations to ensure robust training.

2. ML-Powered Prediction: Learns from the generated dataset and predicts user-drawn shapes on a notepad interface.

3. High Accuracy: Achieves strong generalization performance across varying drawing styles and distortions.

4. Broad Applications: Can be extended to handwriting recognition, educational tools, HCI (human–computer interaction), or creative AI applications.

**Technical Overview**

1. Data Generation: Able to procedurally draw thousands of synthetic samples of circles, triangles, squares, and rectangles.

2. Preprocessing Normalizes drawings, applies augmentation (translation, rotation, scaling), and encodes inputs into pixel-based or vectorized representations.

3. Training: Models trained on the synthetic dataset with stratified splits and regularization to prevent overfitting.

4. Evaluation: High test accuracy on both synthetic validation sets and live user-drawn inputs.
