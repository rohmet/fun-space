import interface_terminal

if __name__ == "__main__":
    login_berhasil = interface_terminal.halaman_login()

    if login_berhasil:
        interface_terminal.jalankan_aplikasi()
    