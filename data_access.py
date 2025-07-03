from database import products, users

def tambah_produk(produk):
    products.append(produk)

def ambil_semua_produk():
    return products

def hapus_produk(nama):
    global products
    products = [p for p in products if p["nama"] != nama]
    
def cari_user(username):
    return users.get(username)

