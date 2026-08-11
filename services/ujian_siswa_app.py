import random
import streamlit as st

from services.ujian_siswa_cli import UjianSiswa
from repositories.bank_soal_app import BankSoalApp
from models.soal_app import SoalApp
from config import JUMLAH_SOAL


class UjianSiswaApp:
    def __init__(self) -> None:
        self.soal_list = []
        self.index = 0
        self.jumlah_benar = 0
        self.selesai = False
        self.sudah_jawab = False
        self.jumlah_soal_real = JUMLAH_SOAL

    def siapkan_sesi(self, tingkat: str):
        bank_soal_app = BankSoalApp()
        raw = bank_soal_app.ambil_soal(tingkat)

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

    def _hitung_nilai(self) -> tuple[int, str]:
        nilai = int((self.jumlah_benar / self.jumlah_soal_real) * 100)

        if nilai <= 50:
            pesan = "Ayo semangat belajar lagi ya! 💪"
        elif nilai <= 70:
            pesan = "Lumayan! Sedikit lagi bisa lebih baik."
        elif nilai <= 85:
            pesan = "Bagus! Kamu sudah paham banyak nih."
        elif nilai <= 95:
            pesan = "Keren banget! Kamu pintar sekali! 🌟"
        else:  # 96-100
            pesan = "Luar biasa! Nilai sempurna, kamu juara! 🎉🏆"

        return nilai, pesan

    def tampilkan_hasil_web(self):
        nilai, pesan = self._hitung_nilai()

        st.subheader(f"Nilai akhir: {nilai}")
        st.write(f"Jawaban benar: {self.jumlah_benar}/{self.jumlah_soal_real}")
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

        if st.button("Ulangi dari awal"):
            for k in ["soal_list", "index", "jumlah_benar", "selesai", "sudah_jawab"]:
                st.session_state.pop(k, None)
            st.rerun()
