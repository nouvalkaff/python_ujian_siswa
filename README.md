# 📝 Ujian Siswa v2.0

Aplikasi latihan soal pilihan ganda untuk siswa SD (kelas 1–6), tersedia dalam dua versi: **CLI** (Command Line) dan **Web** (Streamlit). Soal dan pilihan jawaban diacak otomatis, sistem menghitung nilai akhir beserta pesan motivasi.

---

## ✨ Fitur

- 🎓 Pilihan tingkat kelas (1–6 SD)
- 🎲 Mengacak urutan soal
- 🔀 Mengacak urutan pilihan jawaban
- ✅ Penilaian otomatis
- 📊 Menghitung nilai akhir beserta pesan motivasi
- 🔒 Jawaban terkunci setelah disubmit (versi web)
- 📁 Bank soal mudah ditambahkan atau diubah
- 🖥️ Versi CLI — ringan, jalan lewat terminal
- 🌐 Versi Web — tampilan interaktif via browser (Streamlit)
- 🐳 Mendukung deployment via Docker (kedua versi)

---

## 📂 Struktur Proyek

```text
.
├── main.py                  # Entry point versi CLI
├── functions.py             # Logic versi CLI
├── streamlit_app.py         # Entry point versi Web
├── functions_app.py         # Logic versi Web
├── assets/
│   ├── bank_soal_sd_1.txt
│   ├── bank_soal_sd_2.txt
│   ├── bank_soal_sd_3.txt
│   ├── bank_soal_sd_4.txt
│   ├── bank_soal_sd_5.txt
│   └── bank_soal_sd_6.txt
├── requirements.txt         # Dependency versi CLI
├── requirements_app.txt     # Dependency versi Web
├── Dockerfile                # Docker image versi CLI
├── Dockerfile_app            # Docker image versi Web
├── .gitignore
├── .dockerignore
└── README.md
```

> Versi CLI dan Web sengaja dipisah filenya (termasuk `functions.py` vs `functions_app.py`) supaya masing-masing bisa dikembangkan/dikustomisasi independen tanpa saling mempengaruhi.

---

## 📦 Persyaratan

- Python 3.10 atau lebih baru
- Untuk versi CLI: library `colorama`
- Untuk versi Web: library `streamlit`

---

## 🚀 Cara Menjalankan — Versi CLI

### Lokal

```bash
pip install -r requirements.txt
python main.py
```

Pilih tingkat kelas (1–6), lalu kerjakan 10 soal pilihan ganda yang diacak otomatis.

### Docker

```bash
docker build -t ujian-siswa -f Dockerfile .
docker run -it --rm ujian-siswa
```

Mode interaktif (`-it`) diperlukan karena aplikasi berbasis input terminal.

---

## 🌐 Cara Menjalankan — Versi Web

### Lokal

```bash
pip install -r requirements_app.txt
streamlit run streamlit_app.py
```

Browser otomatis terbuka ke `http://localhost:8501`.

### Docker

```bash
docker build -t ujian-siswa-web -f Dockerfile_app .
docker run -p 8501:8501 --rm ujian-siswa-web
```

Akses lewat `http://localhost:8501`.

### Deploy ke Streamlit Community Cloud

1. Push repository ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io), login dengan akun GitHub
3. Klik **New app** → pilih repo, branch `main`, main file `streamlit_app.py`
4. Klik **Deploy**

---

## 📝 Format Bank Soal

Setiap soal ditulis dalam satu baris dengan format berikut:

```text
Pertanyaan|Jawaban Benar,Jawaban Salah,Jawaban Salah,Jawaban Salah
```

Contoh:

```text
2 + 3 =|5,4,6,7
```

> **Catatan:** Jawaban pertama dianggap sebagai jawaban benar. Seluruh pilihan jawaban diacak otomatis saat aplikasi berjalan. Nama file bank soal mengikuti pola `bank_soal_sd_<tingkat>.txt` di dalam folder `assets/`, di mana `<tingkat>` adalah angka 1–6.

---

## ⚙️ Kustomisasi

- Menambah bank soal baru untuk tingkat kelas lain (taruh di `assets/`)
- Mengubah isi pertanyaan atau pilihan jawaban
- Mengatur jumlah soal per sesi (`JUMLAH_SOAL` di `functions.py` / `functions_app.py`)
- Membuat soal untuk mata pelajaran atau topik lain (Matematika, Bahasa Indonesia, Bahasa Inggris, IPA, IPS, dsb.)

---

## 🛠️ Dibuat Menggunakan

- Python
- Streamlit
- Colorama
- Docker

---

## 👨‍💻 Pengembang

**Mohamad Nouval Abdel A**

Proyek ini dikembangkan sebagai media pembelajaran dan latihan pemrograman Python, dari aplikasi Command Line (CLI) sederhana hingga versi Web interaktif menggunakan Streamlit.

Terima kasih telah berkunjung. Semoga bermanfaat!