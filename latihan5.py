#Latihan 5.py
import pandas as pd
df = pd.read_csv('data_kantin.csv')

print(df.duplicated().sum()) # jumlah baris duplikat
df = df.drop_duplicates()
df['harga'] = df['harga'].astype(int) # memastikan tipe data harga adalah integer
print(df.dtypes)

# Tugas Analisis 5: Setelah drop_duplicates(), berapa jumlah baris dataset sekarang dibanding
# sebelumnya? Mengapa penting memastikan tipe data (dtypes) sudah benar sebelum data
# dianalisis lebih lanjut?

#--- ANSWER --
# 6 baris
# untuk mengatahui jenis data sehingga mengurangi kemungkinan error. karena kita jadi tau jika 
# semisal ada jenis data yang berbeda.