import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("420x520")
top.resizable(False, False)

# 1 label judul
judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Arial", 16, "bold"))
judul.pack(pady=15)

# Frame untuk 10 input nilai mata pelajaran
frame = tk.Frame(top)
frame.pack(pady=5)

mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika",
         "Kimia", "Biologi", "Ekonomi", "Sosiologi", "Geografi", "Informatika"]