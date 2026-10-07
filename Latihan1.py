# Latihan 1: Operasi Dasar NumPy Array
import numpy as np

harga= np.array([5000, 7000, 3000, 12000, 4500])
print('Rata-rata harga:', harga.mean())
print('Harga tertinggi:', harga.max())
print('Harga setelah diskon10%:', harga * 0.9)
#print('Harga setelah diskon10%:', [5000, 7000, 3000, 12000, 4500] * 0.9)
print('Harga setelah diskon 10%:', np.array([5000, 7000, 3000, 12000, 4500]) * 0.9)

#Tugas Analisis 1: Bandingkan hasil harga * 0.9 di atas dengan jika harga berupa list Python
# biasa (bukan array). Apa yang terjadi bila kamu mencoba [5000,7000,3000] * 0.9? Jelaskan
# mengapa berbeda.

#--- ANSwER ---
# jadi beda karena nanti bakal eror. tapi kalau mau engga eror bisa jalanin pakai perintah ini : print('Harga setelah diskon 10%:', np.array([5000, 7000, 3000, 12000, 4500]) * 0.9) nah. 
# kenapa kalau yang atas engga bisa? karena ini itu list python yang dimana list pyhton engga bisa melakukan operasi desimal. sehingga hanya untuk bilangan bulat. ditambah list python juga hanya menjalan dengan cara di kerjakan satu persatu. tidak seperti numpy yang bisa langsung mengerjakan semuanya.