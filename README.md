
# Z_Wifi

### WIFI_SCANNER - NETWORK DISCOVERY

**Pengembang:** ZAnony Scarela  
**Versi:** 1.0.0  
**Bahasa Pemrograman:** Python  
**Lisensi:** Belum ditentukan

---

## Tentang Proyek

Z_Wifi merupakan aplikasi berbasis Python yang dirancang untuk membantu pengguna melakukan pemindaian, analisis, dan penemuan informasi jaringan WiFi melalui antarmuka terminal.

Proyek ini dikembangkan menggunakan struktur modular agar mudah dipelajari, dikembangkan, dan diperluas ke berbagai sistem operasi.

Z_Wifi memiliki visi menjadi aplikasi Network Discovery lintas platform yang dapat digunakan pada Android, Linux, macOS, dan Windows.

---

## Fitur Utama

### 1. Pemindaian WiFi
Menampilkan jaringan WiFi yang terdeteksi di sekitar perangkat.

### 2. Analisis Kekuatan Sinyal
Menganalisis kekuatan sinyal WiFi berdasarkan nilai RSSI.

### 3. Informasi Channel
Menampilkan informasi channel dan frekuensi jaringan WiFi.

### 4. Informasi Jaringan
Menampilkan informasi koneksi jaringan yang sedang digunakan.

### 5. Riwayat Pemindaian
Menyimpan dan menampilkan hasil pemindaian sebelumnya.

### 6. Deteksi Perangkat
Membantu menemukan perangkat yang terdeteksi pada jaringan lokal menggunakan Nmap.

### 7. Animasi Loading
Memberikan tampilan proses yang lebih interaktif melalui animasi terminal.

---

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

## Instalasi Android / Termux

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

Instal dependensi Python:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Aplikasi

Unduh proyek:

```bash
git clone https://github.com/USERNAME/Z_Wifi.git
```

Masuk ke direktori:

```bash
cd Z_Wifi
```

Jalankan aplikasi:

```bash
python main.py
```

Ganti USERNAME dengan nama pengguna GitHub pemilik repositori.

---

## Struktur Proyek

```text
Z_Wifi/
├── core/
│   ├── banner.py
│   ├── engine.py
│   └── menu.py
├── modules/
│   ├── wifi_scan.py
│   ├── signal.py
│   ├── channel.py
│   ├── network_info.py
│   ├── history.py
│   └── device_discovery.py
├── config/
│   └── settings.py
├── utils/
│   ├── colors.py
│   ├── helpers.py
│   └── animation.py
├── reports/
├── main.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── .gitignore
```

---

## Keamanan dan Penggunaan

Z_Wifi dikembangkan untuk kebutuhan pembelajaran dan pemeriksaan jaringan yang sah.

- Gunakan hanya pada jaringan milik sendiri atau jaringan yang telah mendapatkan izin.
- Fitur deteksi perangkat ditujukan untuk jaringan lokal yang diizinkan.
- Beberapa informasi jaringan mungkin dibatasi oleh sistem operasi.
- Riwayat pemindaian dapat berisi informasi jaringan pribadi. Jangan membagikan laporan tersebut secara publik.

---

## Pengembang

**ZAnony Scarela**

Proyek: Z_Wifi  
Versi: 1.0.0  
Kategori: Network Discovery Tool

---

## Kontribusi

Pengembangan Z_Wifi masih berlangsung.

Saran, laporan kesalahan, dan kontribusi pengembangan sangat terbuka untuk membantu meningkatkan kualitas proyek ini.

---

## Lisensi

## Lisensi

Proyek Z_Wifi menggunakan lisensi MIT.

Bebas digunakan, dimodifikasi, dan didistribusikan
sesuai ketentuan MIT License.

Copyright (c) 2026 ZAnony Scarela
