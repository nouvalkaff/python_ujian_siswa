import streamlit as st

from services.ujian_siswa_app import UjianSiswaApp
from config import TINGKAT_SD, PILIHAN_BAHASA

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
        "wrong": "Jawaban salah. Jawaban yang benar:",
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
        "wrong": "Incorrect answer. The correct answer is:",
        "empty": "The question bank for this grade is empty. Choose another grade.",
    },
}


def main():
    try:
        if "bahasa" not in st.session_state:
            bahasa = st.selectbox(
                "Bahasa / Language",
                PILIHAN_BAHASA,
                format_func=lambda x: ("Bahasa Indonesia" if x == "1" else "English"),
            )

            text = TEXT[bahasa]

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
            bahasa = st.session_state.bahasa
            text = TEXT[bahasa]

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
                    status, jawaban_benar = st.session_state.feedback

                    if status == "benar":
                        st.success(text["correct"])
                    else:
                        st.error(f"{text['wrong']} " f"**{jawaban_benar}**")

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
