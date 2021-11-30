print("Rental Warnet Connect\n")
penyewa = input("Masukkan nama penyewa: ")
#print ("Nama Penyewa :", penyewa) 

print("\n~~~~Jenis Pemakaian~~~~")
print("1. Internet (Rp 4000/jam) ")
internet=int(input("Berapa menit : "))
print("2. Mengetik (Rp 2000/jam) ")
mengetik=int(input("Berapa menit : "))
print("3. Game Online (Rp 5000/jam) ")
game_online=int(input("Berapa menit : "))
print("\n~~~~Fasilitas Lain~~~~")
print("1. Scan (Rp 1000/file) ")
scan=int(input("Berapa file : "))
print("2. Print Warna (Rp 500/lembar) ")
printwarna=int(input("Berapa lembar : "))
print("3. Print Hitam Putih (Rp 300/lembar) ")
printhitamputih=int(input("Berapa lembar : "))
print("\n~~~~Fasilitas Minuman~~~~")
print("1. Teh Botol (Rp 3000/botol) ")
tehbotol=int(input("Berapa botol : "))

if internet < 31 and internet > 0:
  biaya_internet = (30/60)*4000
elif internet > 30:
  biaya_internet = (internet/60)*4000
elif internet == 0:
  biaya_internet = 0
  
if mengetik < 31 and mengetik > 0:
  biaya_mengetik = (30/60)*2000
elif mengetik > 30:
  biaya_mengetik = (mengetik/60)*2000
elif mengetik == 0:
  biaya_mengetik = 0
  
if game_online < 31 and game_online > 0:
  biaya_game_online = (30/60)*5000
elif game_online > 30:
  biaya_game_online = (game_online/60)*5000
elif game_online == 0:
  biaya_game_online = 0

biaya_scan=scan*1000
biaya_print_warna=printwarna*500
biaya_print_hitam_putih=printhitamputih*300
biaya_teh_botol=tehbotol*3000

TotalPembayaran=(biaya_internet+biaya_mengetik+biaya_game_online+biaya_scan
                 +biaya_print_warna+biaya_print_hitam_putih+biaya_teh_botol)
print("\n--------------------Rincian Biaya--------------------")
print("\n- Biaya rental komputer")
print("  Internet",": Rp.",biaya_internet)
print("  Mengetik",": Rp.",biaya_mengetik)
print("  Game Online",": Rp.",biaya_game_online)
print("\n- Biaya scan: Rp.",biaya_scan)
print("\n- Biaya print")
print("  Warna",": Rp.",biaya_print_warna)
print("  Hitam-putih",": Rp.",biaya_print_hitam_putih)
print("\n- Teh botol: Rp.",biaya_teh_botol)
print("\nTotal Biaya yang harus dibayarkan",penyewa,"= Rp.",TotalPembayaran)
input()
   

