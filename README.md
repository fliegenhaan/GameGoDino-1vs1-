# 🦖 GameGoDino-1vs1 🦖

## About
Game ini merupakan versi terbaru dari sebuah project yang sebelumnya dibuat oleh kelompok tugas besar Dasar Pemrograman IF1210 2024 K10-C. Program ini adalah sebuah game berbasis bahasa pemrograman Python yang mewajibkan pengguna untuk login ke akun mereka atau membuat akun jika tidak memiliki akun. Setelah login, pengguna dapat membeli monster dan item lainnya, meng-upgrade level monster, serta bertarung dengan monster lainnya. Semua perubahan yang terjadi dalam game disimpan dan data-data dalam game diakses dari file CSV yang berada dalam folder tertentu. Program ini melibatkan beberapa fungsi utama seperti autentikasi pengguna (dalam fungsi register, login, logout), pengelolaan inventori monster dan potion, pertarungan antar monster, dan pengaksesan serta penyimpanan data.

## 🔄 About Latest Version
Pada repositori ini semua fungsi yang tadinya terpisah digabung dalam satu file bernama `Main.py`. Pada file tersebut sudah diperbaiki beberapa bug yang sebelumnya belum diperbaiki terkait penempatan elemen array serta tipe variabel yang masih tidak sesuai. Pada repositori ini juga akan terus di-update jika sewaktu-waktu developer/user menemukan bug.

## 👥 Contributors
**Assistant:**

- 13521024 - Ahmad Nadil

**Students (K10-C):**

- 19623309 - Muhammad Raihaan Perdana
- 19623299 - Sebastian Enrico Nathanael
- 19623249 - Raka Daffa Iftikhaar
- 19623169 - Audy Alicia Renatha Tirayoh
- 16523089 - Firda Dian Yudha Az Zahra

## 🌟 Features
- 🎲 **Random Number Generator:** Memanggil bilangan acak menggunakan algoritma Linear Congruential Generator
- 📝 **Register:** Registrasi sebuah akun yang baru
- 🔐 **Login:** Masuk ke akun yang sudah terdata di database
- 🚪 **Logout:** Keluar dari akun yang sudah ter-login sebelumnya
- 🐲 **Monster:** Entitas di dalam program yang memiliki atribut serta identitas sendiri yang dipertarungkan oleh user pada battle/arena
- 🧪 **Potion:** Entitas di dalam program yang membantu meningkatkan atribut dari Monster
- 📋 **Menu and Help:** Halaman utama berisi apa saja yang dapat dilakukan di dalam program
- 🎒 **Inventory:** Halaman yang berisi item (monster/potion) yang dimiliki oleh sebuah akun
- ⚔️ **Battle:** Tempat monster yang dimiliki oleh user di dalam akun bertarung melawan monster yang ada di database yang dipanggil secara random menggunakan RNG
- 🏟️ **Arena:** Tempat pelatihan monster yang berisi 5 stage dengan mekanisme pertarungan pada tiap stage sama dengan battle
- 🛒 **Shop and Currency:** Tempat jual beli item (monster/potion) di dalam program
- 🧬 **Laboratory:** Tempat meng-upgrade level dari monster yang dimiliki oleh pengguna
- 🛍️ **Shop Management:** Tempat bagi admin untuk mengatur item (monster/potion) yang dijual di shop
- 📊 **Monster Management:** Tempat bagi admin untuk mengatur spesifikasi monster yang ada pada database
- 📂 **Load:** Fungsi yang dipanggil pada awal berjalannya program untuk memanggil data-data berupa file CSV yang akan digunakan selama program berjalan
- 💾 **Save:** Fungsi yang dapat digunakan untuk menyimpan segala perubahan yang terjadi selama berjalannya program dalam bentuk CSV
- 🚪 **Exit:** Fungsi yang dapat dipanggil ketika ingin keluar dari program

## 🚀 How to Run
1. Jalankan file pada terminal
2. Masukkan format berupa `python {nama file python}.py {nama folder csv}`
3. Setelah loading data selesai, ketik 'help' untuk menampilkan aksi yang dapat dilakukan
4. Untuk melakukan setiap pilihan aksi yang ada di program, ketik angka yang mewakili aksi pada pilihan di menu & help
5. Setelah menjalankan setiap aksi, selalu ketik 'help' untuk kembali menampilkan aksi dan melakukan aksi lainnya
