import tkinter as tk
import os
import sys
import pygame
from PIL import Image, ImageTk
import threading

pygame.mixer.init()


def resource_path(relative_path):
    """ Get the absolute path to resource, works for dev and for PyInstaller. """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


image_path = resource_path("shrimp.jpg")
sound_path = resource_path("shrimp.mp3")
bg_sound_path = resource_path("bg.mp3")


def on_yes():
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()
    scale_and_display_image()

    question_label.pack_forget()
    yes_button.pack_forget()
    no_button.pack_forget()


def play_sound():
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)


def on_no():
    pygame.mixer.music.stop()
    show_main_menu()


def scale_and_display_image():
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    img = Image.open(image_path)
    img_ratio = img.width / img.height
    window_ratio = window_width / window_height
    if img_ratio > window_ratio:
        new_width = window_width
        new_height = int(new_width / img_ratio)
    else:
        new_height = window_height
        new_width = int(new_height * img_ratio)
    img = img.resize((new_width, new_height))

    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk
    image_label.pack()


def show_main_menu():
    image_label.pack_forget()
    question_label.pack_forget()
    yes_button.pack_forget()
    no_button.pack_forget()
    main_menu_label.pack()
    play_button.pack()
    exit_button.pack()


def start_shrimp_detector():
    main_menu_label.pack_forget()
    play_button.pack_forget()
    exit_button.pack_forget()

    question_label.pack()
    yes_button.pack()
    no_button.pack()


def exit_program():
    pygame.mixer.music.stop()
    root.quit()


def play_background_music():
    pygame.mixer.music.load(bg_sound_path)
    pygame.mixer.music.play(-1, 0.0)


root = tk.Tk()
root.title("Shrimp Detector")
root.geometry("800x600")

question_label = tk.Label(root, text="Are you a shrimp?", font=("Arial", 16))
yes_button = tk.Button(root, text="Yes", command=on_yes)
no_button = tk.Button(root, text="No", command=on_no)

image_label = tk.Label(root)

main_menu_label = tk.Label(root, text="Welcome to Shrimp Detector!", font=("Arial", 24, "bold"), fg="darkblue")
play_button = tk.Button(root, text="Play Shrimp Detector", command=start_shrimp_detector)
exit_button = tk.Button(root, text="Exit", command=exit_program)

play_background_music()
show_main_menu()
root.mainloop()
