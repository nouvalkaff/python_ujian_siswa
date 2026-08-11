# 📝 Student Exam v2.0

A multiple-choice practice quiz application for elementary school students (grades 1–6), available in two versions: **CLI** (Command Line) and **Web** (Streamlit).

The application supports **Bahasa Indonesia and English question banks**, automatically shuffles questions and answer choices, calculates the final score, and provides motivational feedback.

---

## ✨ Features

- 🎓 Grade level selection for elementary grades 1–6
- 🌐 **Language selection in CLI**
  - 🇮🇩 Bahasa Indonesia
  - 🇬🇧 English

- 🎲 Randomized question order
- 🔀 Randomized answer choice order
- ✅ Automatic grading
- 📊 Automatic final score calculation
- 💬 Motivational feedback based on the final score
- 🔒 Answers are locked after submission in the Web version
- 📁 Easy-to-edit question banks
- 🖥️ CLI version — lightweight and terminal-based
- 🌐 Web version — interactive browser interface using Streamlit
- 🐳 Docker support for both CLI and Web versions
- 🛡️ Handles empty question banks without crashing
- 📉 Automatically adjusts the number of questions when fewer questions are available

---

## 📂 Project Structure

```text
.
├── main.py                         # CLI version entry point
├── streamlit_app.py                # Web version entry point
├── config.py                       # Shared application constants
│
├── models/
│   ├── soal_cli.py                 # Question domain model — CLI
│   └── soal_app.py                 # Question domain model — Web
│
├── repositories/
│   ├── bank_soal_cli.py            # Loads question banks — CLI
│   └── bank_soal_app.py            # Loads question banks — Web
│
├── services/
│   ├── ujian_siswa_cli.py          # Exam session logic — CLI
│   ├── ujian_siswa_app.py          # Exam session logic — Web
│   └── nilai.py                    # Shared scoring and feedback logic
│
├── assets/
│   └── question_bank/
│       ├── idn/
│       │   ├── bank_soal_sd_1.txt
│       │   ├── bank_soal_sd_2.txt
│       │   ├── bank_soal_sd_3.txt
│       │   ├── bank_soal_sd_4.txt
│       │   ├── bank_soal_sd_5.txt
│       │   └── bank_soal_sd_6.txt
│       │
│       └── eng/
│           ├── primary_question_bank_1.txt
│           ├── primary_question_bank_2.txt
│           ├── primary_question_bank_3.txt
│           ├── primary_question_bank_4.txt
│           ├── primary_question_bank_5.txt
│           └── primary_question_bank_6.txt
│
├── requirements.txt                # CLI dependencies
├── requirements_app.txt            # Web dependencies
├── Dockerfile                      # CLI Docker image
├── Dockerfile_app                  # Web Docker image
├── .gitignore
├── .dockerignore
└── README.md
```

The project uses an OOP structure with separate implementations for the CLI and Web versions:

- `models/` — question/domain models
- `repositories/` — question-bank loading and data access
- `services/` — exam flow, scoring, and feedback
- `config.py` — shared configuration and paths

The CLI and Web versions use separate `_cli` and `_app` modules so they can be developed and customized independently.

---

## 🌐 Language Support

The application currently provides two question-bank languages:

| Language         | Directory                   | Filename pattern                    |
| ---------------- | --------------------------- | ----------------------------------- |
| Bahasa Indonesia | `assets/question_bank/idn/` | `bank_soal_sd_<grade>.txt`          |
| English          | `assets/question_bank/eng/` | `primary_question_bank_<grade>.txt` |

### English Question Banks

The English question banks are designed around **Cambridge Primary-style learning progression** for elementary grades 1–6.

The question banks cover subjects such as:

- Math
- Indonesian Language
- English
- Science
- Social Studies
- General Knowledge
- Indonesian History
- IT / Computing

The English question banks are named according to the grade:

```text
primary_question_bank_1.txt
primary_question_bank_2.txt
primary_question_bank_3.txt
primary_question_bank_4.txt
primary_question_bank_5.txt
primary_question_bank_6.txt
```

> The English question banks use English for the question text, while Indonesian Language and Indonesian History questions may test Indonesian-specific vocabulary, language, culture, and history.

---

## 📦 Requirements

- Python 3.10 or newer
- `colorama` for the CLI version
- `streamlit` for the Web version
- Docker (optional)

---

## 🚀 How to Run — CLI Version

### Local

Install the CLI dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The CLI will ask you to select:

1. Language
2. Grade level

For example:

```text
Silakan pilih bahasa pengantar / Please select your preferred language:
1. Bahasa Indonesia (ID)
2. English (EN)

Input: 2

You selected English.

Select questions for elementary school grade:
1. Grade 1
2. Grade 2
3. Grade 3
4. Grade 4
5. Grade 5
6. Grade 6

Enter grade level: 3
```

The application then loads the corresponding question bank.

---

### Docker

Build the CLI image:

