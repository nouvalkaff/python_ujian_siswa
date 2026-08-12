from colorama import Fore, Style
from config import TINGKAT_SD, DIR_PATH_IDN, PILIHAN_BAHASA, DIR_PATH_ENG


class BankSoal:
    def __init__(self) -> None:
        self.daftar_soal = []
        self.pilihan_bahasa = ""

    def _pilih_bahasa(self) -> str:
        print("Silakan pilih bahasa pengantar / Please select your preferred language:")
        print("1. Bahasa Indonesia (ID)")
        print("2. English (EN)")
        while True:
            input_bahasa = input("Input: ")
            if input_bahasa not in PILIHAN_BAHASA:
                print(
                    f"{Fore.YELLOW}Input tidak valid! Pilih 1 atau 2 / Invalid input! Choose 1 or 2.{Style.RESET_ALL}"
                )
                continue

            if input_bahasa == "1":
                print("\nAnda memilih Bahasa Indonesia.")
            else:
                print("\nYou selected English.")

            self.pilihan_bahasa = "ind" if input_bahasa == "1" else "eng"
            return self.pilihan_bahasa

    def ambil_soal(self) -> None:
        bahasa = self._pilih_bahasa()

        try:
            if bahasa == "ind":
                with open(f"{DIR_PATH_IDN}_{self._ambil_tingkat()}.txt", "r") as file:
                    self.daftar_soal = [soal.strip() for soal in file if soal.strip()]
            else:
                with open(
                    f"{DIR_PATH_ENG}_{self._ambil_tingkat_eng()}.txt", "r"
                ) as file:
                    self.daftar_soal = [soal.strip() for soal in file if soal.strip()]
        except FileNotFoundError:
            msg = (
                "Bank soal untuk tingkat ini tidak tersedia."
                if bahasa == "ind"
                else "The question bank for this grade is not available."
            )
            print(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}")
            self.daftar_soal = []

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

    @staticmethod
    def _ambil_tingkat_eng() -> str:
        print("Select questions for elementary school grade:")
        print("1. Grade 1")
        print("2. Grade 2")
        print("3. Grade 3")
        print("4. Grade 4")
        print("5. Grade 5")
        print("6. Grade 6")

        while True:
            tingkat_dipilih = input("\nEnter grade level: ")

            if tingkat_dipilih not in TINGKAT_SD:
                print(
                    f"{Fore.YELLOW}Invalid grade level. Choose one: 1, 2, 3, 4, 5, or 6.{Style.RESET_ALL}"
                )
                continue

            print(
                f"{Fore.CYAN}You are working on grade {tingkat_dipilih} questions.{Style.RESET_ALL}\n"
            )

            return tingkat_dipilih
