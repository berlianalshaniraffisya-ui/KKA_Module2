#Latihan 4: Menangani Missing Value
import pandas as pd

df = pd.read_csv('data_kantin.csv')
print (df.isnull().sum()) #Jumlah data kosong tiap kolom

df['terjual'] = df['terjual'].fillna(0) # Isi kekosongan dengan 0
df = df.dropna(subset=['menu']) # Menghapus baris jika kolom menu kosong

#Tugas Analisis 4: Mengapa pada contoh di atas kolom terjual diisi (fillna) sedangkan baris
#dengan menu kosong justru dihapus (dropna)? Diskusikan alasan logisnya.

#--- ANSWER --
# karena jika kolom terjual kosong bisa di isi 0 sementara jika menu, 
# kita tidak tahu pembeli membeli menu apa. 
# Sementara jika terjual kita bisa dengan mudah melihat harga dari menu yang ada
