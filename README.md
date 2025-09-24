
## 🖼️ Image Resizer with OpenCV

This project is a simple Python-based Image Resizer using the OpenCV library.
It loads an image, resizes it by a specified percentage, and saves the resized output.

---

## 🚀 Features

- Resize images by any percentage (default: 50%)
- Works with any image format supported by OpenCV
- Preserves aspect ratio
- Saves resized image as a new file

---
## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV
  
Install OpenCV by running:

    pip install opencv-python

---
## 📂 Project Structure

ImageResizer/

│-- main.py     # Main program file

│-- krishna.jpg         # Input image (example)

│-- ResizedImage.jpg    # Output resized image

│-- README.md           # Project documentation


---
## ⚙️ Configurable Parameters

Inside the script, you can modify these:

- source = "krishna.jpg"          # Input image file
- destination = "ResizedImage.jpg" # Output image file
- scale_percent = 50              # Resize percentage (e.g., 50 = half size)

## ▶️ How to Run

1.Clone or download this repository.

2.Place your image in the project folder (example: krishna.jpg).

3.Open a terminal in the project folder.

4.Run the script:

    python main.py

5.The resized image will be saved as ResizedImage.jpg.

---
## 💻 Example Output

If the original image size is 800 × 600 and scale_percent = 50:

- New width = 400
- New height = 300
- Saved as ResizedImage.jpg

---
## ✨ Future Improvements

- Allow resizing by specific width/height instead of percentage
- Add GUI with sliders for scaling
- Support batch image resizing

---
## 👩‍💻 Author

Krupali – Image Resizer Project Developer

---
