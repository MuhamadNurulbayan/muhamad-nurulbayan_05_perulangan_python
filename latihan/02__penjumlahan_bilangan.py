# Input: bilangan bulat positif n
# Proses: menghitung jumlah 1 + 2 + ... + n
# Kondisi berhenti: for selesai pada i = n
# Output: jumlah total

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")
