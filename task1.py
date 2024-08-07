import pygame
import PIL
import cv2
import moviepy.editor as mp
import pkg_resources
import tkinter as tk

def cek_instalasi():
    # Pygame
    try:
        print("✅ Versi Pygame:", pygame.__version__)
    except AttributeError:
        print("❌ Versi Pygame tidak ditemukan")
    
    # Pillow
    try:
        print("✅ Versi Pillow:", PIL.__version__)
    except AttributeError:
        print("❌ Versi Pillow tidak ditemukan")
    
    # OpenCV
    try:
        print("✅ Versi OpenCV:", cv2.__version__)
    except AttributeError:
        print("❌ Versi OpenCV tidak ditemukan")
    
    # MoviePy
    try:
        versi_moviepy = pkg_resources.get_distribution("moviepy").version
        print("✅ Versi MoviePy:", versi_moviepy)
    except pkg_resources.DistributionNotFound:
        print("❌ MoviePy tidak terinstal")
    
    # Pydub
    try:
        versi_pydub = pkg_resources.get_distribution("pydub").version
        print("✅ Versi Pydub:", versi_pydub)
    except pkg_resources.DistributionNotFound:
        print("❌ Pydub tidak terinstal")
    
    # Tkinter
    try:
        root = tk.Tk()
        root.title("Tes Tkinter")
        root.geometry("200x100")
        label = tk.Label(root, text="Tkinter berfungsi!")
        label.pack()
        root.update()
        print("✅ Tkinter terinstal dan berfungsi!")
        root.destroy()
    except tk.TclError:
        print("❌ Tkinter tidak terinstal atau tidak berfungsi")

if __name__ == "__main__":
    cek_instalasi()
