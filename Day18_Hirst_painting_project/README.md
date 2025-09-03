🎨 Hirst Painting Project (Python Turtle)
📌 Project Summary

This project recreates a Hirst-style dot painting using Python’s turtle graphics library.
It extracts colors from an image using the colorgram library and randomly places them on a grid of dots, inspired by the works of Damien Hirst.

🚀 Features

Extracts dominant colors from any image with colorgram.

Uses RGB colors with turtle graphics to draw dots.

Creates a 10 x 10 dot painting with random colors.

Adjustable grid size, dot size, and spacing.

Fast drawing mode with hidden turtle for smooth rendering.

🛠️ Requirements

Make sure you have Python installed.
Then install the dependencies:

pip install colorgram.py

📂 How It Works

Use colorgram.extract("image.jpg", 30) to get colors from an image.

Store RGB values in a color list.

Draw 100 dots (10 rows × 10 columns) on the screen using turtle.

Randomly pick colors from the extracted list to make each dot unique.