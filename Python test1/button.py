import tkinter
from time import sleep

window=tkinter.Tk()

window_width=700
window_height=700
window_pos_x=700
window_pos_y=700

window.geometry("{}x{}+{}+{}".format(window_width,window_height,window_pos_x,window_pos_y))

window.resizable(False,False)

window.title("Tkinter: Button Test by Rosmary")

window.iconphoto(False, tkinter.Photolmage(file="icon1.png"))

button1=