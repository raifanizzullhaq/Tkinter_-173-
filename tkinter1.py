import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("420x520")
top.resizable(False, False)

# 1 label judul
judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Arial", 16, "bold"))
judul.pack(pady=15)