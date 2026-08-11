from colorama import Fore, Style
from random import shuffle

from models.soal_cli import Soal
from config import JUMLAH_SOAL, PILIHAN_GANDA
from services.nilai import evaluasi_nilai


class UjianSiswa:
    def __init__(self, soal_raw: list[str]):
        self.soal_raw = soal_raw
        self.jawaban_benar = 0

    def proses_soal(self):
        shuffle(self.soal_raw)

        jumlah_soal = min(JUMLAH_SOAL, len(self.soal_raw))
        if jumlah_soal == 0:
            print(
                f"{Fore.RED}Bank soal kosong, tidak bisa memulai ujian.{Style.RESET_ALL}"
            )
            return
        for i in range(jumlah_soal):
            soal_jawaban = self.soal_raw[i].split("|")
            soal_mentah = soal_jawaban[0]
            kumpulan_jawaban = soal_jawaban[1].split("#")

            print(f"{i+1}. Soal: {soal_mentah} ?")
            print("Pilihan Ganda:")

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
        pesan = evaluasi_nilai(nilai)
        warna = self._warna_untuk_nilai(nilai)
        print(f"\nJumlah jawaban benar : {jumlah_benar}/{jumlah_soal}")
        print(f"{warna}Nilai akhir kamu : {nilai}{Style.RESET_ALL}")
        print(f"{warna}{pesan}{Style.RESET_ALL}")

    def _proses_jawab(self, soal: Soal):
        while True:
            jawaban_user = input("\nJawabanmu: ").strip().lower()

            if jawaban_user not in PILIHAN_GANDA:
                print(
                    f"{Fore.YELLOW}Jawaban tidak valid! Ketik salah satu huruf: a, b, c, atau d.{Style.RESET_ALL}"
                )
                continue
            elif soal.cek_jawaban(jawaban_user):
                print(f"{Fore.GREEN}Jawaban benar.{Style.RESET_ALL}\n")
                return True
            else:
                print(f"{Fore.RED}Jawaban salah.{Style.RESET_ALL}")
                print(f"Jawaban yang benar adalah '{soal.jawaban_benar}'\n")
                return False
