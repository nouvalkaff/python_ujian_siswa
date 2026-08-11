from colorama import Fore, Style


class BankSoal:
    TINGKAT_SD = ["1", "2", "3", "4", "5", "6"]
    dir_path = "./assets/bank_soal/bank_soal_sd"

    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self) -> None:
        with open(f"{self.dir_path}_{BankSoal._ambil_tingkat()}.txt", "r") as file:
            self.daftar_soal = [soal.strip() for soal in file]

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

            if tingkat_dipilih not in BankSoal.TINGKAT_SD:
                print(
                    f"{Fore.YELLOW}Tingkat SD tidak valid. Ketik salah satu: 1, 2, 3, 4, 5, atau 6.{Style.RESET_ALL}"
                )
                continue

            print(
                f"{Fore.CYAN}Kamu mengerjakan soal kelas {tingkat_dipilih}{Style.RESET_ALL}\n"
            )

            return tingkat_dipilih
