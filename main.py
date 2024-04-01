import mp4
import mp3
from tkinter import *

window = Tk()
window.title("Youtube downloader")
window.config(pady=20, padx=20)

canvas = Canvas(width=444, height=444)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(222, 222, image=logo_img)

canvas.grid(row=0, column=0, columnspan=4)

spacer = Label(text="       ")
spacer.grid(row=1, column=2)

ytm4 = Button(text="Youtube to MP4", command=mp4.Youtube_To_Mp4, pady=10, padx=10)
ytm4.grid(row=2, column=1)

spacer = Label(text="       ")
spacer.grid(row=2, column=2)

ytmp3 = Button(text="Youtube to Mp3", command=mp3.Youtube_To_Mp3, pady=10, padx=10)
ytmp3.grid(row=2, column=3)

window.mainloop()