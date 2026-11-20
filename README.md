## Z_Wifi
Z_Wifi merupakan aplikasi berbasis Python yang dirancang untuk membantu pengguna melakukan pemindaian, analisis, dan penemuan informasi jaringan WiFi melalui antarmuka terminal.

Proyek ini dikembangkan menggunakan struktur modular agar mudah dipelajari, dikembangkan, dan diperluas ke berbagai sistem operasi.

Z_Wifi memiliki visi menjadi aplikasi Network Discovery lintas platform yang dapat digunakan pada Android, Linux, macOS, dan Windows.

---

## Fitur Utama
Menampilkan jaringan WiFi yang terdeteksi di sekitar perangkat.

Menganalisis kekuatan sinyal WiFi berdasarkan nilai RSSI.

Menampilkan informasi channel dan frekuensi jaringan WiFi.

Menampilkan informasi koneksi jaringan yang sedang digunakan.

Menyimpan dan menampilkan hasil pemindaian sebelumnya.

Membantu menemukan perangkat yang terdeteksi pada jaringan lokal menggunakan Nmap.

## Platform

Z_Wifi dirancang dengan tujuan mendukung berbagai sistem operasi.

| Sistem Operasi | Status |
|---|---|
| Android / Termux | Implementasi awal |
| Linux | Direncanakan |
| macOS | Direncanakan |
| Windows | Direncanakan |

Dukungan setiap platform bergantung pada ketersediaan perangkat keras, driver, izin, dan kemampuan sistem operasi.

---

## Persyaratan

- Python 3.
- Git.
- Colorama.
- Nmap untuk fitur deteksi perangkat.
- Termux:API untuk implementasi Android.

Catatan: Kebutuhan tambahan dapat berbeda pada setiap sistem operasi.

---

## Instalasi linux/macOS/Termux

Perbarui paket Termux:

```bash
pkg update && pkg upgrade -y
```

Instal kebutuhan sistem:

```bash
pkg install python git nmap -y
```

Instal Termux:API:

```bash
pkg install termux-api -y
```

Pasang aplikasi Termux:API Android dari sumber resmi dan berikan izin yang diperlukan.

```bash
git clone https://github.com/Zayd404/Z_Wifi.git
```

Instal dependensi Python:

```bash
pip install -r requirements.txt
```

```bash
cd Z_Wifi
```

```bash
python main.py
```

## Keamanan dan Penggunaan

Z_Wifi dikembangkan untuk kebutuhan pembelajaran dan pemeriksaan jaringan yang sah.

- Gunakan hanya pada jaringan milik sendiri atau jaringan yang telah mendapatkan izin.
- Fitur deteksi perangkat ditujukan untuk jaringan lokal yang diizinkan.
- Beberapa informasi jaringan mungkin dibatasi oleh sistem operasi.
- Riwayat pemindaian dapat berisi informasi jaringan pribadi. Jangan membagikan laporan tersebut secara publik.

---

## Kontribusi

Pengembangan Z_Wifi masih berlangsung.

Saran, laporan kesalahan, dan kontribusi pengembangan sangat terbuka untuk membantu meningkatkan kualitas proyek ini.

---

## Lisensi

Proyek Z_Wifi menggunakan lisensi MIT.

Bebas digunakan, dimodifikasi, dan didistribusikan
sesuai ketentuan MIT License.

Copyright (c) 2026 ZAnony Scarela
