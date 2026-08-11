from config import DIR_PATH


class BankSoalApp:
    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self, tingkat: str) -> list[str]:
        with open(f"{DIR_PATH}_{tingkat}.txt", "r") as file:
            self.daftar_soal = [soal.strip() for soal in file]
        return self.daftar_soal
