# business_logic.py
import data_access

def buat_produk(nama, harga):
    if not nama.strip():
        raise ValueError("Nama produk tidak boleh kosong.")
    if harga <= 0:
        raise ValueError("Harga harus lebih dari 0.")
    
    produk = {"nama": nama, "harga": harga}
    data_access.tambah_produk(produk)

def ambil_produk():
    return data_access.ambil_semua_produk()

def hapus_produk(nama):
    data_access.hapus_produk(nama)
    
def verifikasi_login(username, password):
    if not username or not password:
        return "input_kosong"

    stored_password = data_access.cari_user(username)

    if stored_password is None or stored_password != password:
        return "kredensial_salah"

    if stored_password is None:
        return "user_tidak_ditemukan"
    
    if stored_password == password:
        return "sukses"
    else:
        return "password_salah"