from colorama import Fore, Style
from random import shuffle

from models.soal_cli import Soal
from config import JUMLAH_SOAL, PILIHAN_GANDA
from services.nilai import evaluasi_nilai, evaluate_score


class UjianSiswa:
    def __init__(self, soal_raw: list[str], bahasa: str):
        self.soal_raw = soal_raw
        self.bahasa = bahasa
        self.jawaban_benar = 0

    def proses_soal(self):
        shuffle(self.soal_raw)

        jumlah_soal = min(JUMLAH_SOAL, len(self.soal_raw))

        if jumlah_soal == 0:
            message = (
                "Bank soal kosong, tidak bisa memulai ujian."
                if self.bahasa == "idn"
                else "Question bank is empty, cannot start the exam."
            )
            print(f"{Fore.RED}{message}{Style.RESET_ALL}")
            return

        for i in range(jumlah_soal):
            soal_jawaban = self.soal_raw[i].split("|")
            soal_mentah = soal_jawaban[0]
            kumpulan_jawaban = soal_jawaban[1].split("#")

            is_bahasa_idn = self.bahasa == "idn"

            msg_1 = "Soal:" if is_bahasa_idn else "Question:"
            msg_1 = f"{i+1}. {msg_1} {soal_mentah} ?"
            print(msg_1)

            msg_2 = "Pilihan Ganda:" if is_bahasa_idn else "Options:"
            print(msg_2)

            soal = Soal(soal_mentah, kumpulan_jawaban)
            soal.tampilkan_soal()
            hasil_jawab = self._proses_jawab(soal)
            self.jawaban_benar += 1 if hasil_jawab else 0

        self._tampilkan_hasil(self.jawaban_benar, jumlah_soal)

    @staticmethod
    def _warna_untuk_nilai(nilai: int) -> str:
        if nilai <= 50:
            return Fore.RED
        elif nilai <= 70:
            return Fore.YELLOW
        elif nilai <= 85:
            return Fore.CYAN
        elif nilai <= 96:
            return Fore.GREEN
        else:
            return Fore.LIGHTGREEN_EX

    def _tampilkan_hasil(self, jumlah_benar: int, jumlah_soal: int):
        nilai = int((jumlah_benar / jumlah_soal) * 100)
        is_bahasa_ind = self.bahasa == "ind"

        pesan = evaluasi_nilai(nilai) if is_bahasa_ind else evaluate_score(nilai)
        warna = self._warna_untuk_nilai(nilai)

        total_msg = (
            "Jumlah jawaban benar" if is_bahasa_ind else "Total correct answer(s)"
        )
        print(f"\n{total_msg}: {jumlah_benar}/{jumlah_soal}")

        score_msg = "Nilai akhir kamu" if is_bahasa_ind else "Your final score"
        print(f"{warna}{score_msg}: {nilai}{Style.RESET_ALL}")
        print(f"{warna}{pesan}{Style.RESET_ALL}")

    def _proses_jawab(self, soal: Soal):
        while True:
            is_bahasa_ind = self.bahasa == "ind"
            input_msg = "Jawabanmu" if is_bahasa_ind else "Your answer"

            jawaban_user = input(f"\n{input_msg}: ").strip().lower()

            if jawaban_user not in PILIHAN_GANDA:
                msg = (
                    "Jawaban tidak valid! Ketik salah satu huruf: a, b, c, atau d."
                    if is_bahasa_ind
                    else "Invalid answer! Enter one of the letters: a, b, c, or d."
                )

                print(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}")
                continue
            elif soal.cek_jawaban(jawaban_user):
                correct_msg = "Jawaban benar." if is_bahasa_ind else "Correct!"

                print(f"{Fore.GREEN}{correct_msg}{Style.RESET_ALL}\n")
                return True
            else:
                wrong_msg = "Jawaban salah." if is_bahasa_ind else "Wrong!"
                print(f"{Fore.RED}{wrong_msg}{Style.RESET_ALL}")

                correction = (
                    "Jawaban yang benar adalah"
                    if is_bahasa_ind
                    else "The correct answer is"
                )

                print(f"{correction} '{soal.jawaban_benar}'\n")
                return False
