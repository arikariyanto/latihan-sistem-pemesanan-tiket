
import json
import os

FILE_DB = "daftar_film.json"

def load_film():
    if os.path.exists(FILE_DB):
        with open(FILE_DB, "r") as f:
            return json.load(f)
    else:
        return {
            "A001": {"judul": "Avengers: Endgame", "harga": 50000},
            "A002": {"judul": "Spiderman: No Way Home", "harga": 45000},
            "A003": {"judul": "Batman: Dark Knight", "harga": 40000}
        }

# Simpan data film ke file JSON
def simpan_film(data):
    with open(FILE_DB, "w") as f:
        json.dump(data, f, indent=4)

# Variabel utama daftar film
daftar_film = load_film()

def tampilkan_film():
    print("\n=== DAFTAR FILM ===")
    for kode, info in daftar_film.items():
        print(f"{kode} - {info['judul']} (Rp{info['harga']})")

def tambah_film(kode, judul, harga):
    daftar_film[kode] = {"judul": judul, "harga": harga}
    simpan_film(daftar_film)

def hapus_film(kode):
    if kode in daftar_film:
        judul = daftar_film[kode]["judul"]
        del daftar_film[kode]
        simpan_film(daftar_film)
        print(f"🗑️ Film '{judul}' berhasil dihapus.")
    else:
        print("❌ Kode film tidak ditemukan.")
