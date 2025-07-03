# presentation.py
import business_logic

def tampilkan_menu():
    print("\n=== Menu Produk ===")
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Hapus Produk")
    print("4. Keluar")

def halaman_login():
    print("=== SELAMAT DATANG DI APLIKASI PRODUK ===")
    percobaan = 0
    maks_percobaan = 3

    while percobaan < maks_percobaan:
        username = input("Username: ")
        password = input("Password: ")

        status = business_logic.verifikasi_login(username, password)

        if status == "sukses":
            print("\nLogin berhasil! Selamat datang.")
            return True

        elif status == "password_salah":
            print("Password salah.")
        
        elif status == "user_tidak_ditemukan":
            print("Username tidak ditemukan.")
            
        elif status == "kredensial_salah":
            print("Username atau Password salah.")

        elif status == "input_kosong":
            print("Username dan Password tidak boleh kosong.")
        
        percobaan += 1
        print(f"gagal. Sisa percobaan: {maks_percobaan - percobaan}\n")
    
    print("Anda telah gagal login sebanyak 3 kali. Program berhenti.")
    return False

def jalankan_aplikasi():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama produk: ")
            try:
                harga = float(input("Harga produk: "))
                business_logic.buat_produk(nama, harga)
                print("Produk berhasil ditambahkan.")
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == "2":
            produk = business_logic.ambil_produk()
            if not produk:
                print("Belum ada produk.")
            else:
                print("Daftar Produk:")
                for i, p in enumerate(produk, 1):
                    print(f"{i}. {p['nama']} - Rp{p['harga']}")

        elif pilihan == "3":
            nama = input("Masukkan nama produk yang ingin dihapus: ")
            business_logic.hapus_produk(nama)
            print("Produk dihapus (jika ada).")

        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")