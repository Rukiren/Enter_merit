import tkinter as tk
from pynput import keyboard
from threading import Timer
import time

class MeritCounterApp:
    def __init__(self):
        self.merit_count = 0
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.0)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"+{screen_width-150}+20")

        self.label = tk.Label(self.root, text="", font=("Arial", 16), fg="black", bg="white")
        self.label.pack()

        self.fade_timer = None


    def update_label(self):
        self.label.config(text=f" ")
        self.root.attributes("-alpha", 0.8)
        self.root.overrideredirect(True)
        time.sleep(0.02)
        self.reset_fade_timer()
        self.merit_count += 1
        self.label.config(text=f"功德 +1\n累積功德: {self.merit_count}")
        self.root.attributes("-alpha", 0.8)
        self.root.overrideredirect(True)
        self.reset_fade_timer()

    def reset_fade_timer(self):
        if self.fade_timer is not None:
            self.fade_timer.cancel()

        self.fade_timer = Timer(5.0, self.fade_out)
        self.fade_timer.start()

    def fade_out(self):
        self.root.attributes("-alpha", 0.0)

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        self.root.mainloop()

    def on_press(self, key):
        if key == keyboard.Key.enter:
            self.update_label()

app = MeritCounterApp()
app.run()
