# 📝 Ujian Siswa v1.1

Aplikasi berbasis Command Line (CLI) yang dibuat menggunakan Python untuk membantu siswa SD (kelas 1–6) berlatih mengerjakan soal pilihan ganda. Soal dan pilihan jawaban akan diacak secara otomatis, kemudian sistem akan menghitung nilai akhir berdasarkan jawaban yang benar.

---

## ✨ Fitur

- 🎓 Pilihan tingkat kelas (1–6 SD)
- 🎲 Mengacak urutan soal
- 🔀 Mengacak urutan pilihan jawaban
- ✅ Penilaian otomatis
- 📊 Menghitung nilai akhir beserta pesan motivasi
- 📁 Bank soal mudah ditambahkan atau diubah
- 🖥️ Ringan dan berjalan melalui Command Line (CLI)
- 🐳 Mendukung menjalankan aplikasi via Docker

---

## 📂 Struktur Proyek

```text
.
├── main.py
├── functions.py
├── bank_soal_sd_1.txt
├── bank_soal_sd_2.txt
├── bank_soal_sd_3.txt
├── bank_soal_sd_4.txt
├── bank_soal_sd_5.txt
├── bank_soal_sd_6.txt
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📦 Persyaratan

Pastikan telah menginstal:

- Python 3.10 atau lebih baru
- Library `colorama`

Install library menggunakan perintah berikut:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Menjalankan

### Menjalankan Secara Lokal

Jalankan aplikasi menggunakan perintah berikut:

```bash
python main.py
```

Setelah aplikasi berjalan, pilih tingkat kelas (1–6) sesuai bank soal yang tersedia. Setiap sesi terdiri atas 10 soal pilihan ganda yang diacak secara otomatis.

### Menjalankan dengan Docker

Build image:

```bash
docker build -t ujian-siswa .
```

Jalankan container (mode interaktif diperlukan karena aplikasi berbasis input CLI):

```bash
docker run -it --rm ujian-siswa
```

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

> **Catatan:**
> Jawaban pertama akan dianggap sebagai jawaban yang benar. Saat aplikasi dijalankan, seluruh pilihan jawaban akan diacak secara otomatis. Nama file bank soal mengikuti pola `bank_soal_sd_<tingkat>.txt`, di mana `<tingkat>` adalah angka 1 sampai 6.

---

## 💻 Contoh Penggunaan

```text
Pilih soal untuk siswa SD kelas:
1. Kelas 1
2. Kelas 2
3. Kelas 3
4. Kelas 4
5. Kelas 5
6. Kelas 6

Masukkan tingkat kelas: 1
Siap! Kamu akan mengerjakan soal kelas 1

1. Soal: 2 + 3 = ?
Pilihan Ganda:
a. 6
b. 5
c. 4
d. 7

Jawabanmu: b
Jawaban benar.
```

Hasil akhir:

```text
Jumlah jawaban benar : 9/10
Nilai akhir kamu : 90
Keren banget! Kamu pintar sekali! 🌟
```

---

## ⚙️ Kustomisasi

Aplikasi dapat dengan mudah disesuaikan sesuai kebutuhan, seperti:

- Menambah bank soal baru untuk tingkat kelas lain
- Mengubah isi pertanyaan
- Mengganti pilihan jawaban
- Mengatur jumlah soal yang ditampilkan (`JUMLAH_SOAL` pada `functions.py`)
- Membuat soal untuk berbagai mata pelajaran atau topik

Contoh penggunaan:

- Matematika
- Bahasa Indonesia
- Bahasa Inggris
- IPA
- IPS
- Pengetahuan Umum
- Soal sejarah Indonesia
- Soal informasi teknologi

---

## 🛠️ Dibuat Menggunakan

- Python
- Colorama
- Docker

---

## 👨‍💻 Pengembang

**Mohamad Nouval Abdel A**

Proyek ini dikembangkan sebagai media pembelajaran dan latihan pemrograman Python, dengan fokus pada pembuatan aplikasi Command Line (CLI) yang sederhana, mudah dipahami, dan mudah dikembangkan.

Terima kasih telah berkunjung. Semoga bermanfaat!
