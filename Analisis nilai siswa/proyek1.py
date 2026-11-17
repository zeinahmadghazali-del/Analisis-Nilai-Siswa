siswa_list = [
    {"nama": "Budi", "nilai": [85,90,78]},
    {"nama": "Ani", "nilai": [92,88,95]},
    {"nama": "Citra", "nilai": [70,75,68]}
]

def rata_siswa(nilai_list):
    total = 0
    for i in nilai_list:
        total += i
    return total / len(nilai_list)

def cek_lulus(rata):
    if rata >= 75:
        return "Lulus"
    return "Tidak lulus"
def cari_terbaik(siswa_list):
    nama_terbaik =  "" 
    rata_terbaik = 0
    for s in siswa_list:
        rata = rata_siswa(s["nilai"])
        if rata > rata_terbaik:
            rata_terbaik = rata
            nama_terbaik = s["nama"]
    return nama_terbaik, rata_terbaik

def rata_kelas(siswa_list):
    total = 0
    for s in siswa_list:
        rata = rata_siswa(s["nilai"])
        total += rata
    return total / len(siswa_list)

print("=== Laporan Nilai Siswa ===")
for s in siswa_list:
    rata = rata_siswa(s["nilai"])
    status = cek_lulus(rata)
    print(f"{s['nama']:<8} : {rata:.2f} : {status}")
print("==============================")
print(f"rata-rata kelas: {rata_kelas(siswa_list):.2f}")
nama, skor = cari_terbaik(siswa_list)
print(f"siswa terbaik: {nama} ({skor:.2f})")


