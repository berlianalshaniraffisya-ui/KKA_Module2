#Latihan 2: Membuat Series & DataFrame
import pandas as pd
import numpy as np

data_kantin = {
    'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Es Teh', None],
    'harga': [12000, 4000, 10000, 4000, 8000],
    'terjual': [23, 40, None, 35, 18]
}

df = pd.DataFrame(data_kantin)
print('Rata-rata harga:', df['harga'].mean())
print(df)


#Tugas Analisis 2: Amati tabel yang dihasilkan. Kolom mana yang terlihat memiliki data kosong
#(None)? Menurutmu apa risikonya jika data ini langsung dianalisis tanpa dibersihkan?

#--- ANSWER ---
#Maka output yang akan keluar, nilai NaN juga akan muncul. sehingga kurang efektif jika tujuan kita adalah untuk membuat rekap pengeluaran. 
# Juga saatt kita ingin menjalankan numpy untuk rekap penjualan juga bisa error.