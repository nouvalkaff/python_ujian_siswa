from repositories.bank_soal_cli import BankSoal


class BankSoalApp:
    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self, tingkat: str) -> list[str]:
        with open(f"{BankSoal.dir_path}_{tingkat}.txt", "r") as file:
            self.daftar_soal = [soal.strip() for soal in file]
        return self.daftar_soal
