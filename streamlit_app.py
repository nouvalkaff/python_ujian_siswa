import streamlit as st

from services.ujian_siswa_app import UjianSiswaApp
from config import TINGKAT_SD, PILIHAN_BAHASA

RADIO_CSS = """
    <style>
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        gap: 8px;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background-color: #1c1f26;
        border: 1px solid #3a3f4b;
        border-radius: 8px;
        padding: 10px 14px;
        width: 100%;
        transition: border-color 0.15s ease, background-color 0.15s ease;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        border-color: #7a8194;
        background-color: #22262e;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
        background-color: #2a2e37 !important;
        border: 2px solid #7a8194 !important;
        width: 20px !important;
        height: 20px !important;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] div[aria-checked="true"] > div:first-child,
    div[data-testid="stRadio"] input:checked + div {
        border-color: #e63946 !important;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child > div {
        background-color: #e63946 !important;
    }
    </style>
"""

TEXT = {
    "1": {
        "title": "📝 Ujian Siswa SD",
        "instruction": "Pilih tingkat kelas untuk mulai latihan soal.",
        "class": "Kelas",
        "start": "Mulai",
        "question": "Soal",
        "answer": "Pilih jawaban:",
        "submit": "Jawab",
        "next": "Lanjut",
        "correct": "Jawaban benar! 🎉",
        "wrong": "Jawaban salah.",
        "empty": "Bank soal untuk kelas ini kosong. Pilih kelas lain.",
    },
    "2": {
        "title": "📝 Elementary Student Exam",
        "instruction": "Choose a grade to start the practice quiz.",
        "class": "Grade",
        "start": "Start",
        "question": "Question",
        "answer": "Choose an answer:",
        "submit": "Submit",
        "next": "Next",
        "correct": "Correct answer! 🎉",
        "wrong": "Incorrect answer.",
        "empty": "The question bank for this grade is empty. Choose another grade.",
    },
}


def main():
    st.markdown(RADIO_CSS, unsafe_allow_html=True)
    try:
        # Step 1: Language selection — standalone page
        if "bahasa" not in st.session_state:
            st.title("🌐 Bahasa / Language")
            st.write("Pilih bahasa pengantar / Select your preferred language")

            bahasa_dipilih = st.selectbox(
                "Bahasa / Language",
                PILIHAN_BAHASA,
                format_func=lambda x: ("Bahasa Indonesia" if x == "1" else "English"),
            )

            lanjut = "Lanjut" if bahasa_dipilih == "1" else "Next"

            if st.button(lanjut):
                st.session_state.bahasa = bahasa_dipilih
                st.rerun()

            return

        bahasa = st.session_state.bahasa
        text = TEXT[bahasa]

        # Step 2: Grade selection — separate page, shown after language is confirmed
        if "soal_list" not in st.session_state:
            st.title(text["title"])
            st.write(text["instruction"])

            tingkat = st.selectbox(
                text["class"],
                TINGKAT_SD,
                format_func=lambda t: (f"Kelas {t}" if bahasa == "1" else f"Grade {t}"),
            )

            if st.button(text["start"]):
                ujian_siswa_app = UjianSiswaApp()

                if ujian_siswa_app.siapkan_sesi(tingkat, bahasa):
                    st.rerun()
                else:
                    st.warning(text["empty"])

        else:
            ujian_siswa_app = UjianSiswaApp()

            if "jumlah_soal_real" in st.session_state:
                ujian_siswa_app.jumlah_soal_real = st.session_state.jumlah_soal_real

            if st.session_state.selesai:
                ujian_siswa_app.bahasa = bahasa
                ujian_siswa_app.jumlah_benar = st.session_state.jumlah_benar
                ujian_siswa_app.tampilkan_hasil_web()

            else:
                i = st.session_state.index
                soal = st.session_state.soal_list[i]

                st.title(text["title"])

                st.progress(i / ujian_siswa_app.jumlah_soal_real)

                st.write(
                    f"{text['question']} " f"{i + 1}/{ujian_siswa_app.jumlah_soal_real}"
                )

                st.subheader(soal["pertanyaan"])

                pilihan = st.radio(
                    text["answer"],
                    soal["opsi"],
                    index=None,
                    key=f"pilihan_{i}",
                    disabled=st.session_state.sudah_jawab,
                    format_func=lambda opt: f"{chr(65 + soal['opsi'].index(opt))}. {opt}",
                )

                if not st.session_state.sudah_jawab:
                    if st.button(
                        text["submit"],
                        disabled=pilihan is None,
                    ):
                        st.session_state.sudah_jawab = True
                        soal["jawaban_user"] = pilihan

                        if pilihan == soal["jawaban_benar"]:
                            st.session_state.jumlah_benar += 1
                            st.session_state.feedback = (
                                "benar",
                                None,
                            )
                        else:
                            st.session_state.feedback = (
                                "salah",
                                soal["jawaban_benar"],
                            )

                        st.rerun()

                else:
                    status, _ = st.session_state.feedback

                    if status == "benar":
                        st.success(text["correct"])
                    else:
                        st.error(text["wrong"])

                    if st.button(text["next"]):
                        st.session_state.index += 1
                        st.session_state.sudah_jawab = False

                        if st.session_state.index >= ujian_siswa_app.jumlah_soal_real:
                            st.session_state.selesai = True

                        st.rerun()

    except Exception as e:
        st.error(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
