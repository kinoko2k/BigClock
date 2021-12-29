import tkinter as tk
import datetime
import time
import threading

class Timer:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root)
        self.label["font"] = ("Helvetica", 104)
        self.label["bg"] = "skyblue"
        self.label["fg"] = "green"
        self.label.grid(column=3, row=10)
        self.root.attributes("-topmost", True)
        self.root.title(u"ClockGUI")

    def changeLabelText(self):
        while True:
            self.label["text"] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            time.sleep(1)


if __name__ == "__main__":
    timer = Timer()
    thread = threading.Thread(target=timer.changeLabelText)
    thread.start()
    timer.root.mainloop()
root.mainloop()
