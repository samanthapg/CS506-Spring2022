from PIL import Image, ImageDraw
import PySimpleGUI as sg
from PIL import Image 
import os
import tkinter
import io

def image_to_GUI(lake_path, lake_name, park_path, park_name):
    img = Image.open(os.getcwd()+lake_path)
    img.thumbnail((1200, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    img2 = Image.open(os.getcwd()+park_path)
    img2.thumbnail((1200, 800))
    bio2 = io.BytesIO()
    img2.save(bio2, format="PNG")

    #GUI implementation 
    layout = [[[sg.Text(lake_name, font=("Arial, 25")),] ,
    [sg.Image(data=bio.getvalue())],
    [sg.Text(park_name, font=("Arial, 25")),] , 
    [sg.Image(data=bio2.getvalue())]],
    [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Image", layout, size=(1200,800))

    #closing the window conditions 
    while True:
      event, values = window.read()
      if event == " Don't Show Me Anymore" or event == sg.WIN_CLOSED:
        break
      
      window.close()
      #return 
