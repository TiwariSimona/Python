Created  a landsacape using python tkinter module

from tkinter import *
root = Tk()
root.minsize(600, 600)
root.maxsize(600, 600)
canvas = Canvas(root, width=600, height=600)
canvas.pack()
canvas.create_rectangle(0, 0, 1000, 600, fill="skyblue") #background
canvas.create_rectangle(50, 350, 250, 580, fill="blue")    #house
canvas.create_rectangle(110, 450, 190, 580, fill="PaleGreen1") #door
canvas.create_polygon(50, 350, 155, 260, 250, 350, fill="deep pink") #chhat
canvas.create_polygon(250, 350, 350, 300, 350, 530, 250, 580, fill="yellow") #sidewall
canvas.create_oval(350, 60, 450, 150, fill="yellow") #sun
canvas.create_polygon(280, 400, 330, 375, 330, 428, 280, 455, fill="saddle brown")   #window
canvas.create_polygon(155, 260, 250, 210, 350, 300, 250, 350, fill="orange") #chhat
canvas.create_rectangle(520, 550, 550, 600, fill="saddle brown")    #treebranch
canvas.create_polygon(480, 550, 533, 500, 590, 550, fill="PaleGreen1")
canvas.create_polygon(480, 500, 533, 450, 590, 500, fill="PaleGreen1")
canvas.create_polygon(480, 450, 533, 400, 590, 450, fill="PaleGreen1")
