import random
import streamlit as st

from repositories.bank_soal_app import BankSoalApp
from models.soal_app import SoalApp
from config import JUMLAH_SOAL
from services.nilai import evaluasi_nilai, evaluate_score


class UjianSiswaApp:
    def __init__(self) -> None:
        self.soal_list = []
        self.index = 0
        self.jumlah_benar = 0
        self.selesai = False
        self.sudah_jawab = False
        self.jumlah_soal_real = JUMLAH_SOAL
        self.bahasa = "1"

    def siapkan_sesi(self, tingkat: str, bahasa: str) -> bool:
        self.bahasa = bahasa
        bank_soal_app = BankSoalApp()
        raw = bank_soal_app.ambil_soal(tingkat, bahasa)

        if not raw:
            return False

        random.shuffle(raw)
        self.jumlah_soal_real = min(self.jumlah_soal_real, len(raw))
        dipilih = raw[: self.jumlah_soal_real]

        for baris in dipilih:
            soal_obj = SoalApp(baris)
            pertanyaan, jawaban_benar = soal_obj.parse_soal()

            self.soal_list.append(
                {
                    "pertanyaan": pertanyaan,
                    "opsi": soal_obj.acak_opsi(),
                    "jawaban_benar": jawaban_benar,
                    "jawaban_user": None,
                }
            )

        st.session_state.soal_list = self.soal_list
        st.session_state.index = self.index
        st.session_state.jumlah_benar = self.jumlah_benar
        st.session_state.selesai = self.selesai
        st.session_state.sudah_jawab = self.sudah_jawab
        st.session_state.jumlah_soal_real = self.jumlah_soal_real
        st.session_state.bahasa = self.bahasa

        return True

    def _hitung_nilai(self) -> tuple[int, str]:
        nilai = int((self.jumlah_benar / self.jumlah_soal_real) * 100)

        if self.bahasa == "1":
            pesan = evaluasi_nilai(nilai)
        else:
            pesan = evaluate_score(nilai)

        return nilai, pesan

    def tampilkan_hasil_web(self):
        nilai, pesan = self._hitung_nilai()

        if self.bahasa == "1":
            st.subheader(f"Nilai akhir: {nilai}")
            st.write(f"Jawaban benar: " f"{self.jumlah_benar}/{self.jumlah_soal_real}")
            st.success(pesan)

            st.divider()
            st.subheader("Review Jawaban")

            for i, soal in enumerate(st.session_state.soal_list):
                benar = soal["jawaban_user"] == soal["jawaban_benar"]
                ikon = "✅" if benar else "❌"

                with st.expander(f"{ikon} Soal {i + 1}: {soal['pertanyaan']}"):
                    st.write(f"Jawabanmu: **{soal['jawaban_user']}**")

                    if not benar:
                        st.write(f"Jawaban benar: **{soal['jawaban_benar']}**")

        else:
            st.subheader(f"Final Score: {nilai}")
            st.write(
                f"Correct answers: " f"{self.jumlah_benar}/{self.jumlah_soal_real}"
            )
            st.success(pesan)

            st.divider()
            st.subheader("Answer Review")

            for i, soal in enumerate(st.session_state.soal_list):
                benar = soal["jawaban_user"] == soal["jawaban_benar"]
                ikon = "✅" if benar else "❌"

                with st.expander(f"{ikon} Question {i + 1}: {soal['pertanyaan']}"):
                    st.write(f"Your answer: **{soal['jawaban_user']}**")

                    if not benar:
                        st.write(f"Correct answer: **{soal['jawaban_benar']}**")

        if st.button("Ulangi dari awal" if self.bahasa == "1" else "Start Again"):
            for k in [
                "soal_list",
                "index",
                "jumlah_benar",
                "selesai",
                "sudah_jawab",
                "jumlah_soal_real",
                "feedback",
                "bahasa",
            ]:
                st.session_state.pop(k, None)

            st.rerun()
