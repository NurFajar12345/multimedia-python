import pygame
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import threading

pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('example.jpg')

# Memuat suara
sound = pygame.mixer.Sound('example.mp3')
sound.play()

# Menghitung posisi x agar gambar berada di tengah
x = (800 - image.get_width()) // 2  # Menghitung posisi x agar gambar berada di tengah secara horizontal
y = (600 - image.get_height()) // 2 # Menghitung posisi y agar gambar berada di tengah secara vertikal

# Loop utama permainan tanpa animasi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar di posisi tengah
    screen.fill((0, 0, 0))  # Mengisi latar belakang dengan warna hitam
    screen.blit(image, (x, y))  # Menempatkan gambar di tengah

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()

# Fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Music Player")

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter di thread terpisah
def run_tkinter():
    root.mainloop()

tk_thread = threading.Thread(target=run_tkinter)
tk_thread.start()
