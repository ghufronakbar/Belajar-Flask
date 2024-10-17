Berikut adalah README yang sesuai untuk proyek Flask + MySQL dan Flask + Session:

# FLASK + MYSQL + SESSION

## Deskripsi Proyek

Ini adalah aplikasi web sederhana yang dibangun menggunakan Flask (framework Python) dan MySQL sebagai database. Aplikasi ini mendukung login menggunakan sesi (session) untuk mengelola autentikasi pengguna. Setelah login, pengguna dapat melihat daftar pengguna lain dan detail setiap pengguna, serta halaman tentang aplikasi.

## Requirements

Pastikan Anda memiliki perangkat berikut sebelum memulai:

- **MySQL Server** atau **XAMPP** (untuk menjalankan server MySQL secara lokal)
- **Python** (pastikan Python sudah diinstal di komputer Anda)
- **Flask** (framework Python untuk pengembangan web)
- **flask-mysqldb** (untuk koneksi Flask ke MySQL)
- **XAMPP** (opsional, jika Anda menggunakan MySQL lokal)

## Instalasi

### 1. Install Library yang Dibutuhkan

Jalankan perintah berikut untuk menginstal dependensi yang diperlukan:

```bash
pip install flask flask-mysqldb
```

### 2. Setup MySQL

Buat database MySQL baru untuk aplikasi ini. Misalnya, Anda dapat membuat database dengan nama `my-flask-app`:

```sql
CREATE DATABASE `my-flask-app`;
```

Kemudian buat tabel `users`:

```sql
CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);
```

Masukkan beberapa data awal ke tabel:

```sql
INSERT INTO `users` (`username`, `email`, `password`) VALUES
('admin', 'admin@example.com', 'password123');
```

### 3. Konfigurasi Flask

Di file Python, pastikan konfigurasi Flask untuk koneksi MySQL telah diatur:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'my-flask-app'
app.secret_key = 's3cr3t'
```

### 4. Jalankan Aplikasi

Setelah semua langkah di atas selesai, jalankan aplikasi Flask:

```bash
python app.py
```

## Fitur

- **Login & Logout**: Pengguna dapat login menggunakan email dan password yang tersimpan di database MySQL. Informasi login disimpan dalam session.
- **List Pengguna**: Setelah login, pengguna dapat melihat semua pengguna yang terdaftar di database.
- **Detail Pengguna**: Pengguna dapat melihat detail pengguna lain.
- **Session**: Aplikasi ini menggunakan Flask Session untuk mengelola autentikasi pengguna. Setelah login, session menyimpan informasi login hingga pengguna logout.

## Struktur Aplikasi

```
- app.py
- templates/
    - login.html
    - index.html
    - user.html
    - about.html
```

## Endpoint

1. **`/`** - Halaman login.
2. **`/users`** - Menampilkan semua pengguna (hanya bisa diakses jika sudah login).
3. **`/users/<user_id>`** - Menampilkan detail pengguna berdasarkan ID.
4. **`/about`** - Halaman tentang aplikasi.
5. **`/logout`** - Keluar dari aplikasi.

## Contoh Penggunaan

1. **Login**: Masukkan email dan password, kemudian klik login. Jika benar, akan diarahkan ke halaman daftar pengguna.
2. **Melihat Detail Pengguna**: Setelah login, klik nama pengguna untuk melihat detail lebih lanjut.
3. **Logout**: Klik logout untuk keluar dari aplikasi.

## Catatan

- **Keamanan**: Session disimpan secara lokal di sisi server dan dienkripsi menggunakan `secret_key`.
- **MySQL**: Pastikan MySQL berjalan di localhost dengan pengguna dan password yang benar.

Dengan README ini, pengguna dapat menginstal, mengonfigurasi, dan menjalankan aplikasi Flask + MySQL + Session.