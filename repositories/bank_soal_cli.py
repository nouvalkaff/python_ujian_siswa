from colorama import Fore, Style
from config import TINGKAT_SD, DIR_PATH_ID


class BankSoal:
    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self) -> None:
        with open(f"{DIR_PATH_ID}_{BankSoal._ambil_tingkat()}.txt", "r") as file:
            self.daftar_soal = [soal.strip() for soal in file if soal.strip()]

    @staticmethod
    def _ambil_tingkat() -> str:
        print("Pilih soal untuk siswa SD kelas: ")
        print("1. Kelas 1")
        print("2. Kelas 2")
        print("3. Kelas 3")
        print("4. Kelas 4")
        print("5. Kelas 5")
        print("6. Kelas 6")

        while True:
            tingkat_dipilih = input("\nMasukkan tingkat kelas: ")

            if tingkat_dipilih not in TINGKAT_SD:
                print(
                    f"{Fore.YELLOW}Tingkat SD tidak valid. Ketik salah satu: 1, 2, 3, 4, 5, atau 6.{Style.RESET_ALL}"
                )
                continue

            print(
                f"{Fore.CYAN}Kamu mengerjakan soal kelas {tingkat_dipilih}{Style.RESET_ALL}\n"
            )

            return tingkat_dipilih
