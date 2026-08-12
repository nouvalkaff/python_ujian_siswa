# 📝 Student Exam v2.1

A multiple-choice practice quiz application for elementary school students (grades 1–6), available in two versions: **CLI** (Command Line) and **Web** (Streamlit).

The application provides randomized multiple-choice questions, automatic grading, score calculation, motivational feedback, and multilingual question banks in **Bahasa Indonesia and English**.

---

## ✨ Features

- 🎓 Grade level selection for elementary grades 1–6
- 🌐 **Multilingual question banks**
  - 🇮🇩 Bahasa Indonesia
  - 🇬🇧 English

- 🎲 Randomized question order
- 🔀 Randomized answer choice order
- ✅ Automatic grading
- 📊 Automatic final score calculation
- 💬 Motivational feedback based on the final score
- 🔒 Answers are locked after submission in the Web version
- 📁 Question banks are stored as editable `.txt` files
- 🖥️ CLI version — lightweight and terminal-based
- 🌐 Web version — interactive browser UI using Streamlit
- 🐳 Docker support for both CLI and Web versions
- 📉 Automatically adjusts the number of questions when fewer questions are available
- 🛡️ Handles empty question banks without crashing

---

## 🆕 What's New in v2.1

### Multilingual Question Banks

Version **2.1** introduces English question banks alongside the existing Indonesian question banks.

Question banks are now separated by language:

```text
assets/
└── question_bank/
    ├── ind/
    └── eng/
```

The CLI version supports selecting the preferred question-bank language before starting the exam.

English question banks are available for grades 1–6 and use the following naming convention:

```text
primary_question_bank_1.txt
primary_question_bank_2.txt
primary_question_bank_3.txt
primary_question_bank_4.txt
primary_question_bank_5.txt
primary_question_bank_6.txt
```

The Indonesian question banks remain:

```text
bank_soal_sd_1.txt
bank_soal_sd_2.txt
bank_soal_sd_3.txt
bank_soal_sd_4.txt
bank_soal_sd_5.txt
bank_soal_sd_6.txt
```

The language-specific paths are centralized in `config.py`:

```python
DIR_PATH_IDN = "./assets/question_bank/ind/bank_soal_sd"
DIR_PATH_ENG = "./assets/question_bank/eng/primary_question_bank"
```

---

## 📚 Question Bank Content

The question banks cover elementary-school subjects and topics including:

- Math
- Indonesian Language
- English
- Science
- Social Studies
- General Knowledge
- Indonesian History
- IT / Computing

The English question banks are designed for elementary students from Grade 1 through Grade 6, with increasing difficulty across grade levels.

---

## 📂 Project Structure

```text
.
├── main.py                         # CLI version entry point
├── streamlit_app.py                # Web version entry point
├── config.py                       # Shared application constants
│
├── models/
│   ├── soal_cli.py                 # Question model — CLI
│   └── soal_app.py                 # Question model — Web
│
├── repositories/
│   ├── bank_soal_cli.py            # Question-bank repository — CLI
│   └── bank_soal_app.py            # Question-bank repository — Web
│
├── services/
│   ├── ujian_siswa_cli.py          # Exam service — CLI
│   ├── ujian_siswa_app.py          # Exam service — Web
│   └── nilai.py                    # Shared scoring and feedback logic
│
├── assets/
│   └── question_bank/
│       ├── ind/
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
├── .devcontainer/
├── .vscode/
└── README.md
```

The project follows an OOP-oriented structure:

- `models/` — domain models for questions
- `repositories/` — question-bank data access
- `services/` — exam flow, scoring, and feedback
- `config.py` — shared configuration and question-bank paths

The CLI and Web implementations use separate classes so they can be developed and customized independently.

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

The CLI guides the user through the exam setup, including language and grade selection.

The available languages are:

```text
1. Bahasa Indonesia
2. English
```

After selecting a language, choose a grade from:

```text
1. Grade 1
2. Grade 2
3. Grade 3
4. Grade 4
5. Grade 5
6. Grade 6
```

