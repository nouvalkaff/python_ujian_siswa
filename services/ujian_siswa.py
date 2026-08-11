from colorama import Fore, Style
from random import shuffle

from models.soal import Soal


class UjianSiswa:
    JUMLAH_SOAL = 10

    def __init__(self, soal_raw: list[str]):
        self.soal_raw = soal_raw
        self.jawaban_benar = 0

    def proses_soal(self):
        shuffle(self.soal_raw)
        self.jumlah_benar = 0

        for i in range(self.JUMLAH_SOAL):
            soal_mentah = self.soal_raw[i].split("|")

            print(f"{i+1}. Soal: {soal_mentah[0]} ?")
            print("Pilihan Ganda:")

            kumpulan_jawaban = soal_mentah[1].split("#")
            soal = Soal(soal_mentah[0], kumpulan_jawaban)

            jawaban_benar = soal.jawaban_benar

            soal_dict = soal.tampilkan_soal()
            hasil_jawab = self._proses_jawab(soal)

            if hasil_jawab == True:
                self.jumlah_benar += 1

        self._tampilkan_hasil(self.jumlah_benar)

    def _tampilkan_hasil(self, jumlah_benar: int):
        nilai = int((jumlah_benar / self.JUMLAH_SOAL) * 100)

        if nilai <= 50:
            warna = Fore.RED
            pesan = "Ayo semangat belajar lagi ya! 💪"

        elif nilai <= 70:
            warna = Fore.YELLOW
            pesan = "Lumayan! Sedikit lagi bisa lebih baik."

        elif nilai <= 85:
            warna = Fore.CYAN
            pesan = "Bagus! Kamu sudah paham banyak nih."

        elif nilai <= 95:
            warna = Fore.GREEN
            pesan = "Keren banget! Kamu pintar sekali! 🌟"

        else:  # 96-100
            warna = Fore.LIGHTGREEN_EX
            pesan = "Luar biasa! Nilai sempurna, kamu juara! 🎉🏆"

        print(f"\nJumlah jawaban benar : {jumlah_benar}/{self.JUMLAH_SOAL}")
        print(f"{warna}Nilai akhir kamu : {nilai}{Style.RESET_ALL}")
        print(f"{warna}{pesan}{Style.RESET_ALL}")

    def _proses_jawab(self, soal: Soal):
        while True:
            jawaban_user = input("\nJawabanmu: ").strip().lower()

            if jawaban_user not in Soal.PILIHAN_GANDA:
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
