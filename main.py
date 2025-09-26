
import modul_film
import modul_tiket
import modul_util

while True:
    print("\n=== MENU BIOSKOP ===")
    print("1. Lihat Daftar Film")
    print("2. Tambah Film Baru")
    print("3. Hapus Film")    
    print("4. Pesan Tiket")
    print("5. Riwayat Pemesanan")
    print("6. Urutkan Harga Film (Bubble Sort)")
    print("7. Cari Film (Linear Search)")
    print("8. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        modul_film.tampilkan_film()

    elif pilihan == "2":
        kode = input("Masukkan kode film: ")
        judul = input("Masukkan judul film: ")
        harga = int(input("Masukkan harga tiket: "))
        modul_film.tambah_film(kode, judul, harga)
        print("✅ Film berhasil ditambahkan!")

    elif pilihan == "3":
        kode = input("Masukkan kode film yang ingin dihapus: ")
        modul_film.hapus_film(kode)

    elif pilihan == "4":
        modul_film.tampilkan_film()
        kode = input("Masukkan kode film: ")
        jumlah = int(input("Jumlah tiket: "))
        nama = input("Nama pemesan: ")
        modul_tiket.pesan_tiket(kode, jumlah, nama)

    elif pilihan == "5":
        modul_tiket.tampilkan_riwayat()

    elif pilihan == "6":
        harga_list = [f["harga"] for f in modul_film.daftar_film.values()]
        print("Sebelum sorting:", harga_list)
        sorted_list = modul_util.bubble_sort(harga_list)
        print("Setelah sorting:", sorted_list)

    elif pilihan == "7":
        target = input("Masukkan kode film yang dicari: ")
        semua_kode = list(modul_film.daftar_film.keys())  
        idx = modul_util.linear_search(semua_kode, target)
        if idx != -1:
            kode = semua_kode[idx]
            film = modul_film.daftar_film[kode]
            print(f"✅ Film ditemukan! {kode} - {film['judul']} (Rp{film['harga']})")
        else:
            print("⚠️ Kode film tidak ditemukan!")


    elif pilihan == "8":
        print("Terima kasih, keluar dari sistem!")
        break

    else:
        print("⚠️ Pilihan tidak valid, coba lagi.")
