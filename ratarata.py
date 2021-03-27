print("Membuat program menghitung rata-rata nilai")

n = int(input("\n Banyaknya Data : "))

print() # membuat baris baru
data = [] # data = ["ayam", "pitik"]

jum = 0 # dimulai dari 0

for i in range(0, n):
    temp = int(input("Masukkan data ke - %d:  "%(i+1)))
    data.append(temp)
    jum +=data[i]
    rata2 = jum/n


print("\nRata-rata = %0.2f"% rata2)
print("Data Sebelum di urutkan", data)
print("Data sesudah diurutkan dari yang terkecil",sorted(data, reverse=False))
print("Data sesudah diurutkan dari yang terbesar", sorted(data, reverse=True))

# del data[3]
data.remove(1)
print("Data Sesudah di Hapus", data)

angka = [2,4,1,3]
angka.sort()
print(angka)

