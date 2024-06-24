# GameGoDino-1vs1-


# About
> Game ini merupakan versi terbaru dari sebuah project yang sebelumnya dibuat oleh kelompok tugas besar Dasar Pemrograman IF1210 2024 K10-C. Program ini adalah sebuah game berbasis bahasa pemrograman Python yang mewajibkan pengguna untuk login ke akun mereka atau membuat akun jika tidak memiliki akun. Setelah login, pengguna dapat membeli monster dan item lainnya, mengupgrade level monster, serta bertarung dengan monster lainnya. Semua perubahan yang terjadi dalam game disimpan dan data-data dalam game diakses dari file CSV yang berada dalam folder tertentu. Program ini melibatkan beberapa fungsi utama seperti autentikasi pengguna(dalam fungsi register,login,logout), pengelolaan inventori monster dan potion, pertarungan antar monster, dan pengaksesan dan penyimpanan data.
# About Latest Version
> Pada repositori ini semua fungsi yang tadinya terpisah digabung dalam satu file bernama Main.py. Pada file tersebut sudah diperbaiki beberapa bug yang sebelumnya belum diperbaiki terkait penempatan elemen array serta tipe variabel yang masih tidak sesuai. Pada repositori ini juga akan terus di-update jika sewaktu-waktu developer/user menemukan bug.
# Contributors
> Assistant:
> 1. 13521024 - Ahmad Nadil

> Students(K10-C):
> 1. 19623309 - Muhammad Raihaan Perdana
> 2. 19623299 - Sebastian Enrico Nathanael
> 3. 19623249 - Raka Daffa Iftikhaar
> 4. 19623169 - Audy Alicia Renatha Tirayoh
> 5. 16523089 - Firda Dian Yudha Az Zahra
# Features
> 1. Random Number Generator : Memanggil bilangan acak menggunakan algoritma Linear Congruential Generator
> 2. Register : Registrasi sebuah akun yang baru
> 3. Login : Masuk ke akun yang sudah terdata di database
> 4. Logout : Keluar dari akun yang sudah ter-login sebelumnya
> 5. Monster : Entitas di dalam program yang memiliki atribut serta identitas sendiri yang dipertarungkan oleh user pada battle/arena
> 6. Potion : Entitas di dalam program yang membantu meningkatkan atribut dari Monster
> 7. Menu and Help : Halaman utama berisi apa saja yang dapat dilakukan di dalam program
> 8. Inventory : Halaman yang berisi item(monster/potion) yang dimiliki oleh sebuah akun
> 9. Battle : Tempat monster yang dimiliki oleh user di dalam akun bertarung melawan monster yang ada di database yang dipanggil secara random menggunakan rng
> 10. Arena : Tempat pelatihan monster yang berisi 5 stage dengan mekanisme pertarungan pada tiap stage sama dengan battle
> 11. Shop and Currency : Tempat jual beli item(monster/potion) di dalam program
> 12. Laboratory : Tempat meng-upgrade level dari monster yang dimiliki oleh pengguna
> 13. Shop Management : Tempat bagi admin untuk mengatur item(monster/potion) yang dijual di shop
> 14. Monster Management : Tempat bagi admin untuk mengatur spesifikasi monster yang ada pada database
> 15. Load : Fungsi yang dipanggil pada awal berjalannya program untuk memanggil data-data berupa file CSV yang akan digunakan selama program berjalan
> 16. Save : Fungsi yang dapat digunakan untuk menyimpan segala perubahan yang terjadi selama berjalannya program dalam bentuk CSV
> 17. Exit : Fungsi yang dapat dipanggil ketika ingin keluar dari program
# How to Run
> 1. Jalankan file pada terminal
> 2. Masukkan format berupa "python {nama file python}.py {nama folder csv}"
> 3. Setelah loading data selesai, ketik 'help' untuk menampilkan aksi yang dapat dilakukan
> 4. Untuk melakukan setiap pilihan aksi yang ada di program, ketik angka yang mewakili aksi pada pilihan di menu&help
> 5. Setelah menjalankan setiap aksi, selalu ketik 'help' untuk kembali menampilkan aksi dan melakukan aksi lainnya.
