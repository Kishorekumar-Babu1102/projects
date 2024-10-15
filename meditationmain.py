import tkinter as tk
from tkinter import messagebox
import time
import pygame
import pyttsx3

class MeditationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation App")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Welcome to the Meditation App!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Meditation", command=self.start_meditation, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Meditation", command=self.stop_meditation, font=("Helvetica", 14))
        self.stop_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Helvetica", 14))
        self.quit_button.pack(pady=10)

    def start_meditation(self):
        messagebox.showinfo("Meditation", "Starting meditation session...")
        self.play_music()
        self.guided_meditation_script()

    def stop_meditation(self):
        self.stop_music()
        messagebox.showinfo("Meditation", "Meditation session stopped.")

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/meditation_music.mp3")
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def guided_meditation_script(self):
        engine = pyttsx3.init()
        script = [
            "Close your eyes and take a deep breath...",
            "Focus on your breathing. Feel the air entering your lungs...",
            "Let go of any thoughts that come into your mind..."
        ]
        for line in script:
            engine.say(line)
            engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = MeditationApp(root)
    root.mainloop()