```bash
docker build -t ujian-siswa -f Dockerfile .
```

Run the container:

```bash
docker run -it --rm ujian-siswa
```

Interactive mode (`-it`) is required because the CLI application uses terminal input.

---

## 🌐 How to Run — Web Version

### Local

Install the Web dependencies:

```bash
pip install -r requirements_app.txt
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

The application will be available at:

```text
http://localhost:8501
```

The Web version allows users to:

1. Select a grade level
2. Start the quiz
3. Answer multiple-choice questions
4. Receive immediate answer feedback
5. Continue through the remaining questions
6. View the final score and answer review

The number of questions automatically adjusts to the number of available questions in the selected question bank.

---

### Docker

Build the Web image:

```bash
docker build -t ujian-siswa-web -f Dockerfile_app .
```

Run the container:

```bash
docker run -p 8501:8501 --rm ujian-siswa-web
```

Then open:

```text
http://localhost:8501
```

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with your GitHub account.
4. Create a new app.
5. Select this repository and the `main` branch.
6. Set the main file to:

```text
streamlit_app.py
```

7. Deploy the application.

---

## 📝 Question Bank Format

Each question must be written on a single line using this format:

```text
Question|Correct Answer#Wrong Answer#Wrong Answer#Wrong Answer
```

Example:

```text
2 + 3 =|5#4#6#7
```

The format consists of:

```text
Question | Correct Answer # Wrong Answer # Wrong Answer # Wrong Answer
```

### Important

The **first answer after `|` is always treated as the correct answer**.

For example:

```text
What is 5 + 3?|8#7#9#6
```

The correct answer is:

```text
8
```

The application then shuffles all four answer choices before presenting them to the student.

### Question Bank Naming

Indonesian:

```text
bank_soal_sd_<grade>.txt
```

Example:

```text
bank_soal_sd_1.txt
bank_soal_sd_2.txt
```

English:

```text
primary_question_bank_<grade>.txt
```

Example:

```text
primary_question_bank_1.txt
primary_question_bank_2.txt
```

Where `<grade>` is a number from `1` to `6`.

---

## 📊 Question Selection and Scoring

The default number of questions per session is configured in `config.py`:

```python
JUMLAH_SOAL = 10
```

The application does not require every question bank to contain exactly 10 questions.

If a question bank contains fewer questions than the configured amount, the application automatically uses the number of questions actually available.

For example:

```text
JUMLAH_SOAL = 10
Available questions = 7
Actual questions = 7
```

If the selected question bank is empty, the application displays a warning instead of crashing.

---

## 💻 Usage Example

### CLI

```text
Silakan pilih bahasa pengantar / Please select your preferred language:
1. Bahasa Indonesia (ID)
2. English (EN)

Input: 1

Anda memilih Bahasa Indonesia.

Pilih soal untuk siswa SD kelas:
1. Kelas 1
2. Kelas 2
3. Kelas 3
4. Kelas 4
5. Kelas 5
6. Kelas 6

Masukkan tingkat kelas: 1

Kamu mengerjakan soal kelas 1
```

A question is then presented with four shuffled choices:

```text
1. Soal: 2 + 3 = ?

Pilihan Ganda:
a. 6
b. 5
c. 4
d. 7

Jawabanmu: b

Jawaban benar.
```

Example final result:

```text
Jumlah jawaban benar : 9/10
Nilai akhir kamu : 90

Keren banget! Kamu pintar sekali! 🌟
```

The exact feedback message depends on the student's score and selected language.

---

## ⚙️ Customization

### Add or Edit Question Banks

Question banks are stored under:

```text
assets/question_bank/
```

Separate them by language:

```text
assets/question_bank/
├── idn/
└── eng/
```

Add or edit the corresponding grade-level `.txt` file.

### Change the Number of Questions

Edit `JUMLAH_SOAL` in `config.py`:

```python
JUMLAH_SOAL = 10
```

Both CLI and Web versions use this shared configuration.

### Add New Subjects or Topics

The question-bank format is intentionally simple, so it can be used for different subjects and topics, including:

- Math
- Indonesian Language
- English
- Science
- Social Studies
- General Knowledge
- Indonesian History
- IT / Computing

---

## 🛠️ Built With

- Python
- Streamlit
- Colorama
- Docker

---

## 🎯 Project Goals

This project was built as a Python learning project and gradually evolved from a simple command-line quiz into an OOP-based application with:

- CLI and Web versions
- Multiple language support
- Structured question-bank management
- Randomized questions and answer choices
- Automatic scoring
- Localized feedback
- Docker support
- Separate application layers using models, repositories, and services

The project is primarily intended for **learning, experimentation, and practicing Python application development**.

---

## 👨‍💻 Developer

**Mohamad Nouval Abdel A**

Built as a Python practice project, evolving from a simple Command Line quiz application into an interactive Web application using Streamlit, with OOP architecture, multilingual question banks, and Docker support.

Thanks for visiting. Hope it helps!
