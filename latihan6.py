# latihan 6.py
import pandas as pd

df = pd.read_csv('data_kantin.csv')
laris = df[df['terjual'] > 20 ] # filtering
urut = df.sort_values(by='terjual', ascending=False) # sorting

df['total_pendapatan'] = df['harga'] * df['terjual'] # kolom turunan

ringkasan = df.groupby('menu')['total_pendapatan'].sum() # agregasi
print(ringkasan)

# Tugas Analisis 6: Dari hasil groupby di atas, menu apa yang menghasilkan total_pendapatan
# tertinggi? Bagaimana informasi ini bisa membantu pengambilan keputusan di kantin sekolah?

#--- ANSWER --
# Nasi goreng dengan total : Rp 4.188.000
# dari data ini bisa dijadikan sumber referensi atau pengambilan keputusan untuk perbandingan menu mana yang paling diminati terlepas dari harganya. namun dari total kita juga bisa mengatahui mana yang disukai oleh para siswa dan apakah harga nya terlalu mahal atau siswa tetap mau beli meski mahal. 