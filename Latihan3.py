#Latihan 3: Data Loading & Inspection
import pandas as pd

df = pd.read_csv('data_kantin.csv')
print(df.head()) # 5 baris pertama
print(df.info()) # tipe data & jumlah non-null tiap kolom
print(df.describe()) # statistik ringkas kolom numerik
print(df.shape) # jumlah (baris, kolom)

#Tugas Analisis 3: Dari hasil df.info(), kolom mana yang jumlah non-null-nya lebih sedikit dari
#jumlah baris total? Apa artinya?

#--- ANSWER ---
#kolom menu dan terjual dikarenakan menu non null nya adalah 107 sementara terjual adalah 104.