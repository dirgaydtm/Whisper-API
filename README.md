# Faster Whisper API

API sederhana untuk melakukan transkripsi audio menggunakan [Faster Whisper](https://github.com/guillaumekln/faster-whisper) dan Flask.

## Fitur

- Endpoint `/transcribe` untuk mengunggah file audio (MP3) dan mendapatkan hasil transkripsi beserta deteksi bahasa.
- Endpoint `/` untuk pengecekan status API.

## Cara Menjalankan

1. **Instalasi Dependensi**

   Pastikan Python dan pip sudah terpasang. Jalankan perintah berikut untuk menginstal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

2. **Menjalankan Server**

   Jalankan aplikasi dengan perintah:

   ```bash
   python app.py
   ```

   Server akan berjalan di `http://0.0.0.0:5000`.

## Penggunaan API

### 1. Transkripsi Audio

- **Endpoint:** `POST /transcribe`
- **Form Data:**
  - `file`: File audio (format MP3)
- **Response:**
  ```json
  {
    "language": "id",
    "text": "Hasil transkripsi audio"
  }
  ```

### 2. Cek Status API

- **Endpoint:** `GET /`
- **Response:**
  ```json
  {
    "message": "Faster Whisper API is running"
  }
  ```

## Catatan

- File audio yang diunggah akan disimpan sementara dan dihapus setelah proses transkripsi selesai.
- Model Faster Whisper yang digunakan adalah versi "base" dan berjalan di CPU.
- Untuk model lain, ubah variabel `model_size` di `app.py`.
