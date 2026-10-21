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
 
entries = []
for i, nama in enumerate(mapel):
    tk.Label(frame, text=nama, anchor="w", width=18).grid(
        row=i, column=0, padx=5, pady=3, sticky="w")
    e = tk.Entry(frame, width=12, justify="center")
    e.grid(row=i, column=1, padx=5, pady=3)
    entries.append(e)
 
# Fungsi: apapun inputnya, hasil selalu TeknologiInformasi
def hasil_prediksi():
    label_hasil.config(text="Prodi: TeknologiInformasi")
 
# 1 button
tombol = tk.Button(top, text="Hasil Prediksi", command=hasil_prediksi,
                   font=("Arial", 11, "bold"), width=18)
tombol.pack(pady=15)
 
# 1 label luaran hasil prediksi
label_hasil = tk.Label(top, text="", font=("Arial", 13, "bold"), fg="blue")
label_hasil.pack(pady=5)
 
top.mainloop()