import time
import os
import argparse
import sys
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          FUNGSI-FUNGSI PRIMITIF
# fungsi pengganti .index()
def find_index(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1
# fungsi pengganti .pop()
def remove_element(lst,index):
    lst = lst[:index] + lst[index+1:]
    return lst
# fungsi agar output muncul huruf per huruf
def delay_print(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()
# fungsi Membuang ";" (fungsi pengganti .split())
def splitter(a):
    list = []
    temp = ''
    j = 0
    for i in a:
        for j in i:
            if j == ';':
                list.append(temp)
                temp = ''
            else:
                temp += j
        if temp.endswith('\n'):
            temp = temp[:-1]
        list.append(temp)
        temp = ''
    return list
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          Random Number Generator
def lcg_rng(seed, batasbawah, batasatas, a=6364136223846793005, c=1442695040888963407, m=2**64):
    seed = (a * seed + c) % m
    scaled_random_number = batasbawah + int((batasatas - batasbawah) * (seed / (m - 1)))  # Menghasilkan nilai antara batas atas dan batas bawah
    return scaled_random_number, seed
#Memanggil random number
def callingnum(batasbawah,batasatas):
    current_time = int(time.time())  # Ambil waktu sistem saat ini
    random_number, current_time = lcg_rng(current_time, batasbawah, batasatas)  # Gunakan waktu sistem sebagai seed
    return random_number
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          LOAD
def load(folder_name):
    monsterdict = {}
    userdict = {}
    item_inventorydict = {}
    item_shopdict = {}
    monster_inventorydict = {}
    monster_shopdict ={}
    # Mengecek apakah folder ada
    if not os.path.exists(folder_name):
        print(f"Folder '{folder_name}' tidak ditemukan.")
        return False
    time.sleep(0.5)
    print("\nLoading...")
    time.sleep(0.5)
    # Proses load data dari file CSV di dalam folder
    for file_name in os.listdir(folder_name):
        if file_name.endswith('.csv'):
            delay_print(f"Loading data dari file: {file_name}")
            with open(os.path.join(folder_name, file_name), 'r') as file:
                if file_name == "monster.csv":
                    monsterdict = csv_to_dict("monster.csv",folder_name)
                if file_name == "user.csv":
                    userdict = csv_to_dict("user.csv",folder_name)
                if file_name == "monster_shop.csv":
                    monster_shopdict = csv_to_dict("monster_shop.csv",folder_name)
                if file_name == "monster_inventory.csv":
                    monster_inventorydict = csv_to_dict("monster_inventory.csv",folder_name)
                if file_name == "item_shop.csv":
                    item_shopdict = csv_to_dict("item_shop.csv",folder_name)
                if file_name == "item_inventory.csv":
                    item_inventorydict = csv_to_dict("item_inventory.csv",folder_name)
                pass
    
    print("\nLoad selesai.")
    return True,monsterdict,userdict,monster_shopdict,monster_inventorydict,item_shopdict,item_inventorydict
    #dilanjutkan dengan memanggil fungsi register,login,dll untuk melanjutkan permainan
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          CONVERT CSV KE DICTIONARY
# Mengubah data csv menjadi dictionary yang siap pakai
def csv_to_dict(datacsv,folder_name):
    data = open(os.path.join(folder_name, datacsv), 'r')
    arraydata = []
    for i in data:
        arraydata.append(i)
    splitted_data = splitter(arraydata)
    if datacsv == "monster.csv" or datacsv == "user.csv": #Jika data csv headernya 5 (monster.csv dan user.csv)
        keys = splitted_data[:5]
        values = [splitted_data[i:i+5] for i in range(5, len(splitted_data), 5)]

        # Mengonversi menjadi dictionary
        result = {}
        for key in keys:
            index = find_index(keys, key)
            result[key] = [value[index] for value in values]
    else:                                               #Jika data csv headernya 3 (selain monster.csv dan user.csv)
        keys = splitted_data[:3]
        values = [splitted_data[i:i+3] for i in range(3, len(splitted_data), 3)]

        # Mengonversi menjadi dictionary
        result = {}
        for key in keys:
            index = find_index(keys, key)
            result[key] = [value[index] for value in values]
    return result
while True:
    parser = argparse.ArgumentParser(description='Load data dari folder CSV')
    parser.add_argument('folder_name', type=str, help='Nama folder yang berisi file CSV')

    # Parsing argumen
    args = parser.parse_args()

    # Memanggil fungsi load dengan nama folder yang diberikan
    success,monsterdict,userdict,monster_shopdict,monster_inventorydict,item_shopdict,item_inventorydict = load(args.folder_name)
    # Mengecek apakah folder ada. jika ada, maka request untuk memasukkan nama folder akan berhenti dan melanjutkan permainan
    if success:
        #diikuti dengan fungsi2 lainnya
        break
    else:
        pass # Akan terus looping hingga nama folder yang dimasukkan 
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               GAMBAR-GAMBAR MONSTER
default_monster = '''
                                    ,
                                   |`|
                                  /'_/_
                                ,'_/\_/\_                       ,
                              ,'_/}'_\_,/_                    ,'|
                            ,'_/\_'_ \_ \_/                _,-'_/
                          ,'_/'\_'_ \_ }'_,\           _,-'_,-/ \,
                        ,' /_\ _'_ \_ }'_,/       __,-'<_,' _,\_,/
                       ( (' )\/(_ \_ }'_,\   __--' _,-_/_,-',_/ _|
                        \_`\> 6` 7  }'_,/ ,-' _,-,'\,_'_ \,_/'_,|
                          \/-  _/ 7 '/ _,' _/'\_  \,_'_ \_ |'_,/
                           \_'/>   7'_/' _/' \_ '\,_'_ \_ |'_,|
                             >/  _ ,V  ,<  \__ '\,_'_ \_ |'_,/
                           /'_  ( )_)\/-,',__ '\,_'_,\_,|'_|
                          ( ) \_ \|_  `\_    \_,/'\,_'_,/'
                           ||_  \_\_)    `\_
                            \_)   >        `\_
                                 /  `,      |`\_
                                /    \     / \ `|
                               /   __/|   /  /  `))
                              (`  (   (` (_  \   /
                              /  ,/    |  /  /   )
                             / ,/      | /   \   `\_
                           _/_/        |/    /__/,_/     
                          /_(         /_(

'''
Captain_Rex = '''
                                               ____
   ___                                      .-~. /_"-._
 `-._~-.                                  / /_ "~o\  :Y
       \  \                                / : \~x.  ` ')
       ]  Y                              /  |  Y< ~-.__j
      /   !                        _.--~T : l  l<  /.-~
     /   /                 ____.--~ .   ` l /~\ \<|Y
    /   /             .-~~"        /| .    ',-~\ \L|
   /   /             /     .^   \ Y~Y \.^>/l_   "--'
  /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
 Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
 |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
 |      ~---~           /   ~~"---\_  ' __[>
 l  .                _.^   ___     _>-y~
  \  \     .      .-~   .-~   ~>--"  /
   \  ~---"            /     ./  _.-'
    "-.,_____.,_  _.--~\     _.-~
                ~~     (   _}       
                       `. ~(
                         )  |
                   /,`--'~\--'~|
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Rakdaf = '''
            c,_.--.,y
             7  a.a(
            (    ,_Y)
            :   '---;
        ___.'\.  - (
      .'"""S,._'--'_2..,_
      |    ':::::=:::::  |
      .     f== ;-,---.' T
       Y.   r,-,_/_      |
       |:\___.---' '---./
       |'`             )
        \             ,
        ':;,.________.;L
        /  '---------' |
        |              |
        L---'-,--.-'--,-'
         T    /   \   Y
         |   Y    ,   |
         |   \    (   |
         (   )     \,_L
         7-./      )  `,
        /  _(      '._  |
      '---'           '--'
'''
Tomo = '''
                          .       .
                         / `.   .' |
                 .---.  <    > <    >  .---.
                 |    \  \ - ~ ~ - /  /    |
                  ~-..-~             ~-..-~
              \~~~\.'                    `./~~~/
    .-~~^-.    \__/                        \__/
  .'  O    \     /               /       \  |
 (_____,    `._.'               |         }  \/~~~/
  `----.          /       }     |        /    \__/
        `-.      |       /      |       /      `. ,~~|
            ~-.__|      /_ - ~ ^|      /- _      `..-'   f: f:
                 |     /        |     /     ~-.     `-. _||_||_
                 |_____|        |_____|
'''
Viki = '''
                         . - ~ ~ ~ - .
       ..     _      .-~               ~-.
      //|     \ `..~                      `.
     || |      }  }              /       \  |
 (\   || \~^..'                 |         }  |
  \`.-~  o      /       }       |        /    |
  (__          |       /        |       /      `.
   `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
               |     /          |     /     ~-.     ~- _
               |_____|          |_____|         ~ - . _ _~_-_
'''
Anky = '''
                      /~~~~~~~~~~~~\_
  _+=+_             _[~  /~~~~~~~~~~~~\_
 {""|""}         [~~~    [~   /~~~~~~~~~\_
  """:-'~[~[~"~[~  ((++     [~  _/~~~~~~~~\_
       '=_   [    ,==, ((++    [    /~~~~~~~\-~~~-.
          ~-_ _=+-(   )/   ((++  .~~~.[~~~~(  {@} \`.
                  /   }\ /     (     }     (   .   ''}
                 (  .+   \ /  //     )    / .,  """"/
                 ||  \     \ (   .+~~\_  /.= /'""""
                 <"_V_">      ||  \    ~~~~~~||  |
                               ||  \          ||  |
                               <"_V_">        <"_V_">
'''
The_Little_Ping = '''
                            <\              _
                             ||           _/{
                      _       ||      _-   -_
                    /{        / `\   _-     - -_
                  _~  =      ( @  \ -        -  -_
                _- -   ~-_   \( =\ \           -  -_
              _~  -       ~_ | 1 :\ \      _-~-_ -  -_
            _-   -          ~  |V: \ \  _-~     ~-_-  -_
         _-~   -            /  | :  \ \            ~-_- -_
      _-~    -   _.._      {   | : _-``               ~- _-_
   _-~   -__..--~    ~-_  {   : \:}
 =~__.--~~              ~-_\  :  /
                            \ : /__
                           //`Y'--||      =
                          <+       ||
                           ||      WWW
                           MMM

'''
Sepuh_Raihan = '''
         __.,,------.._
      ,'"   _      _   "`.
     /.__, ._  -=- _"`    Y
    (.____.-.`      ""`   j
     VvvvvvV`.Y,.    _.,-'       ,     ,     ,
         Y    ||,   '"\         ,/    ,/    ./
         |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,
    ..  ,;,,',-'"\,'  ,  .     '     ' ""' '--,/    .. ..
  ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..
 ff||`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..
 l` \` `.`."`-..,-' j  /./ /, , / , / /l \   \=\l   || `' || ||...
  `  `   `-._ `-.,-/ ,' /`"/-/-/-/-/-/-/-`.`.  `'.\--`'--..`'_`' || 
             "`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,
           ,-"'' _.,-'    l_,-'_,,'          "`-._ . "`. /|     `.'\ ,       |
         ,',.,-'"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j
         |||               `._ )-."`.     /|         `.| |        `.`-||-||/
         |` \`                 "`._   "`--' j          j' j          `-`---'
          `  `                     "`_,-','/       ,-'"  /
                                  ,'",__,-'       /,, ,-'
                                  Vvv'            VVv'
'''
vs = '''

░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░ ░▒▓██████▓▒░  
  ░▒▓█▓▓█▓▒░        ░▒▓█▓▒░ 
  ░▒▓█▓▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓██▓▒░  ░▒▓███████▓▒░  
                                           

'''
gambarmonster = [Captain_Rex,Rakdaf,Tomo,Viki,Anky,The_Little_Ping,Sepuh_Raihan]
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               INVENTORY
def inventory(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    index_array_fileuser = find_index(arrayusername, userdatabase[1])
    owca_coin = arrayuseroc[index_array_fileuser]
    user_id = arrayuserid[index_array_fileuser]
    # array harus berjumlah sama
    arrayidmonsterbaru = []
    arraylevelmonsterbaru = []
    arraytypemonsterbaru = []
    arrayhpmonsterbaru = []
    arraypotiontypebaru = []
    arraypotionqtybaru = []
    arrayatkpowerbaru = []
    arraydefpowerbaru = []
    for i in range(len(arrayuseridMinv)):
        if arrayuseridMinv[i] == user_id:
            arrayidmonsterbaru.append(arrayidmonsterMinv[i])
            arraylevelmonsterbaru.append(arraymonsterlevel[i])
    for i in arrayidmonsterbaru:
        if i in arrayidmonster:
            arraytypemonsterbaru.append(arraytypemonster[int(i)-1])
            arrayhpmonsterbaru.append(arrayhpmonster[int(i)-1])
    for i in range(len(arrayuseridIinv)):
        if arrayuseridIinv[i] == user_id:
            arraypotionqtybaru.append(arrayqtyIinv[i])
            arraypotiontypebaru.append(arraytypeIinv[i])
    for i in arraytypemonsterbaru:
        if i in arraytypemonster:
            index_array_typemonster = find_index(arraytypemonster, i)
            arrayatkpowerbaru.append(arrayatkpower[index_array_typemonster])
            arraydefpowerbaru.append(arraydefpower[index_array_typemonster])
    print(f"============ INVENTORY LIST (User ID: {user_id}) ============")
    print(f"jumlah O.W.C.A coin mu sekarang adalah {owca_coin}")
    count = 0
    count2 = 0
    for i in range(len(arrayidmonsterbaru)):
        print(f"{i+1}. Monster (Name : {arraytypemonsterbaru[i]}, Lvl : {arraylevelmonsterbaru[i]}, HP : {arrayhpmonsterbaru[i]})")
        count += 1
    for i in range(count, (len(arraypotionqtybaru)+count)-1):
        print(f"{i+1}. Potion (Type : {arraypotiontypebaru[count2]}, Qty : {arraypotionqtybaru[count2]})")
        count2 += 1
        count += 1
    print("Ketik id untuk menampilkan detail item !(atau ketik 'exit' untuk keluar dari inventory)")
    detailorstop = input(">>>>>  ")
    while detailorstop != "exit":
        if detailorstop >= "0" and detailorstop <= "9":
            itemid = int(detailorstop) - 1
            if itemid < len(arrayidmonsterbaru):
            # Menampilkan detail monster
                print("Monster")
                print(f"Name      : {arraytypemonsterbaru[itemid]}")
                print(f"ATK Power : {arrayatkpowerbaru[itemid]}") 
                print(f"DEF Power : {arraydefpowerbaru[itemid]}") 
                print(f"HP        : {arrayhpmonsterbaru[itemid]}")
                print(f"Level     : {arraylevelmonsterbaru[itemid]}")
            elif itemid < len(arrayidmonsterbaru) + len(arraypotionqtybaru):
                idx = itemid - len(arrayidmonsterbaru)
                print("Potion")
                print(f"Type      : {arraypotiontypebaru[idx]}")
                print(f"Qty       : {arraypotionqtybaru[idx]}")
            else:
                print("Item tidak ditemukan.")
        else:
            print("Perintah tidak valid, masukkan perintah yang valid")

        detailorstop = input(">>>>> ")
    print("Keluar dari inventory........")
    time.sleep(1)
    print("Anda telah keluar dari inventory")
    return arrayidmonsterbaru,arraylevelmonsterbaru,arraytypemonsterbaru,arrayhpmonsterbaru,arraypotiontypebaru,arraypotionqtybaru,arrayatkpowerbaru,arraydefpowerbaru
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               LABORATORY
def laboratory(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    print("============== LABORATORY ==============")
    print("\nSelamat datang di Lab Dokter Asep !!! ")
    arraylabmonsterid = []
    arraylabmonsterlevel = []
    arraylabmonstertype = []
    for i in range(len(arrayuseridMinv)):
        if userdatabase[0] == arrayuseridMinv[i]:
            monsteriduser = arrayidmonsterMinv[i]
            monster_index = int(monsteriduser) - 1
            arraylabmonstertype.append(arraytypemonster[monster_index])
            arraylabmonsterid.append(arrayidmonsterMinv[i])
            arraylabmonsterlevel.append(arraymonsterlevel[i])
    for i in range(len(arraylabmonsterid)):
      print(f"{i+1}. {arraylabmonstertype[i]} (level : {arraylabmonsterlevel[i]})")
    time.sleep(2)
    print("\n============= UPGRADE PRICE ============= \n1. Level 1 -> Level 2: 300 OC \n2. Level 2 -> Level 3: 500 OC \n3. Level 3 -> Level 4: 800 OC \n4. Level 4 -> Level 5: 1000 OC")
    while True:
        monster_option = input("Pilih Monster atau 'exit' untuk keluar : ")
        while not isDigitorExit(monster_option):
            print("Input tidak valid, coba lagi! ")
            monster_option = input("Pilih Monster atau 'exit' untuk keluar : ")
        if monster_option == "exit":
            break
        indexmonsteroption = int(monster_option) - 1
        if indexmonsteroption >= len(arraylabmonsterid):
            print("Input melebihi indeks pada pilihan, coba lagi! ")
            continue
        if arraylabmonsterlevel[indexmonsteroption] == "5":
            print("Maaf, monster yang anda pilih sudah mencapai level maksimum.")
        else:
            if arraylabmonsterlevel[indexmonsteroption] == "1":
                harga = 300
            elif arraylabmonsterlevel[indexmonsteroption] == "2":
                harga = 500
            elif arraylabmonsterlevel[indexmonsteroption] == "3":
                harga = 800
            elif arraylabmonsterlevel[indexmonsteroption] == "4":
                harga = 1000
            biaya = int(userdatabase[4]) - harga
            while biaya < 0:
                print("Jumlah OC anda tidak cukup untuk mengupgrade level! ")
                monster_option = input("Pilih Monster atau 'exit' untuk keluar : ")
                while not isDigitorExit(monster_option):
                    print("Input tidak valid, coba lagi! ")
                    monster_option = input("Pilih Monster atau 'exit' untuk keluar : ")
                if monster_option == 'exit':
                    break
                indexmonsteroption = int(monster_option) - 1
            print(f"{arraylabmonstertype[indexmonsteroption]} akan di-upgrade ke level {int(arraylabmonsterlevel[indexmonsteroption])+1}")
            upgradevalid = input(">>>> Lanjutkan upgrade? (Y/N) :")
            if upgradevalid.lower() == "y":
                arraylabmonsterlevel[indexmonsteroption] = str(int(arraylabmonsterlevel[indexmonsteroption])+1)
                userdatabase[4] = str(biaya)
                i = 0
                for i in range(len(arrayuseridMinv)):
                    if userdatabase[0] == arrayuseridMinv[i] and arraylabmonsterid[indexmonsteroption] == arrayidmonsterMinv[i]:
                        arraymonsterlevel[i] = str(int(arraymonsterlevel[i]) + 1)
                time.sleep(1)
                print(f"\nSelamat {arraylabmonstertype[indexmonsteroption]} berhasil di-upgrade ke level {int(arraylabmonsterlevel[indexmonsteroption])}!")
                for i in range(len(arraylabmonsterid)):
                    print(f"{i+1}. {arraylabmonstertype[i]} (level : {arraylabmonsterlevel[i]})")
            else:
                print(f"{arraylabmonstertype[indexmonsteroption]} tidak jadi di-upgrade ke level {int(arraylabmonsterlevel[indexmonsteroption])+1}")
    for i in range(len(arrayuserid)):
        if userdatabase[0] == arrayuserid[i]:
            arrayuseroc[i] = userdatabase[4]
    return arraymonsterlevel,arrayuseroc
# Fungsi mengecek apakah input merupakan string bilangan atau 'exit'    
def isDigitorExit(monster_option):
    if monster_option.lower() == "exit":
        return True
    for char in monster_option:
        if char < '0' or char > '9':
            return False
    return True
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               SHOP AND CURRENCY
def shop_currency(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    potiontype = ['strength','resilience','healing']
    potionid = ['1','2','3']
    potionidshop = ['1','2']
    delay_print("============== SHOP ==============")
    time.sleep(0.5)
    delay_print("\nIrasshaimase! Selamat datang di SHOP!!")
    time.sleep(1)
    arraymonsteridyangadadiakunuser = [] #array baru untuk menampung monster2 yang dimiliki user dari monster inventory
    for i in range(len(arrayuseridMinv)):
        if userdatabase[0] == arrayuseridMinv[i]:
            arraymonsteridyangadadiakunuser.append(arrayidmonsterMinv[i])
    arrayidmonstershopbaru = arrayidmonstershop
    arrayshopmosntertypebaru = []
    arrayshopapbaru = []
    arrayshopdpbaru = []
    arrayshophpbaru = []
    arraymonsterstockbaru = arraymonsterstock
    arraymonsterpricebaru = arraymonsterprice
    # Mengecek sekalian menambah elemen pada array kosong yang dikhususkan untuk ditampilkan shop karena pada data csv hanya ada id,stock sama price
    for i in (arrayidmonstershop):
        if i in arrayidmonster:
            arrayshopmosntertypebaru.append(arraytypemonster[int(i)-1])
            arrayshopapbaru.append(arrayatkpower[int(i)-1])
            arrayshopdpbaru.append(arraydefpower[int(i)-1])
            arrayshophpbaru.append(arrayhpmonster[int(i)-1])
    potionidshopbaru = potionidshop
    arraypotiontypebaru = []
    arraypotionstockbaru = arraypotionstock
    arraypotionpricebaru = arraypotionprice
    for i in (potionidshop):
        if i in potionid:
            arraypotiontypebaru.append(arraypotiontype[int(i)-1])
    while True:
        action = input("\n>>> Pilih aksi (lihat/beli/keluar): ")
        if action == "lihat":
            view_option = input("\n>>> Mau lihat apa? (monster/potion): ")
            if view_option == "monster":
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                time.sleep(1)
            elif view_option == "potion":
                time.sleep(1)
                print(" ID |      Type      | Stok  | Harga")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                time.sleep(1)
        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang adalah {userdatabase[4]}")
            buy_option = input(">>> Mau beli apa? (monster/potion): ")
            if buy_option == "monster":
                buymonsterid = input(">>> Masukkan id monster : ")
                while isMonsIdExist(buymonsterid,arrayidmonstershop) == False:
                    print("Monster dengan id tersebut tidak ada di shop")
                    buymonsterid = input(">>> Masukkan id monster : ")
                indexidmonster = find_index(arrayidmonstershop,buymonsterid)
                if int(arraymonsterprice[indexidmonster]) <= int(userdatabase[4]) and isMonsIdExist(buymonsterid,arraymonsteridyangadadiakunuser) == False: #Jika  oc cukup (userdatabase[4]=oc yg dimiliki user) dan user belum punya monster tersebut, maka update array2 dengan monster yang baru dibeli
                    userdatabase[4] = str(int(userdatabase[4]) - int(arraymonsterprice[indexidmonster]))
                    arrayuseridMinv.append(userdatabase[0])
                    arrayidmonsterMinv.append(buymonsterid)
                    arraymonsterlevel.append("1")
                    arraymonsterstock[indexidmonster] = str(int(arraymonsterstock[indexidmonster]) - 1)
                    delay_print(f"Berhasil membeli item : Monster {arrayshopmosntertypebaru[indexidmonster]} berhasil masuk ke inventory-mu")
                elif isMonsIdExist(buymonsterid,arraymonsteridyangadadiakunuser) == True: # jika user sudah punya monsternya
                    delay_print(f"Monster {arrayshopmosntertypebaru[indexidmonster]} sudah ada di inventory-mu")
                elif arraymonsterstock[indexidmonster] == "0": #Jika monster sudah habis di shop
                    delay_print(f"Monster {arrayshopmosntertypebaru[indexidmonster]} sudah habis")
                elif int(arraymonsterprice[indexidmonster]) >= int(userdatabase[4]): #Jika harga monster melebihi oc user
                    delay_print(f"Jumlah O.W.C.A. Coin-mu tidak cukup untuk membeli monster {arrayshopmosntertypebaru[indexidmonster]}")
            elif buy_option == "potion":
                buypotionid = input(">>> Masukkan id potion : ")
                jumlah = input(">>> Masukkan jumlah potion : ")
                while isMonsIdExist(buypotionid,potionidshop) == False:
                    print("Potion tersebut tidak ada di shop")
                    buypotionid = input(">>> Masukkan id potion : ")
                    jumlah = input(">>> Masukkan jumlah potion : ")
                indexidpotion = find_index(potionidshop,buypotionid)
                arrayptypeygdipunyauser = []
                for i in range(len(arrayuseridIinv)):
                    if userdatabase[0] == arrayuseridIinv[i]:
                        arrayptypeygdipunyauser.append(arraytypeIinv[i])
                if int(arraypotionprice[indexidpotion])*int(jumlah) <= int(userdatabase[4]) and potiontype[indexidpotion] in arrayptypeygdipunyauser:
                    userdatabase[4] = str(int(userdatabase[4]) - (int(arraypotionprice[indexidpotion])*int(jumlah)))
                    for i in range(len(arraytypeIinv)):
                        if userdatabase[0] == arrayuseridIinv[i] and arraytypeIinv[i] == potiontype[indexidpotion]:
                            arrayqtyIinv[i] = str(int(arrayqtyIinv[i]) + int(jumlah))
                    arraypotionstock[indexidpotion] = str(int(arraypotionstock[indexidpotion]) - int(jumlah))
                    delay_print(f"Berhasil membeli item : {potiontype[indexidpotion]} potion berhasil masuk ke inventory-mu")                    
                elif int(arraypotionprice[indexidpotion])*int(jumlah) <= int(userdatabase[4]) and potiontype[indexidpotion] not in arrayptypeygdipunyauser:
                    userdatabase[4] = str(int(userdatabase[4]) - (int(arraypotionprice[indexidpotion])*int(jumlah)))
                    arrayuseridIinv.append(userdatabase[0])
                    arraytypeIinv.append(potiontype[indexidpotion])
                    arrayqtyIinv.append(str(jumlah))
                    arraypotionstock[indexidpotion] = str(int(arraypotionstock[indexidpotion]) - int(jumlah))
                    delay_print(f"Berhasil membeli item : {potiontype[indexidpotion]} potion berhasil masuk ke inventory-mu")
                elif int(arraypotionprice[indexidpotion])*int(jumlah) >= int(userdatabase[4]):
                    delay_print(f"Jumlah O.W.C.A. Coin-mu tidak cukup untuk membeli {potiontype[indexidpotion]} potion")
        elif action == "keluar":
            delay_print("BosR4iii bilang makasih, belanja lagi ya nanti >_<")
            break
        else:
            delay_print("Perintahmu tidak sesuai, coba ulangi perintah! ")
            False
    for i in range(len(arrayuserid)):
        if userdatabase[0] == arrayuserid[i]:
            arrayuseroc[i] = userdatabase[4]            
    return userdatabase,arrayuseridMinv,arrayidmonsterMinv,arraymonsterlevel,arrayuseridIinv,arraytypeIinv,arrayqtyIinv,arraymonsterstock,arraypotionstock,arrayuseroc
#Fungsi mengecek id monster/potion apakah ada
def isMonsIdExist(id,lst):
    for i in range(len(lst)):
        if id == lst[i]:
            return True
    return False
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               SHOP MANAGEMENT
def shop_management(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    # DATABASE POTION
    potiontype = ['strength','resilience','healing']
    potionid = ['1','2','3']
    potionidshop = ['1','2']
    print(">>>  SHOP ")
    time.sleep(0.5)
    delay_print("============== SHOP MANAGEMENT ==============")
    delay_print(f"\nIrasshaimase! Selamat datang kembali, {userdatabase[1]}! ")
    time.sleep(1)
    arrayidmonstershopbaru = arrayidmonstershop
    arrayshopmosntertypebaru = []
    arrayshopapbaru = []
    arrayshopdpbaru = []
    arrayshophpbaru = []
    arraymonsterstockbaru = arraymonsterstock
    arraymonsterpricebaru = arraymonsterprice
    # Mengecek sekalian menambah elemen pada array kosong yang dikhususkan untuk ditampilkan shop karena pada data csv hanya ada id,stock sama price
    for i in (arrayidmonstershop):
        if i in arrayidmonster:
            arrayshopmosntertypebaru.append(arraytypemonster[int(i)-1])
            arrayshopapbaru.append(arrayatkpower[int(i)-1])
            arrayshopdpbaru.append(arraydefpower[int(i)-1])
            arrayshophpbaru.append(arrayhpmonster[int(i)-1])
    potionidshopbaru = potionidshop
    arraypotiontypebaru = []
    arraypotionstockbaru = arraypotionstock
    arraypotionpricebaru = arraypotionprice
    for i in (potionidshop):
        if i in potionid:
            arraypotiontypebaru.append(arraypotiontype[int(i)-1])
    while True:
        action = input("\n>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        if action == "lihat":
            view_option = input("\n>>> Mau lihat apa? (monster/potion) : ")
            if view_option == "monster":
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                time.sleep(1)
            elif view_option == "potion":
                print(" ID |      Type      | Stok  | Harga")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                time.sleep(1)
        elif action == "tambah":
            add_option = input("\n>>> Mau nambahin apa? (monster/potion) : ")
            if add_option == "monster":
                # Pembuatan array baru khusus monster yang belum ada di shop agar jika menambah monster tinggal ambil dari array monster yg blm ada di shop
                arrayidmonsterblmada = []
                arraymonstertypeblmada = []
                arrayapblmada = []
                arraydpblmada = []
                arrayhpblmada = []
                for i in (arrayidmonster):
                    if i not in arrayidmonstershop:
                        arrayidmonsterblmada.append(arrayidmonster[int(i)-1])
                        arraymonstertypeblmada.append(arraytypemonster[int(i)-1])
                        arrayapblmada.append(arrayatkpower[int(i)-1])
                        arraydpblmada.append(arraydefpower[int(i)-1])
                        arrayhpblmada.append(arrayhpmonster[int(i)-1])
                delay_print("Berikut merupakan monster yang sudah ada di shop! ")
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                time.sleep(2)
                delay_print("Berikut monster yang belum ada di shop! ")
                for i in range(len(arraymonstertypeblmada)):
                    print(f"{arrayidmonsterblmada[i]:<3} | {arraymonstertypeblmada[i]:<14} | {arrayapblmada[i]:<9} | {arraydpblmada[i]:<9} | {arrayhpblmada[i]}")
                time.sleep(1)
                id_monster = input("\n>>> Masukkan id monster : ")
                while id_monster not in arrayidmonsterblmada:
                    id_monster = input("\n>>> Monster tidak ada, Masukkan id monster : ")
                initial_stock_monster = input("\n>>> Masukkan stok awal : ")
                while not isdigit(initial_stock_monster):
                    initial_stock_monster = input("\n>>> Harus digit, Masukkan stok awal : ")
                monster_price = input("\n>>> Masukkan harga monster : ")
                while not isdigit(monster_price):
                    monster_price = input("\n>>> Harus digit, Masukkan harga monster : ")
                for i in range(len(arrayidmonsterblmada)):
                    if id_monster == arrayidmonsterblmada[i]:
                        arrayidmonstershopbaru.append(id_monster)
                        arrayshopmosntertypebaru.append(arraymonstertypeblmada[i])
                        arrayshopapbaru.append(arrayapblmada[i])
                        arrayshopdpbaru.append(arraydpblmada[i])
                        arrayshophpbaru.append(arrayhpblmada[i])
                        arraymonsterstockbaru.append(initial_stock_monster)
                        arraymonsterpricebaru.append(monster_price)
                delay_print("Monster telah berhasil dimasukkan ke dalam shop")
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")

            elif add_option == "potion":
                # Pembuatan array baru khusus potion yang belum ada di shop agar jika menambah potion tinggal ambil dari array potion yg blm ada di shop
                arraypotiontypeblmada = []
                arraypotionidblmada = []
                for i in (potionid):
                    if i not in potionidshop:
                        arraypotionidblmada.append(potionid[int(i)-1])
                        arraypotiontypeblmada.append(potiontype[int(i)-1])
                delay_print("Berikut potion yang sudah ada di shop! ")
                print(" ID |      Type      | Stok  | Harga")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                time.sleep(1)
                delay_print("Berikut potion yang belum ada di shop")
                for i in range(len(arraypotiontypeblmada)):
                    print(f"{arraypotionidblmada[i]:<3} | {arraypotiontypeblmada[i]:<14}")
                time.sleep(1)
                id_potion = input("\n>>> Masukkan id potion : ")
                while id_potion not in potionid:
                    id_potion = input("\n>>> Masukkan id potion : ")
                initial_stock_potion = input("\n>>> Masukkan stok awal : ")
                while not isdigit(initial_stock_potion):
                    initial_stock_potion = input("\n>>> Harus Berupa Digit!Masukkan stok awal : ")
                potion_price = input("\n>>> Masukkan harga potion : ")
                while not isdigit(potion_price):
                    potion_price = input("\n>>> Harus Berupa Digit!Masukkan harga potion : ")
                for i in range(len(arraypotionidblmada)):
                    if id_potion == arraypotionidblmada[i]:
                        potionidshopbaru.append(id_potion)
                        arraypotiontypebaru.append(arraypotiontypeblmada[i])
                        arraypotionstockbaru.append(initial_stock_potion)
                        arraypotionpricebaru.append(potion_price)
                time.sleep(1)
                delay_print("Potion telah berhasil dimasukkan ke dalam shop")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
        elif action == "ubah":
            change_option = input("\n>>> Mau mengubah apa? (monster/potion) : ")
            if change_option == "monster":
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                time.sleep(1)
                id_monster = input("\n>>> Masukkan id monster : ")
                while id_monster not in arrayidmonstershopbaru:
                    id_monster = input("\n>>> Masukkan id monster : ")
                final_stock_monster = input("\n>>> Masukkan stok baru : ")
                while not isdigitorempty(final_stock_monster):
                    final_stock_monster = input("\n>>> yang bener bang..(kosong atau ga angka), Masukkan stok baru : ")
                monter_price = input("\n>>> Masukkan harga monster baru : ")
                while not isdigitorempty(monter_price):
                    monter_price = input("\n>>> yang bener bang..(kosong atau ga angka)Masukkan harga monster baru : ")
                time.sleep(1)
                # Kondisi jika hanya ingin merubah harga/stok secara parsial
                if final_stock_monster == '' and monter_price != '':
                    for i in range(len(arrayidmonstershopbaru)):
                        if id_monster == arrayidmonstershopbaru[i]:
                            arraymonsterprice[i] = monter_price
                elif monter_price == '' and final_stock_monster != '':
                    for i in range(len(arrayidmonstershopbaru)):
                        if id_monster == arrayidmonstershopbaru[i]:
                            arraymonsterstock[i] = final_stock_monster
                else: # Jika ingin mengubah keduanya
                    for i in range(len(arrayidmonstershopbaru)):
                        if id_monster == arrayidmonstershopbaru[i]:
                            arraymonsterstock[i] = final_stock_monster
                            arraymonsterprice[i] = monter_price
                delay_print("\nMonster yang anda pilih telah berhasil dirubah ke dalam shop")
                time.sleep(1)
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                
            elif change_option == "potion":
                print(" ID |      Type      | Stok  | Harga")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                id_potion = input("\n>>> Masukkan id potion : ")
                while id_potion not in potionidshopbaru:
                    id_potion = input("\n>>> Masukkan id potion : ")
                final_stock_potion = input("\n>>> Masukkan stok baru : ")
                while not isdigitorempty(final_stock_potion):
                    final_stock_potion = input("\n>>> yang bener bang..(kosong atau ga angka), Masukkan stok baru : ")
                potion_price = input("\n>>> Masukkan harga monster baru : ")
                while not isdigitorempty(potion_price):
                    potion_price = input("\n>>> yang bener bang..(kosong atau ga angka)Masukkan harga monster baru : ")
                time.sleep(1)
                # Kondisi jika hanya ingin merubah harga/stok secara parsial
                if final_stock_potion == '' and potion_price != '':
                    for i in range(len(potionidshopbaru)):
                        if id_potion == potionidshopbaru[i]:
                            arraypotionpricebaru[i] = potion_price
                elif potion_price == '' and final_stock_potion != '':
                    for i in range(len(potionidshopbaru)):
                        if id_potion == potionidshopbaru[i]:
                            arraypotionstockbaru[i] = final_stock_potion
                else: # Jika ingin mengubah keduanya
                    for i in range(len(potionidshopbaru)):
                        if id_potion == potionidshopbaru[i]:
                            arraypotionpricebaru[i] = potion_price
                            arraypotionstockbaru[i] = final_stock_potion
                delay_print("Potion yang ada pilih telah berhasil dirubah ke dalam shop")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
        elif action == "hapus":
            delete_option = input("\n>>> Mau menghapus apa? (monster/potion) : ")
            if delete_option == "monster":
                print(" ID |      Type      | ATK Power | DEF Power | HP   | Stok  | Harga")
                for i in range(len(arrayidmonstershopbaru)):
                    print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                id_monster = input("\n>>> Masukkan id monster : ")
                while id_monster not in arrayidmonstershopbaru:
                    id_monster = input("\n>>> Masukkan id monster : ")
                sure = input("Apakah anda yakin ingin menghapus (nama monster)? (y/n) : ")
                if sure == "y":
                    for index in range(len(arrayidmonstershopbaru)):
                        if id_monster == arrayidmonstershop[index]:
                            arrayidmonstershopbaru = remove_element(arrayidmonstershopbaru,index)
                            arrayshopmosntertypebaru = remove_element(arrayshopmosntertypebaru,index)
                            arrayshopapbaru = remove_element(arrayshopapbaru,index)
                            arrayshopdpbaru = remove_element(arrayshopdpbaru,index)
                            arrayshophpbaru = remove_element(arrayshophpbaru,index)
                            arraymonsterstockbaru = remove_element(arraymonsterstockbaru,index)
                            arraymonsterpricebaru = remove_element(arraymonsterpricebaru,index)
                    arrayidmonstershop = arrayidmonstershopbaru
                    arraymonsterstock = arraymonsterstockbaru
                    arraymonsterprice = arraymonsterpricebaru
                    delay_print("Monster yang anda pilih berhasil dihapus dari shop")
                    for i in range(len(arrayidmonstershopbaru)):
                        print(f"{arrayidmonstershopbaru[i]:<3} | {arrayshopmosntertypebaru[i]:<14} | {arrayshopapbaru[i]:<9} | {arrayshopdpbaru[i]:<9} | {arrayshophpbaru[i]:<4} | {arraymonsterstockbaru[i]:<5} | {arraymonsterpricebaru[i]}")
                else:
                    print("Monster yang anda pilih tidak jadi dihapus")
            elif delete_option == "potion":
                print(" ID |      Type      | Stok  | Harga")
                for i in range(len(potionidshopbaru)):
                    print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                id_potion = input("\n>>> Masukkan id potion : ")
                while id_potion not in potionidshopbaru:
                    id_potion = input("\n>>> Masukkan id potion : ")
                sure = input("Apakah anda yakin ingin menghapus (jenis potion)? (y/n) : ")
                if sure == "y":
                    for index in range(len(potionidshop)):
                        if id_potion == potionidshop[index]:
                            potionidshopbaru = remove_element(potionidshopbaru, index)
                            arraypotiontypebaru = remove_element(arraypotiontypebaru, index)
                            arraypotionstockbaru = remove_element(arraypotionstockbaru, index)
                            arraypotionpricebaru = remove_element(arraypotionpricebaru, index)
                    delay_print("\nPotion yang ada pilih berhasil dihapus dari shop")
                    for i in range(len(potionidshopbaru)):
                        print(f"{potionidshopbaru[i]:<3} | {arraypotiontypebaru[i]:<14} | {arraypotionstockbaru[i]:<5} | {arraypotionpricebaru[i]}")
                else:
                    delay_print("Potion yang ada pilih tidak jadi dihapus dari shop ")       
        elif action == "keluar":
            delay_print(f"\nDadah {userdatabase[1]}, c uuuu!!>-<")
            False
            break
        else:
            print("\nUpsss...Sepertinya perintah Anda tidak sesuai")
            time.sleep(1)
            print("\nCoba ulangi ")
    arrayidmonstershop = arrayidmonstershopbaru
    arraymonsterstock = arraymonsterstockbaru
    arraymonsterprice = arraymonsterpricebaru
    arraypotiontype = arraypotiontypebaru
    arraypotionstock = arraypotionstockbaru
    arraypotionprice = arraypotionpricebaru
    return arrayidmonstershop, arraymonsterstock, arraymonsterprice, arraypotiontype, arraypotionstock, arraypotionprice
# Fungsi mengecek apakah input berupa string bilangan
def isdigit(s):
    for char in s:
        if char < '0' or char > '9':
            return False
    return True
# Fungsi mengecek apakah input berupa string bilangan atau kosong
def isdigitorempty(s):
    if s == '':
        return True
    for char in s:
        if char < '0' or char > '9':
            return False
    return True
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           MONSTER MANAGEMENT
def monster_management(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    delay_print("============== MONSTER ==============")
    delay_print("\nSELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    print("///     RAWWRRRRRR     ////")
    time.sleep(0.5)
    print("///     GROUGHHHHH     ////")
    time.sleep(0.5)
    print("///     AUWHHHHHHH     ////")
    time.sleep(0.5)
    while True:
        print("\n1. Tampilkan semua Monster")
        print("2. Tambah monster baru")
        print("3. Keluar")
        mm_option = input(">>>> Pilih salah satu aksi: ")
        if mm_option == "1":
            print(" ID |      Type      | ATK Power | DEF Power | HP   ")
            for i in range(len(arrayidmonster)):
                print(f"{arrayidmonster[i]:<3} | {arraytypemonster[i]:<14} | {arrayatkpower[i]:<9} | {arraydefpower[i]:<9} | {arrayhpmonster[i]:<4}")
        elif mm_option == "2":
            delay_print("Memulai pembuatan monster baru....")
            time.sleep(1)
            print(" ")
            monster_type = input("Masukkan Type/Nama Monster : ")
            while isMonsterExist(monster_type,arraytypemonster) == True:
                print("Nama sudah terdaftar, coba lagi!")
                monster_type = input("Masukkan Type/Nama Monster : ")
            atk_power = input("Masukkan ATK Power : ")
            while isCharValid(atk_power) == False:
                print("ATK Power harus bernilai integer (0-9)")
                atk_power = input("Masukkan ATK Power : ")
            def_power = input("Masukkan DEF Power :")
            while isCharValid(def_power) == False:
                print("DEF Power harus bernilai integer (0-9)")
                def_power = input("Masukkan DEF Power : ")
            while int(def_power) > 50:
                print("DEF Power harus bernilai di antara 0 dan 50!")
                def_power = input("Masukkan DEF Power : ")
            hp_monster = input("Masukkan HP : ")
            while isCharValid(hp_monster) == False:
                print("HP harus bernilai integer (0-9)")
                hp_monster = input("Masukkan HP : ")
            time.sleep(2)
            delay_print("Monster baru telah berhasil dibuat! ")
            print(f"Type : {monster_type} \nATK Power : {atk_power} \nDEF Power : {def_power} \nHP : {hp_monster}")
            addtodatabase = input(">>>Tambahkan monster ke dalam database(y/n)? ")
            if addtodatabase == "y" or addtodatabase == "Y":
                arrayidmonster.append(str(len(arrayidmonster)+1))
                arraytypemonster.append(monster_type)
                arrayatkpower.append(atk_power)
                arraydefpower.append(str(def_power))
                arrayhpmonster.append(hp_monster)
                gambarmonster.append(default_monster)
                time.sleep(2)
                delay_print("Selamat! Monster berhasil ditambahkan ke database! ")
            else:
                delay_print("Monster tidak jadi ditambahkan ke database")
        elif mm_option == "3":
            break
        else:
            print("Beri masukkan yang benar!!! : ")
    return arrayidmonster,arraytypemonster,arrayatkpower,arraydefpower,arrayhpmonster,gambarmonster
# Fungsi mengecek apakah monster ada pada suatu array
def isMonsterExist(namamonster,arraytypemonster):
    for i in range(len(arraytypemonster)):
        if namamonster == arraytypemonster[i]:
            return True
    return False
# Fungsi mengecek apakah inputan user untuk atribut berupa string bilangan
def isCharValid(atk_power):
    for char in atk_power:
        if char < '0' or char > '9': 
            return False
    return True
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                  BATTLE
def battle(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv,levelmusuh=None,ocreceived=None,pilihmonster=None,indeksrngmusuh=None):
    delay_print("============== BATTLE ==============")
    if indeksrngmusuh is None:
        indeksrngmusuh = callingnum(1,5)
        musuh = arraytypemonster[indeksrngmusuh]
        gambarmusuh = gambarmonster[indeksrngmusuh]
    else:
        indeksrngmusuh = indeksrngmusuh
        musuh = arraytypemonster[indeksrngmusuh]
        gambarmusuh = gambarmonster[indeksrngmusuh]
    if levelmusuh is None:
        levelmusuh = callingnum(1,5)
    else:
        levelmusuh = levelmusuh
    if levelmusuh == 1:
        apmusuh = int(arrayatkpower[indeksrngmusuh])
        dpmusuh = int(arraydefpower[indeksrngmusuh])
        hpmusuh = int(arrayhpmonster[indeksrngmusuh])
        seranganmusuh = callingnum(apmusuh-(0.3*apmusuh),apmusuh+(0.3*apmusuh))
    else:
        apmusuh = int(arrayatkpower[indeksrngmusuh]) + ((levelmusuh*0.1)*int(arrayatkpower[indeksrngmusuh]))
        dpmusuh = int(arraydefpower[indeksrngmusuh]) + ((levelmusuh*0.1)*int(arraydefpower[indeksrngmusuh]))
        hpmusuh = int(arrayhpmonster[indeksrngmusuh]) + ((levelmusuh*0.1)*int(arrayhpmonster[indeksrngmusuh]))
        seranganmusuh = callingnum(apmusuh-(0.3*apmusuh),apmusuh+(0.3*apmusuh))
    delay_print(f"RAWRRRRRRRRR Monster {musuh} telah muncul")
    print(gambarmusuh)
    print(f"Name      : {musuh}")
    print(f"ATK Power : {apmusuh}") 
    print(f"DEF Power : {dpmusuh}") 
    print(f"HP        : {hpmusuh}")
    print(f"Level     : {levelmusuh}")
    delay_print("============= MONSTER LIST =============")
    arraybattleidmonster = []
    arraybattletypemonster = []
    arraybattleap = []
    arraybattledp = []
    arraybattlehp = []
    arraybattlelevel = []
    arraybattleqty = []
    arraybattlepotiontype = []
    count = []
    gambarkita = []
    c = 0
    for i in range(len(arrayuseridIinv)):
        if userdatabase[0] == arrayuseridIinv[i]:
            arraybattleqty.append(arrayqtyIinv[i])
            arraybattlepotiontype.append(arraytypeIinv[i])
    indeksstrength = find_index(arraybattlepotiontype,'strength')
    indekshealing = find_index(arraybattlepotiontype,'healing')
    indeksresilience = find_index(arraybattlepotiontype,'resilience')
    for i in range(len(arrayuseridMinv)):
        if userdatabase[0] == arrayuseridMinv[i]:
            arraybattleidmonster.append(arrayidmonsterMinv[i])
            arraybattlelevel.append(arraymonsterlevel[i])
    for i in arraybattleidmonster:
        if i in arrayidmonster:
            monsterindeks = find_index(arrayidmonster,i)
            arraybattletypemonster.append(arraytypemonster[monsterindeks])
            arraybattleap.append(arrayatkpower[monsterindeks])
            arraybattledp.append(arraydefpower[monsterindeks])
            arraybattlehp.append(arrayhpmonster[monsterindeks])
            gambarkita.append(gambarmonster[monsterindeks])
    for i in range(len(arraybattleidmonster)):
        c += 1
        count.append(str(c))
        print(f"{i+1}. {arraybattletypemonster[i]} ")
    if pilihmonster == None:
        pilihmonster = input("Pilih monster yang ingin anda gunakan untuk bertarung : ")
        while pilihmonster not in count:
            pilihmonster = input("Pilihan monster anda tidak valid, pilih monster dengan benar : ")
    else:
        pilihmonster = pilihmonster
    indeks = int(pilihmonster) - 1
    monsterkita = arraybattletypemonster[indeks]
    gambarkita = gambarkita[indeks]
    apkita = int(arraybattleap[indeks])
    dpkita = int(arraybattledp[indeks])
    hpkita = int(arraybattlehp[indeks])
    levelkita = int(arraybattlelevel[indeks])
    if levelkita == 1:
        apkita = int(arraybattleap[indeks])
        dpkita = int(arraybattledp[indeks])
        hpkita = int(arraybattlehp[indeks])
        serangankita = callingnum(apkita-(0.3*apkita),apkita+(0.3*apkita))
    else:
        apkita = int(arrayatkpower[indeks]) + ((levelkita*0.1)*int(arrayatkpower[indeks]))
        dpkita = int(arraydefpower[indeks]) + ((levelkita*0.1)*int(arraydefpower[indeks]))
        hpkita = int(arrayhpmonster[indeks]) + ((levelkita*0.1)*int(arrayhpmonster[indeks]))
        serangankita = callingnum(apkita-(0.3*apkita),apkita+(0.3*apkita))

    delay_print(f"GROUGHHHHHHHHH! Agent {userdatabase[1]} mengeluarkan monster {arraybattletypemonster[indeks]} untuk melawan monster {musuh}.")
    print(gambarkita)
    salahsatukalah = False
    turn = 0
    time.sleep(2)
    print(f"{gambarmusuh} {vs} {gambarkita}")
    damagediterima = 0
    damagediberikan = 0
    while not salahsatukalah:
        turn += 1
        delay_print(f"============= TURN {turn} {arraybattletypemonster[indeks]} =============")
        print("1. Attack \n2. Use Potion \n3. Quit")
        turnoption = input()
        arrayturnoption = ['1','2','3']
        
        while turnoption not in arrayturnoption:
            turnoption = input("Pilihan tidak valid, pilih opsi lagi : ")
        
        if turnoption == '1':
            print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
            hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
            damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
            print(f"Name          : {musuh}")
            print(f"ATK Power     : {seranganmusuh}")
            print(f"DEF Power     : {dpmusuh}")
            print(f"Sisa hp musuh : {hpmusuh // 1}")
            print(f"Level         : {levelmusuh}")
            time.sleep(0.5)
            print(f"==[ Penjelasan : ATK Power : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
        
        elif turnoption == "2":
            delay_print("============== POTION LIST ==============")
            print(f"1. Strength Potion (Qty: {arraybattleqty[indeksstrength]} ) - Increase ATK Power \n2. Resilience Potion (Qty: {arraybattleqty[indeksresilience]} ) - Increase DEF Power \n3. Healing Potion (Qty: {arraybattleqty[indekshealing]} ) - Restores Health \n4. Cancel")
            pilihpotion = input(">>> Pilih Potion : ")
            arraypilihanpotion = ['1','2','3','4']
            
            while pilihpotion not in arraypilihanpotion:
                pilihpotion = input(">>> Pilih Potion : ")
            
            if pilihpotion == '1':
                if int(arraybattleqty[indeksstrength]) > 0:
                    print(f"Muncul aura kekuatan yang bersinar dari monster {monsterkita}")
                    time.sleep(0.4)
                    delay_print("////PRRRAHHHHH////")
                    arraybattleqty[indeksstrength] = str(int(arraybattleqty[indeksstrength]) - 1)
                    serangankita += (0.05 * serangankita)
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
                else:
                    print("Potion habis!")
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
            
            elif pilihpotion == '2':
                if int(arraybattleqty[indeksresilience]) > 0:
                    print(f"Monster {monsterkita} tiba-tiba dikelilingi armor pelindung yang sangat tebal")
                    time.sleep(0.4)
                    delay_print(f"Monster {monsterkita} menjadi semakin tangguh!!!")
                    arraybattleqty[indeksresilience] = str(int(arraybattleqty[indeksresilience]) - 1)
                    dpkita += (0.05 * dpkita)
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
                else:
                    print("Potion habis!")
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")

            
            elif pilihpotion == '3':
                if int(arraybattleqty[indekshealing]) > 0:
                    print(f"Luka-luka yang ada di tubuh monster {monsterkita} akibat monster {musuh} hilang secara perlahan-lahan")
                    delay_print(f"Monster {monsterkita} sudah pulih dan siap kembali melanjutkan pertarungan!!!")
                    arraybattleqty[indekshealing] = str(int(arraybattleqty[indekshealing]) - 1)
                    hpkita += (0.25 * hpkita)
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
                else:
                    print("Potion habis!")
                    print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                    hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                    damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                    print(f"Name          : {musuh}")
                    print(f"ATK Power     : {seranganmusuh}")
                    print(f"DEF Power     : {dpmusuh}")
                    print(f"Sisa hp musuh : {hpmusuh // 1}")
                    print(f"Level         : {levelmusuh}")
                    time.sleep(0.5)
                    print(f"==[ Penjelasan : ATK Power kita : {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")

            
            elif pilihpotion == '4':
                print(f"BAMMMMMM!!!!, {monsterkita} menyerang {musuh}")
                hpmusuh -= ((serangankita) - ((dpmusuh / 100) * serangankita))
                damagediberikan += (serangankita) - ((dpmusuh / 100) * serangankita)
                print(f"Name          : {musuh}")
                print(f"ATK Power     : {seranganmusuh}")
                print(f"DEF Power     : {dpmusuh}")
                print(f"Sisa hp musuh : {hpmusuh // 1}")
                print(f"Level         : {levelmusuh}")
                time.sleep(0.5)
                print(f"==[ Penjelasan : ATK Power kita: {serangankita}, dikurangi DEF Power musuh : {dpmusuh}%, ATK Result : {(serangankita) - ((dpmusuh / 100) * serangankita)}, sisa HP musuh : {hpmusuh // 1} ]==")
                continue
        
        elif turnoption == "3":
            delay_print(f"Monster {musuh} tampaknya terlalu kuat hingga membuat monster {monsterkita} qtarr qtirrr")
            delay_print(f"Monster {monsterkita} mencari celah untuk kabur....")
            time.sleep(1)
            print(f"Monster {monsterkita} berhasil kabur dan meninggalkan pertarungan!")
            salahsatukalah = True
            if ocreceived is None:
                userdatabase[4] = str(int(userdatabase[4])+0)
                for i in range(len(arrayuserid)):
                    if userdatabase[0] == arrayuserid[i]:
                        arrayuseroc[i] = userdatabase[4]
            else:
                ocreceived = ocreceived
            return True,musuh,ocreceived,damagediterima,damagediberikan,arrayuseroc,pilihmonster,indeksrngmusuh
        time.sleep(1)
        delay_print(f"============= TURN {turn} {musuh} =============")
        time.sleep(2)
        print(f"JDERRRRRRRRR!!!, {musuh} menyerang {monsterkita}")
        hpkita -= ((seranganmusuh) - ((dpkita / 100) * (seranganmusuh)))
        damagediterima += (seranganmusuh) - ((dpkita / 100) * (seranganmusuh))
        print(f"Name          : {monsterkita}")
        print(f"ATK Power     : {serangankita}")
        print(f"DEF Power     : {dpkita}")
        print(f"Sisa hp kamu  : {hpkita // 1}")
        print(f"Level         : {levelkita}")
        time.sleep(0.5)
        print(f"==[ Penjelasan : ATK Power musuh: {seranganmusuh}, dikurangi DEF Power kita : {dpkita}%, ATK Result : {(seranganmusuh) - ((dpkita / 100) * seranganmusuh)}, sisa HP kita : {hpkita // 1} ]==")
        if hpkita <= 0:
            if ocreceived is None:
                userdatabase[4] = str(int(userdatabase[4])+0)
                for i in range(len(arrayuserid)):
                    if userdatabase[0] == arrayuserid[i]:
                        arrayuseroc[i] = userdatabase[4]
            else:
                ocreceived = ocreceived
            defeat = '''
                                ▓█████▄ ▓█████   █████▒▓█████ ▄▄▄     ▄▄▄█████▓
                                ▒██▀ ██▌▓█   ▀ ▓██   ▒ ▓█   ▀▒████▄   ▓  ██▒ ▓▒
                                ░██   █▌▒███   ▒████ ░ ▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░
                                ░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ 
                                ░▒████▓ ░▒████▒░▒█░    ░▒████▒▓█   ▓██▒ ▒██▒ ░ 
                                ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░    ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   
                                ░ ▒  ▒  ░ ░  ░ ░       ░ ░  ░ ▒   ▒▒ ░   ░    
                                ░ ░  ░    ░    ░ ░       ░    ░   ▒    ░      
                                ░       ░  ░           ░  ░     ░  ░        
                                ░                                                                   
                                '''
            graveyardkita = f'''
                                ___________________________________________
                                |                                           |
                                |  Farewell {monsterkita},                  |
                                |  Your legacy will forever be remembered   |
                                |  by the Danvillians.                      |
                                |___________________________________________|
                                                    ||                  .
                                                    ||                  |
                                                    ||                 -|-
                                                    ||              .-'~~~`-.
                                                    ||            .'         `.
                                                    ||            |  R  I  P  |
                                                    ||            |           |
                                                    ||            |           |
                                                    ||          /\|           |/|
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''
            print(defeat)
            print(graveyardkita)
            salahsatukalah = True
            return True,musuh,ocreceived,damagediterima,damagediberikan,arrayuseroc,pilihmonster,indeksrngmusuh
        if hpmusuh <= 0:
            victory = '''
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
                                    ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
                                    ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
                                    ░▒▓██▓▒░  ░▒▓█▓▒░░▒▓██████▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    '''
            graveyardmusuh = f'''

                                        _______________________________
                                        |                               |
                                        | Farewell{musuh},              |
                                        | may you find no               |
                                        | peace.                        |
                                        |_______________________________|
                                                    ||                  .
                                                    ||                  |
                                                    ||                 -|-
                                                    ||              .-'~~~`-.
                                                    ||            .'         `.
                                                    ||            |  R  I  P  |
                                                    ||            |           |
                                                    ||            |           |
                                                    ||          /\|           |/|
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''
            print(victory)
            print(graveyardmusuh)
            if ocreceived is None:
                ocreceived = callingnum(50,100)
                userdatabase[4] = str(int(userdatabase[4]) + ocreceived)
                for i in range(len(arrayuserid)):
                    if userdatabase[0] == arrayuserid[i]:
                        arrayuseroc[i] = userdatabase[4]
            else:
                ocreceived = ocreceived
            print(f"Kamu memperoleh O.W.C.A. Coin sebesar {ocreceived} karena telah mengalahkan monster {musuh}")
            salahsatukalah = True
            return False,musuh,ocreceived,damagediterima,damagediberikan,arrayuseroc,pilihmonster,indeksrngmusuh
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                  ARENA  
def arena(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    delay_print("WELCOME DI ARENA!!")
    countstage = 0
    totalocreceived = 0
    totaldamagediterima = 0
    totaldamagediberikan = 0
    delay_print(f"========= WELCOME TO STAGE 1 =========")
    kitakalah,musuh,ocreceived,damagediterima,damagediberikan,arrayuseroc,pilihmonster,indeksrngmusuh = battle(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv,1,50*1,pilihmonster=None,indeksrngmusuh=None)
    if kitakalah == True:
        totaldamagediberikan += damagediberikan
        totaldamagediterima += damagediterima
        totalocreceived += ocreceived
        delay_print(f"NT Bang!! Monster kamu dikalahin sama {musuh}. Jangan nyerah ya!!")
        delay_print("GAME OVER! Kamu hanya berhasil sampai pada Arena 1!")
        delay_print("Merangkum hasil pertandingan")
        time.sleep(2)
        delay_print("=============== STATS ===============")
        delay_print(f"Total hadiah      : {totalocreceived} OC \nJumlah stage      : {countstage} \nDamage diberikan  : {totaldamagediberikan//1} \nDamage diterima   : {totaldamagediterima//1}")
        print("SESI LATIHAN TELAH BERAKHIR")
        delay_print("Sampai jumpa pada sesi latihan berikutnya!!")
    elif kitakalah == False:
        delay_print(f"SELAMAT KAMU TELAH MEMENANGKAN STAGE 1, BERSIAP UNTUK MEMASUKI STAGE 2")
        totaldamagediberikan += damagediberikan
        totaldamagediterima += damagediterima
        totalocreceived += ocreceived
        countstage += 1
        for i in range(1,5):
            delay_print(f"========= WELCOME TO STAGE {i+1} =========")
            kitakalah,musuh,ocreceived,damagediterima,damagediberikan,arrayuseroc,pilihmonster,indeksrngmusuh = battle(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv,i+1,(50*(i+1)),pilihmonster=pilihmonster,indeksrngmusuh=indeksrngmusuh)
            if kitakalah == True:
                totaldamagediberikan += damagediberikan
                totaldamagediterima += damagediterima
                totalocreceived += ocreceived
                for i in range(len(arrayuserid)):
                    if userdatabase[0] == arrayuserid[i]:
                        arrayuseroc[i] = str(int(arrayuseroc[i]) + totalocreceived)
                delay_print(f"NT Bang!! Monster kamu dikalahin sama {musuh}. Jangan nyerah ya!!")
                delay_print(f"GAME OVER! Kamu berhasil sampai pada Arena {i+1}!")
                delay_print("Merangkum hasil pertandingan")
                time.sleep(2)
                delay_print("=============== STATS ===============")
                delay_print(f"Total hadiah      : {totalocreceived} OC \nJumlah stage      : {countstage} \nDamage diberikan  : {totaldamagediberikan//1} \nDamage diterima   : {totaldamagediterima//1}")
                print("SESI LATIHAN TELAH BERAKHIR")
                delay_print("Sampai jumpa pada sesi latihan berikutnya!!")
                break
            elif kitakalah == False:
                delay_print(f"SELAMAT KAMU TELAH MEMENANGKAN STAGE {i+1}, BERSIAP UNTUK MEMASUKI STAGE {i+2}")
                totaldamagediberikan += damagediberikan
                totaldamagediterima += damagediterima
                totalocreceived += ocreceived
                countstage += 1
                pass
    if countstage == 5:
        print("GOKIL!! Kamu berhasil nyelesein arena sampe stage 5!")
        delay_print("Merangkum hasil pertandingan....")
        time.sleep(2)
        delay_print("============== STATS ==============")
        delay_print(f"Total hadiah      : {ocreceived} OC \nJumlah stage      : {countstage} \nDamage diberikan  : {totaldamagediberikan//1} \nDamage diterima   : {totaldamagediterima//1}")
        for i in range(len(arrayuserid)):
            if userdatabase[0] == arrayuserid[i]:
                arrayuseroc[i] = str(int(arrayuseroc[i]) + ocreceived)
        print("SESI LATIHAN TELAH BERAKHIR")
        delay_print("Sampai jumpa pada sesi latihan berikutnya!!")
    else:
        return userdatabase,arrayuseroc
    return userdatabase,arrayuseroc
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                              REGISTER
def register(arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    arrayuserid,arrayusername,arraypassword,arrayuserrole,arrayuseroc    
    delay_print("============== REGISTER ==============")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    while isUserValid(username) == False:
        delay_print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    
    while isUserExist(username,arrayusername):
        delay_print("Username sudah terpakai, silahkan gunakan username lain!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    delay_print("Pilih salah satu monster untuk menjadi monster awalmu!!")
    delay_print("Pilih monster kalian:")
    for i in range(len(arrayidmonster)):
        delay_print(f"{i+1}. {arraytypemonster[i]}")
    monster_choice = input("Pilih : ")
    while monster_choice not in arrayidmonster:
        monster_choice = input("Pilihan anda tidak ada, Pilih lagi dengan benar : ")
    indexmonsterchoice = find_index(arrayidmonster,monster_choice)
    arrayidmonsterMinv.append(arrayidmonster[indexmonsterchoice])
    arraymonsterlevel.append("1")
    arrayuseridMinv.append(str(len(arrayuserid)+1))
    arrayuserid.append(str(len(arrayuserid)+1))
    arrayusername.append(username)
    arraypassword.append(password)
    arrayuserrole.append('agent')
    arrayuseroc.append('0')
    for i in range(3):
        arrayuseridIinv.append(str(len(arrayuserid)))
        arrayqtyIinv.append('0')
    arraytypeIinv.append('strength')
    arraytypeIinv.append('resilience')
    arraytypeIinv.append('healing')
    newuserdatabase = [arrayuserid[len(arrayuserid)-1],arrayusername[len(arrayusername)-1],arraypassword[len(arraypassword)-1],arrayuserrole[len(arrayuserrole)-1],arrayuseroc[len(arrayuseroc)-1]]
    delay_print(f"Selamat datang {newuserdatabase[3]} {newuserdatabase[1]}. Mari kita mengalahkan Dr Asep Spakbor dengan {arraytypemonster[int(monster_choice)-1]}!")
    return True,newuserdatabase,monster_choice,arrayuseridMinv,arrayidmonsterMinv,arraymonsterlevel,arrayuserid,arrayusername,arraypassword,arrayuserrole,arrayuseroc,arraytypeIinv,arrayqtyIinv,arrayuseridIinv
# Fungsi mengecek apakah username terdiri dari alfabet/angka/strip/underscore
def isUserValid(a):
    for char in a:
        i = ord(char)
        if not (64 < i < 91 or 96 < i < 123 or 47 < i < 58 or i == 45 or i == 95):
            return False
    return True
# Fungsi mengecek apakah username sudah ada pada database(array username)
def isUserExist(a,arrayusername):
    for i in range(len(arrayusername)):
        if arrayusername[i] == a:
            return True
    return False
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                 LOGIN
def login(arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    delay_print("============== LOG-IN ==============")
    while True:
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        
        if not isUserExist(username, arrayusername):
            delay_print("Username tidak terdaftar!")
            option = input("Coba lagi? (y/n): ")
            if option.lower() != 'y':
                return False, None
            continue
        
        count = 0
        for i in range(len(arrayusername)):
            count += 1
            if arrayusername[i] == username:
                break
        
        if arraypassword[count-1] == password:
            delay_print(f"Selamat datang {arrayuserrole[count-1]} {arrayusername[count-1]}!")
            delay_print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil! ")
            userdatabase = [arrayuserid[count-1], arrayusername[count-1], arraypassword[count-1], arrayuserrole[count-1], arrayuseroc[count-1]]
            return True, userdatabase  # Mengembalikan userdatabase setelah login berhasil
        else:
            delay_print("Password salah.")
            option = input("Coba lagi? (y/n): ")
            if option.lower() != 'y':
                return False, None
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                SAVE
# Fungsi mengubah dari array ke dictionary
def list_to_dict(arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv):
    userdict = {'id' : arrayuserid, 'username' : arrayusername, 'password' : arraypassword, 'role' : arrayuserrole, 'oc' : arrayuseroc}
    monsterdict = {'id' : arrayidmonster, 'type' : arraytypemonster, 'atk_power' : arrayatkpower, 'def_power' : arraydefpower, 'hp' : arrayhpmonster}
    monster_shopdict = {'monster_id' : arrayidmonstershop, 'stock' : arraymonsterstock, 'price' : arraymonsterprice}
    monster_inventorydict = {'user_id' : arrayuseridMinv, 'monster_id' : arrayidmonsterMinv, 'level' : arraymonsterlevel}
    item_shopdict = {'type' : arraypotiontype, 'stock' : arraypotionstock, 'price' : arraypotionprice}
    item_inventorydict = {'user_id' : arrayuseridIinv, 'type' : arraytypeIinv, 'quantity' : arrayqtyIinv}
# Fungsi mengubah dari dictionary ke csv
def dict_to_csv(folder, filename, dict_data):
    folder_path = os.path.join(os.getcwd(), folder)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
    with open(file_path, mode='w', newline='') as file:
        header = ';'.join(dict_data.keys()) + '\n'
        file.write(header)
        max_length = max(len(arr) for arr in dict_data.values())
        for i in range(max_length):
            row = [
                dict_data[key][i] if i < len(dict_data[key]) else ''
                for key in dict_data.keys()
            ]
            file.write(';'.join(row))
            if i < max_length - 1:
                file.write('\n')
# Fungsi menyimpan csv ke folder path
def save(folder_path,userdict,monsterdict,monster_shopdict,monster_inventorydict,item_shopdict,item_inventorydict):
    os.makedirs(folder_path, exist_ok=True)
    delay_print(f"Saving....")
    delay_print(f"Saving user.csv ke dalam folder : {folder_path}")
    delay_print(f"Saving monster.csv ke dalam folder : {folder_path}")
    delay_print(f"Saving monster_shop.csv ke dalam folder : {folder_path}")
    delay_print(f"Saving monster_inventory.csv ke dalam folder : {folder_path}")
    delay_print(f"Saving item_shop.csv ke dalam folder : {folder_path}")
    delay_print(f"Saving item_inventory.csv ke dalam folder : {folder_path}")
    dict_to_csv(folder_path, 'user.csv', userdict)
    dict_to_csv(folder_path, 'monster.csv', monsterdict)
    dict_to_csv(folder_path, 'monster_shop.csv', monster_shopdict)
    dict_to_csv(folder_path, 'monster_inventory.csv', monster_inventorydict)
    dict_to_csv(folder_path, 'item_shop.csv', item_shopdict)
    dict_to_csv(folder_path, 'item_inventory.csv', item_inventorydict)
    delay_print(f"Data berhasil disimpan di dalam folder {folder_path}")
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                MENU & HELP
def menu_help(sudahlogin, userdatabase=None):
    # DARI FILE USER.CSV
    arrayusername = userdict['username']
    arraypassword = userdict['password']
    arrayuserid = userdict['id']
    arrayuserrole = userdict['role']
    arrayuseroc = userdict['oc']
    # DARI FILE MONSTER.CSV
    arrayatkpower = monsterdict['atk_power']
    arrayidmonster = monsterdict['id']
    arraytypemonster = monsterdict['type']
    arraydefpower = monsterdict['def_power']
    arrayhpmonster = monsterdict['hp']
    # DARI FILE MONSTER_SHOP.CSV
    arrayidmonstershop = monster_shopdict['monster_id']
    arraymonsterstock = monster_shopdict['stock']
    arraymonsterprice = monster_shopdict['price']
    # DARI FILE MONSTER_INVENTORY.CSV
    arrayuseridMinv = monster_inventorydict['user_id']
    arrayidmonsterMinv = monster_inventorydict['monster_id']
    arraymonsterlevel = monster_inventorydict['level']
    # DARI FILE ITEM_SHOP.CSV
    arraypotiontype = item_shopdict['type']
    arraypotionstock = item_shopdict['stock']
    arraypotionprice = item_shopdict['price']
    # DARI FILE ITEM_INVENTORY.CSV
    arrayuseridIinv = item_inventorydict['user_id']
    arraytypeIinv = item_inventorydict['type']
    arrayqtyIinv = item_inventorydict['quantity']
    if userdatabase is None:
        userdatabase = []  
    call = input(">>> ")
    delay_print("============== HELP ==============")
    if call.lower() == "help":
        if sudahlogin and len(userdatabase) > 0:  #Kalau sudah login dan userdatabase tidak kosong
            if userdatabase[3] == "admin":
                print(f"Halo Admin {userdatabase[1]}. Kamu memanggil command HELP.\nBerikut adalah hal-hal yang dapat kamu lakukan:")
                print("1. Logout : Keluar dari akun yang sedang digunakan.\n2. Shop Management : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent.\n3. Monster Management : Melakukan manajemen pada monster agar permainan berlangsung dengan lancar")
                arraypilihan = ['1','2','3']
                actionchoice = input(">>> Pilih yang mau kamu lakukan : ")
                while actionchoice not in arraypilihan:
                    actionchoice = input(">>> Pilihan kamu tidak valid, pilih yang mau kamu lakukan : ")
                if actionchoice == "1":
                    delay_print("Sebelum anda logout")
                    save_option = input("Apakah Anda ingin menyimpan hasil ke file CSV? (y/n): ")
                    arrsaveopt = ['y','n','Y','N']
                    while save_option not in arrsaveopt:
                        save_option = input("Ulangi, Apakah Anda ingin menyimpan hasil ke file CSV? (y/n): ")
                    if save_option.lower() == 'y':
                        folder_path = input("Masukkan nama folder untuk menyimpan file : ")
                        save(folder_path,userdict,monsterdict,monster_shopdict,monster_inventorydict,item_shopdict,item_inventorydict)
                        delay_print("Processing to log out...")
                        time.sleep(1)
                        print("Anda telah log out!")
                        exitornot = input("File anda sudah disimpan, apakah anda ingin keluar dari aplikasi? (press any key to continue or y to exit app) : ")
                        if exitornot.lower() == 'y':
                            exit()
                        else:
                            menu_help(sudahlogin=False,userdatabase=None)
                    else:
                        delay_print("Data tidak jadi disimpan....")
                        delay_print("Processing to log out...")
                        time.sleep(1)
                        print("Anda telah log out!")
                        exitornot = input("apakah anda ingin keluar dari aplikasi? (press any key to continue or y to exit app) : ")
                        if exitornot.lower() == 'y':
                            exit()
                        else:
                            menu_help(sudahlogin=False,userdatabase=None)
                elif actionchoice == "2":
                    arrayidmonstershop, arraymonsterstock, arraymonsterprice, arraypotiontype, arraypotionstock, arraypotionprice = shop_management(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True,userdatabase=userdatabase)
                elif actionchoice == "3":
                    arrayidmonster,arraytypemonster,arrayatkpower,arraydefpower,arrayhpmonster,gambarmonster = monster_management(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True,userdatabase=userdatabase)
            elif userdatabase[3] == "agent":
                print(f"Halo Agent {userdatabase[1]} Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. \nBerikut adalah hal-hal yang dapat kamu lakukan sekarang: ")
                print("1. Logout : Keluar dari akun yang sedang digunakan.\n2. Inventory : Melihat owca-dex yang dimiliki oleh Agent.\n3. Shop : Melakukan pembelian potion/monster di dalam game.\n4. Laboratory : Melakukan peningkatan level pada monster.\n5. Battle : Memulai pertarungan melawan monster Dr. Asep Spakbor.\n6. Arena : Melakukan pelatihan monster dengan pertarungan 5 stage.")
                arraypilihan = ['1','2','3','4','5','6']
                actionchoice = input(">>> Pilih yang mau kamu lakukan : ")
                while actionchoice not in arraypilihan:
                    actionchoice = input(">>> Pilihan kamu tidak valid, pilih yang mau kamu lakukan : ")
                if actionchoice == "1":
                    delay_print("Sebelum anda logout")
                    save_option = input("Apakah Anda ingin menyimpan hasil ke file CSV? (press y to save or any key to cancel save): ")
                    arrsaveopt = ['y','n','Y','N']
                    while save_option not in arrsaveopt:
                        save_option = input("Ulangi, Apakah Anda ingin menyimpan hasil ke file CSV? (press y to save or any key to cancel save): ")
                    if save_option.lower() == 'y':
                        folder_path = input("Masukkan nama folder untuk menyimpan file : ")
                        save(folder_path,userdict,monsterdict,monster_shopdict,monster_inventorydict,item_shopdict,item_inventorydict)
                        delay_print("Processing to log out...")
                        time.sleep(1)
                        print("Anda telah log out!")
                        exitornot = input("File anda sudah disimpan, apakah anda ingin keluar dari aplikasi? (press any key to continue or y to exit app) : ")
                        if exitornot.lower() == 'y':
                            exit()
                        else:
                            menu_help(sudahlogin=False,userdatabase=None)
                    else:
                        delay_print("Data tidak jadi disimpan....")
                        delay_print("Processing to log out...")
                        time.sleep(1)
                        print("Anda telah log out!")
                        exitornot = input("apakah anda ingin keluar dari aplikasi? (press any key to continue or y to exit app) : ")
                        if exitornot.lower() == 'y':
                            exit()
                        else:
                            menu_help(sudahlogin=False,userdatabase=None)
                elif actionchoice == "2":
                    arrayidmonsterbaru,arraylevelmonsterbaru,arraytypemonsterbaru,arrayhpmonsterbaru,arraypotiontypebaru,arraypotionqtybaru,arrayatkpowerbaru,arraydefpowerbaru = inventory(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True, userdatabase=userdatabase)
                elif actionchoice == "3":
                    userdatabase,arrayuseridMinv,arrayidmonsterMinv,arraymonsterlevel,arrayuseridIinv,arraytypeIinv,arrayqtyIinv,arraymonsterstock,arraypotionstock,arrayuseroc = shop_currency(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True, userdatabase=userdatabase)
                elif actionchoice == "4":
                    arraymonsterlevel,arrayuseroc = laboratory(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True, userdatabase=userdatabase)
                elif actionchoice == "5":
                    battle(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv,levelmusuh=None,ocreceived=None)
                    menu_help(sudahlogin=True, userdatabase=userdatabase)
                elif actionchoice == "6":
                    arena(userdatabase,arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                    menu_help(sudahlogin=True, userdatabase=userdatabase)
        else: # Kalau Belum Login
            delay_print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
            print("1. Login : Masuk ke akun yang sudah terdaftar.\n2. Register: Membuat akun baru")
            print("Footnote : \n1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar. \n2. Jangan lupa untuk memasukkan input yang valid. ")
            arraypilihan = ['1','2']
            actionchoice = input(">>> Pilih yang mau kamu lakukan : ")
            while actionchoice not in arraypilihan:
                actionchoice = input(">>> Pilihan kamu tidak valid, pilih yang mau kamu lakukan : ")
            if actionchoice == "1":
                sudahlogin, userdatabase = login(arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                menu_help(sudahlogin=True, userdatabase=userdatabase) 
            elif actionchoice == "2":
                sudahregis, newuserdatabase, monster_choice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arrayuserid, arrayusername, arraypassword, arrayuserrole, arrayuseroc,arraytypeIinv,arrayqtyIinv,arrayuseridIinv = register(arrayusername, arraypassword, arrayuserid, arrayuserrole, arrayuseroc, arrayatkpower, arrayidmonster, arraytypemonster, arraydefpower, arrayhpmonster, arrayidmonstershop, arraymonsterstock, arraymonsterprice, arrayuseridMinv, arrayidmonsterMinv, arraymonsterlevel, arraypotiontype, arraypotionstock, arraypotionprice, arrayuseridIinv, arraytypeIinv, arrayqtyIinv)
                sudahregis = True
                userdatabase = newuserdatabase
                menu_help(sudahlogin=sudahregis,userdatabase=userdatabase)  
    else:
        print("Input anda salah, masukkan command 'help' yang benar")
        if sudahlogin == True:
            menu_help(sudahlogin=True,userdatabase=userdatabase)
        elif sudahlogin == False:
            menu_help(sudahlogin=False,userdatabase=None)
# Pemanggilan fungsi menu&help untuk menjalankan semua fungsi
menu_help(sudahlogin=False,userdatabase=None)