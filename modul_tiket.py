import modul_film

riwayat_pemesanan = []

def hitung_diskon(jumlah, total):
    if jumlah >= 5:
        return total * 0.20 
    elif jumlah >= 3:
        return total * 0.10   
    else:
        return 0

def pesan_tiket(kode, jumlah, nama):
    if kode in modul_film.daftar_film:
        harga = modul_film.daftar_film[kode]["harga"]
        total = harga * jumlah

        potongan = hitung_diskon(jumlah, total)
        total_bayar = total - potongan

        data = {
            "nama": nama.title(),
            "film": modul_film.daftar_film[kode]["judul"],
            "jumlah": jumlah,
            "total": total,
            "diskon": potongan,
            "bayar": total_bayar
        }
        riwayat_pemesanan.append(data)

        print(f"\n🎟️ Tiket berhasil dipesan!")
        print(f"Nama: {nama.title()}")
        print(f"Film: {data['film']}")
        print(f"Jumlah Tiket: {jumlah}")
        print(f"Total Harga: Rp{total}")
        print(f"Diskon: Rp{potongan}")
        print(f"Total Bayar: Rp{total_bayar}")
    else:
        print("⚠️ Kode film tidak ditemukan!")

def tampilkan_riwayat():
    print("\n=== RIWAYAT PEMESANAN ===")
    if not riwayat_pemesanan:
        print("Belum ada pemesanan")
    else:
        for r in riwayat_pemesanan:
            print(f"{r['nama']} - {r['film']} - {r['jumlah']} tiket "
                  f"- Rp{r['bayar']} (Diskon Rp{r['diskon']})")