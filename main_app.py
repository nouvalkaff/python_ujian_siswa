import streamlit as st

from services.ujian_siswa_app import UjianSiswaApp
from config import TINGKAT_SD


def main():
    st.title("📝 Ujian Siswa SD")

    ujian_siswa_app = UjianSiswaApp()

    if "jumlah_soal_real" in st.session_state:
        ujian_siswa_app.jumlah_soal_real = st.session_state.jumlah_soal_real

    if "soal_list" not in st.session_state:
        st.write("Pilih tingkat kelas untuk mulai latihan soal.")
        tingkat = st.selectbox("Kelas", TINGKAT_SD, format_func=lambda t: f"Kelas {t}")
        if st.button("Mulai"):
            if ujian_siswa_app.siapkan_sesi(tingkat):
                st.rerun()
            else:
                st.warning("Bank soal untuk kelas ini kosong. Pilih kelas lain.")

    elif st.session_state.selesai:
        ujian_siswa_app.jumlah_benar = st.session_state.jumlah_benar
        ujian_siswa_app.tampilkan_hasil_web()

    else:
        i = st.session_state.index
        soal = st.session_state.soal_list[i]

        st.progress(i / ujian_siswa_app.jumlah_soal_real)
        st.write(f"Soal {i + 1}/{ujian_siswa_app.jumlah_soal_real}")
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
                soal["jawaban_user"] = pilihan
                if pilihan == soal["jawaban_benar"]:
                    st.session_state.jumlah_benar += 1
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
                if st.session_state.index >= ujian_siswa_app.jumlah_soal_real:
                    st.session_state.selesai = True
                st.rerun()


if __name__ == "__main__":
    main()
