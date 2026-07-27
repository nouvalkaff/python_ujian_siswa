# Ujian Siswa - versi Web (Streamlit)
# Semua logic inti (baca soal, parse soal, acak opsi, hitung nilai)
# dipakai langsung dari functions.py — bukan ditulis ulang.
import random
import streamlit as st

from functions_app import (
    ambil_soal,
    parse_soal,
    acak_opsi,
    hitung_nilai,
    JUMLAH_SOAL,
    TINGKAT_SD,
)

st.set_page_config(page_title="Ujian Siswa", page_icon="📝")


def siapkan_sesi(tingkat: str):
    raw = ambil_soal(tingkat)  # functions.py
    random.shuffle(raw)
    dipilih = raw[:JUMLAH_SOAL]

    soal_list = []
    for baris in dipilih:
        pertanyaan, opsi, jawaban_benar = parse_soal(baris)  # functions.py
        soal_list.append(
            {
                "pertanyaan": pertanyaan,
                "opsi": acak_opsi(opsi),  # functions.py
                "jawaban_benar": jawaban_benar,
            }
        )

    st.session_state.soal_list = soal_list
    st.session_state.index = 0
    st.session_state.skor = 0
    st.session_state.selesai = False
    st.session_state.sudah_jawab = False


def tampilkan_hasil_web(skor: int):
    nilai, pesan = hitung_nilai(skor)  # functions.py — logic sama persis kayak CLI

    st.subheader(f"Nilai akhir: {nilai}")
    st.write(f"Jawaban benar: {skor}/{JUMLAH_SOAL}")
    st.success(pesan)
    if st.button("Ulangi dari awal"):
        for k in ["soal_list", "index", "skor", "selesai", "sudah_jawab"]:
            st.session_state.pop(k, None)
        st.rerun()


st.title("📝 Ujian Siswa SD")

if "soal_list" not in st.session_state:
    st.write("Pilih tingkat kelas untuk mulai latihan soal.")
    tingkat = st.selectbox("Kelas", TINGKAT_SD, format_func=lambda t: f"Kelas {t}")
    if st.button("Mulai"):
        siapkan_sesi(tingkat)
        st.rerun()

elif st.session_state.selesai:
    tampilkan_hasil_web(st.session_state.skor)

else:
    i = st.session_state.index
    soal = st.session_state.soal_list[i]

    st.progress(i / JUMLAH_SOAL)
    st.write(f"Soal {i + 1}/{JUMLAH_SOAL}")
    st.subheader(soal["pertanyaan"])

    pilihan = st.radio(
        "Pilih jawaban:",
        soal["opsi"],
        index=None,
        key=f"pilihan_{i}",
        disabled=st.session_state.sudah_jawab,
    )

    if not st.session_state.sudah_jawab:
        if st.button("Jawab", disabled=pilihan is None):
            st.session_state.sudah_jawab = True
            if pilihan == soal["jawaban_benar"]:
                st.session_state.skor += 1
                st.session_state.feedback = ("benar", None)
            else:
                st.session_state.feedback = ("salah", soal["jawaban_benar"])
            st.rerun()
    else:
        status, jawaban_benar = st.session_state.feedback
        if status == "benar":
            st.success("Jawaban benar! 🎉")
        else:
            st.error(f"Jawaban salah. Jawaban yang benar: {jawaban_benar}")

        if st.button("Lanjut"):
            st.session_state.index += 1
            st.session_state.sudah_jawab = False
            if st.session_state.index >= JUMLAH_SOAL:
                st.session_state.selesai = True
            st.rerun()