The application then loads the corresponding language- and grade-specific question bank.

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

The Web version allows students to:

1. Select a preferred language (Bahasa Indonesia / English)
2. Select a grade level
3. Start the quiz
4. Answer multiple-choice questions
5. Receive feedback after submitting an answer
6. Continue to the next question
7. View the final score

Like the CLI version, the Web version supports both Bahasa Indonesia and English question banks.

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

Then access:

```text
http://localhost:8501
```

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with your GitHub account.
4. Create a new app.
5. Select this repository.
6. Select the `main` branch.
7. Set the main file to:

```text
streamlit_app.py
```

8. Deploy the application.

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

### Correct Answer

The **first answer after `|` is always treated as the correct answer**.

For example:

```text
What is 5 + 3?|8#7#9#6
```

The correct answer is:

```text
8
```

The application then shuffles all four answer choices before displaying them to the student.

---

## 📁 Question Bank Naming Convention

### Indonesian

Location:

```text
assets/question_bank/ind/
```

Filename:

```text
bank_soal_sd_<grade>.txt
```

Example:

```text
bank_soal_sd_1.txt
bank_soal_sd_2.txt
bank_soal_sd_3.txt
bank_soal_sd_4.txt
bank_soal_sd_5.txt
bank_soal_sd_6.txt
```

### English

Location:

```text
assets/question_bank/eng/
```

Filename:

```text
primary_question_bank_<grade>.txt
```

Example:

```text
primary_question_bank_1.txt
primary_question_bank_2.txt
primary_question_bank_3.txt
primary_question_bank_4.txt
primary_question_bank_5.txt
primary_question_bank_6.txt
```

The `<grade>` value represents the elementary-school grade from **1 to 6**.

---

## 📊 Question Selection and Scoring

The default number of questions per exam session is configured in `config.py`:

```python
JUMLAH_SOAL = 10
```

The application automatically adjusts the number of questions based on the number of questions available in the selected question bank.

For example:

```text
Configured questions: 10
Available questions:   7
Actual questions:      7
```

If the selected question bank is empty, the application displays a warning instead of crashing.

The final score is calculated automatically based on the number of correct answers.

---

## 🔀 Randomization

The application automatically randomizes:

1. Question order
2. Answer-choice order

This means the correct answer is not always displayed in the same position.

For example, a question stored as:

```text
2 + 3 =|5#4#6#7
```

may be displayed as:

```text
a. 6
b. 5
c. 7
d. 4
```

The original question-bank order does not determine the displayed answer position.

---

## ⚙️ Customization

### Add or Edit Questions

Question banks can be edited directly as `.txt` files inside:

```text
assets/question_bank/
```

Use the appropriate language directory:

```text
assets/question_bank/
├── ind/
└── eng/
```

### Change the Number of Questions

Edit `JUMLAH_SOAL` in `config.py`:

```python
JUMLAH_SOAL = 10
```

This configuration is shared by the application.

### Add New Question Banks

Follow the existing naming convention for the selected language and grade.

Indonesian:

```text
bank_soal_sd_<grade>.txt
```

English:

```text
primary_question_bank_<grade>.txt
```

### Add Questions for Different Subjects

The question-bank format can be used for various elementary-school subjects, including:

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

- **Python** — application development
- **Streamlit** — Web interface
- **Colorama** — CLI terminal styling
- **Docker** — containerization

---

## 🎯 Project Goals

This project started as a simple Python command-line quiz and gradually evolved into an OOP-based application with separate CLI and Web implementations.

The project focuses on practicing:

- Python OOP
- Classes and objects
- Repository and service separation
- File-based data management
- Randomized multiple-choice questions
- Automatic grading
- Application configuration
- Multilingual question-bank management
- Streamlit application development
- Docker containerization

## 👨‍💻 Developer

**Mohamad Nouval Abdel A**

Built as a Python learning and practice project, evolving from a simple Command Line quiz into an interactive Web application using Streamlit, with OOP architecture, multilingual question banks, automatic grading, and Docker support.

Thanks for visiting. Hope it helps!
