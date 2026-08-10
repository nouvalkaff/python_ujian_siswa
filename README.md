# 📝 Student Exam v2.0

Multiple-choice practice quiz app for elementary school students (grades 1–6), available in two versions: **CLI** (Command Line) and **Web** (Streamlit). Questions and answer choices shuffled automatically, system computes final score with a motivational message.

---

## ✨ Features

- 🎓 Grade level selection (elementary grades 1–6)
- 🎲 Randomized question order
- 🔀 Randomized answer choice order
- ✅ Automatic grading
- 📊 Final score calculation with motivational message
- 🔒 Answers locked after submit (web version)
- 📁 Question bank easy to add or edit
- 🖥️ CLI version — lightweight, runs in terminal
- 🌐 Web version — interactive browser UI (Streamlit)
- 🐳 Docker deployment support (both versions)

---

## 📂 Project Structure

```text
.
├── main.py                  # CLI version entry point
├── functions.py             # CLI version logic
├── streamlit_app.py         # Web version entry point
├── functions_app.py         # Web version logic
├── assets/
│   ├── bank_soal_sd_1.txt
│   ├── bank_soal_sd_2.txt
│   ├── bank_soal_sd_3.txt
│   ├── bank_soal_sd_4.txt
│   ├── bank_soal_sd_5.txt
│   └── bank_soal_sd_6.txt
├── requirements.txt         # CLI version dependencies
├── requirements_app.txt     # Web version dependencies
├── Dockerfile                # CLI version Docker image
├── Dockerfile_app            # Web version Docker image
├── .gitignore
├── .dockerignore
└── README.md
```

> CLI and Web versions deliberately kept in separate files (including `functions.py` vs `functions_app.py`) so each can be developed/customized independently without affecting the other.

---

## 📦 Requirements

- Python 3.10 or newer
- For CLI version: `colorama` library
- For Web version: `streamlit` library

---

## 🚀 How to Run — CLI Version

### Local

```bash
pip install -r requirements.txt
python main.py
```

Pick a grade level (1–6), then answer 10 auto-shuffled multiple-choice questions.

### Docker

```bash
docker build -t ujian-siswa -f Dockerfile .
docker run -it --rm ujian-siswa
```

Interactive mode (`-it`) required — app relies on terminal input.

---

## 🌐 How to Run — Web Version

### Local

```bash
pip install -r requirements_app.txt
streamlit run streamlit_app.py
```

Browser opens automatically to `http://localhost:8501`.

### Docker

```bash
docker build -t ujian-siswa-web -f Dockerfile_app .
docker run -p 8501:8501 --rm ujian-siswa-web
```

Access via `http://localhost:8501`.

### Deploy to Streamlit Community Cloud

1. Push repository to GitHub
2. Open [share.streamlit.io](https://share.streamlit.io), log in with GitHub account
3. Click **New app** → select repo, branch `main`, main file `streamlit_app.py`
4. Click **Deploy**

---

## 📝 Question Bank Format

Each question is written on one line using this format:

```text
Question|Correct Answer,Wrong Answer,Wrong Answer,Wrong Answer
```

Example:

```text
2 + 3 =|5,4,6,7
```

> **Note:**
> The first answer is treated as the correct one. When the app runs, all answer choices get shuffled automatically. Question bank filenames follow the pattern `bank_soal_sd_<grade>.txt`, where `<grade>` is a number 1–6.

---

## 💻 Usage Example

> Sample output below is in Indonesian — app's actual printed strings are Indonesian.

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

Final result:

```text
Jumlah jawaban benar : 9/10
Nilai akhir kamu : 90
Keren banget! Kamu pintar sekali! 🌟
```

---

## ⚙️ Customization

- Add new question banks for other grade levels (place in `assets/`)
- Edit question text or answer choices
- Adjust number of questions per session (`JUMLAH_SOAL` in `functions.py` / `functions_app.py`)
- Build questions for other subjects or topics (Math, Indonesian, English, Science, Social Studies, etc.)

Usage examples:

- Math
- Indonesian Language
- English
- Science
- Social Studies
- General Knowledge
- Indonesian history questions
- IT questions

---

## 🛠️ Built With

- Python
- Streamlit
- Colorama
- Docker

---

## 👨‍💻 Developer

**Mohamad Nouval Abdel A**

Built as a learning exercise and Python practice project, from a simple Command Line (CLI) app to an interactive Web version using Streamlit.

Thanks for visiting. Hope it helps!
