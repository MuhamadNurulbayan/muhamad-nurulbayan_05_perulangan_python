# Input: bilangan bulat n
# Proses: menampilkan tabel perkalian n dari 1 sampai 10
# Kondisi berhenti: for selesai pada i = 10
# Output: tabel perkalian

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
