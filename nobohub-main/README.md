# Nobohub

Nobohub adalah platform yang dirancang untuk memfasilitasi kolaborasi dan berbagi ide antara kreator dan pengembang. Platform ini menyediakan ruang bagi pengguna untuk mengumpulkan, mengorganisir, dan mengembangkan ide-ide kreatif secara bersama-sama.

## Fitur

- **Pengumpulan Ide**: Kumpulkan dan simpan ide-ide Anda di satu tempat.
- **Kolaborasi**: Bekerja sama dengan pengguna lain untuk mengembangkan ide.
- **Manajemen Proyek**: Lacak perkembangan ide dari konsep hingga implementasi.
- **Antarmuka Ramah Pengguna**: Desain intuitif yang memudahkan navigasi dan penggunaan.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan Nobohub secara lokal:

1. **Kloning repositori**:

   ```bash
   git clone https://github.com/avezoor/nobohub.git
   cd nobohub
   ```

2. **Buat dan aktifkan virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Unix/macOS
   # atau
   env\Scripts\activate.bat  # Untuk Windows
   ```

3. **Instal dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi lingkungan**:

   Buat file `.env` di direktori root proyek dan tambahkan variabel lingkungan yang diperlukan. Contoh:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   ```

5. **Inisialisasi database**:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Jalankan aplikasi**:

   ```bash
   flask run
   ```

   Aplikasi akan berjalan di `http://127.0.0.1:5000/`.

## Dependensi

Pastikan Anda memiliki paket-paket berikut yang terdaftar dalam `requirements.txt`:

```
Flask
Flask-Migrate
Flask-SQLAlchemy
python-dotenv
```

Untuk memperbarui daftar dependensi, gunakan perintah:

```bash
pip freeze > requirements.txt
```

## Kontribusi

Kami menyambut kontribusi dari siapa pun. Untuk berkontribusi:

1. Fork repositori ini.
2. Buat branch baru untuk fitur atau perbaikan Anda (`git checkout -b fitur-baru`).
3. Lakukan commit perubahan Anda (`git commit -m 'Menambahkan fitur baru'`).
4. Push ke branch Anda (`git push origin fitur-baru`).
5. Buat Pull Request ke branch `main` dari repositori ini.

## Lisensi

Proyek ini dilisensikan di bawah [CC BY 4.0 License](LICENSE).



**Catatan:**

- **Konfigurasi Lingkungan**: Pastikan untuk mengganti `your_secret_key` dengan kunci rahasia yang aman. Variabel lingkungan lainnya dapat disesuaikan sesuai kebutuhan.

- **Inisialisasi Database**: Langkah-langkah inisialisasi database menggunakan Flask-Migrate. Pastikan Anda telah mengonfigurasi database dengan benar dalam aplikasi Anda.

- **Dependensi Tambahan**: Jika proyek Anda memerlukan paket tambahan, tambahkan ke file `requirements.txt` dan perbarui instruksi instalasi sesuai kebutuhan.

Dengan dokumentasi yang jelas, pengguna dan kontributor akan lebih mudah memahami dan berkontribusi pada proyek Anda. 