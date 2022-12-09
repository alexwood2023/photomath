import io
import os
import PySimpleGUI as sg
from PIL import Image
import keras_ocr
import matplotlib.pyplot as plt








file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
layout = [
    [sg.Image(key="-IMAGE-")],
    [
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ],
]


window = sg.Window("Image Viewer", layout)
filename = None

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            # Actually store the image in memory in binary
            image.save(bio, format="PNG")
            # Use that image data in order to
            window["-IMAGE-"].update(data=bio.getvalue())

window.close()

print("start analysis")
#analisys
print(filename)
#pipeline = keras_ocr.pipeline.Pipeline()
pipeline = keras_ocr.pipeline.Pipeline()
print("setup pipeline")

images = [
    #keras_ocr.tools.read(img) for img in ["Image1.jpg"]
    keras_ocr.tools.read(filename)
]
print("filename worked")
plt.figure(figsize = (10,20))
plt.imshow(images[0])

#plt.figure(figsize = (10,20))
#plt.imshow(images[1])

"""prediction_groups = pipeline.recognize(images)

fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image,
                                    predictions=predictions,
                                    ax=ax)"""
print("finish analysis")