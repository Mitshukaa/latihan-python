import json
import datetime

menu = {}
file_path = 'menu.json'

try :
    with open(file_path,'r') as file:
        menu = json.load(file)
        
except Exception as e :
    print(f"Terjadi Kesalahan: {e}")
    

# Menampilkan Menu
print()
print('|===========================================|')
print('|               DAFTAR MENU                 |')
print('|===========================================|')
print(f"|{'  Kode':9}| {'    Menu':15}| {'    Harga ':10}     |")
print('|===========================================|')
for item, info in menu.items():
    print(f"|    {info[  'kode']:4} | {  item:14} | Rp{info['harga']:8}     |")
print('|===========================================|')


#Fungsi untuk mengambil pesanan dari pelanggan
def take_order(menu):
    name = input("Nama Pelanggan : ")
    orders = []
    total_harga = 0
    print("Masukkan kode menu dan porsi (Contoh 3, 2)")
    print('(Pilih nomor 0 untuk selesai')
    while True:
        try:
            order = input("Pesanan: ")
            if order.lower() == '0':
                break
            kode_pesanan, porsi = order.split(", ")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                harga = harga_terpilih * int(porsi)
                total_harga += harga
                orders.append({'item': item_terpilih, 'porsi': int(porsi), 'harga': harga})
            else:
                print("Kode kamu tidak valid.")
        except:
            print('Format input salah')

    print(f"Total harga: Rp{total_harga}")
    while True:
        uang_bayar = int(input("Jumlah uang yang dibayarkan: Rp"))
        if uang_bayar < total_harga:
            print("Uang yang dibayarkan kurang.")
        else:
            break
    kembalian = uang_bayar - total_harga
    print(f"Uang kembalian: Rp{kembalian}")

    # Tambahkan kode transaksi dan tanggal beli
    date = datetime.datetime.now()
    kode_transaksi = f"{date.year}{date.month}{date.day}{date.hour}{date.minute}{date.second}"
    tanggal_beli = f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}"

    return name, orders, total_harga, uang_bayar, kembalian, kode_transaksi, tanggal_beli

# Fungsi Untuk Menyimpan pesaan ke dalam file
def save_order(nama_pelanggan, orders, total_harga, uang_bayar, kembalian, kode_transaksi, tanggal_beli):
    order_details = {
        'Nama Pelanggan' : nama_pelanggan,
        'orders' : orders,
        'total_harga' : total_harga,
        'uang_bayar' : uang_bayar,
        'kembalian' : kembalian,
        'kode_transaksi' : kode_transaksi,
        'tanggal_beli' : tanggal_beli
        
    }
    with open('nota.txt', 'a') as file:
        file.write(json.dumps(order_details) + "\n")
    
# fungsi untuk membaca dan menamilkan pesanan dari file
def read_orders():
    with open('nota.txt', 'r') as file:
        lines = file.readlines()
        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|==========================================|')
        print(f"|Kode Transaksi: {order_details['kode_transaksi']:15}           |")
        print('|==========================================|')
        print(f"|Nama Pelanggan: {order_details['Nama Pelanggan']:15}           |")
        print('|==========================================|')
        print(f"|Tanggal: {order_details['tanggal_beli']:15}               |")
        print('|==========================================|')
        print('|              Detail Pesanan              |')
        print('|==========================================|')
        print(f"|{'      Menu':15}      | {'Porsi':}| {'  Harga  ':8}   |")
        print('|==========================================|')
        for order in order_details['orders']:
            print(f"|     {order[  'item'  ]:15} |{order['porsi']:5} | Rp{order['harga']:7}   | ")
            print('|==========================================|')
        print(f"|Total Harga {'':15}    Rp{order_details['total_harga']:8} |")
        print('|------------------------------------------|')
        print(f"|Uang bayar {'':15}     Rp{order_details['uang_bayar']:8} |")
        print('|------------------------------------------|')
        print(f"|kembalian {'':15}      Rp{order_details['kembalian']:8} |")
        print('|==========================================|')
        print('|               Terima Kasih               |')   
        print('|==========================================|')    
        
# Penggunaan Fungsi
nama_pelanggan, orders, total_harga, uang_bayar, kembalian, kode_transaksi, tanggal_beli = take_order(menu)
save_order(nama_pelanggan, orders, total_harga, uang_bayar, kembalian, kode_transaksi, tanggal_beli)
read_orders()
print()
        