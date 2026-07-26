# 📝 Ujian Siswa v1.1

Aplikasi berbasis Command Line (CLI) yang dibuat menggunakan Python untuk membantu siswa berlatih mengerjakan soal pilihan ganda. Soal dan pilihan jawaban akan diacak secara otomatis, kemudian sistem akan menghitung nilai akhir berdasarkan jawaban yang benar.

---

## ✨ Fitur

- 🎲 Mengacak urutan soal
- 🔀 Mengacak urutan pilihan jawaban
- ✅ Penilaian otomatis
- 📊 Menghitung nilai akhir
- 📁 Bank soal mudah ditambahkan atau diubah
- 🖥️ Ringan dan berjalan melalui Command Line (CLI)

---

## 📂 Struktur Proyek

```text
.
├── main.py
├── functions.py
├── bank_soal_sd_1.txt
├── bank_soal_sd_2.txt
├── bank_soal_sd_3.txt
├── bank_soal_fadil_jaidi.txt
└── README.md
```

---

## 📦 Persyaratan

Pastikan telah menginstal:

- Python 3.10 atau lebih baru
- Library `colorama`

Install library menggunakan perintah berikut:

```bash
pip install colorama
```

---

## 🚀 Cara Menjalankan

Jalankan aplikasi menggunakan perintah berikut:

```bash
python main.py
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
> Jawaban pertama akan dianggap sebagai jawaban yang benar. Saat aplikasi dijalankan, seluruh pilihan jawaban akan diacak secara otomatis.

---

## 💻 Contoh Penggunaan

```text
1. Soal: 2 + 3 = ?

Pilihan Ganda:
a. 6
b. 5
c. 4
d. 7

Jawabanmu: b

Jawabanmu benar.
```

Hasil akhir:

```text
Selamat nilai akhir kamu: 90
```

---

## ⚙️ Kustomisasi

Aplikasi dapat dengan mudah disesuaikan sesuai kebutuhan, seperti:

- Menambah bank soal baru
- Mengubah isi pertanyaan
- Mengganti pilihan jawaban
- Mengatur jumlah soal yang ditampilkan
- Membuat soal untuk berbagai mata pelajaran atau topik

Contoh penggunaan:

- Matematika
- Bahasa Indonesia
- Bahasa Inggris
- IPA
- IPS
- Pengetahuan Umum
- Soal latihan sekolah
- Soal ujian perusahaan

---

## 🛠️ Dibuat Menggunakan

- Python
- Colorama

---

## 👨‍💻 Pengembang

**Mohamad Nouval Abdel A**

Proyek ini dikembangkan sebagai media pembelajaran dan latihan pemrograman Python, dengan fokus pada pembuatan aplikasi Command Line (CLI) yang sederhana, mudah dipahami, dan mudah dikembangkan.

Terima kasih telah berkunjung. Semoga bermanfaat!