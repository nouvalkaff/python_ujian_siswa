from config import DIR_PATH_ID


class BankSoalApp:
    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self, tingkat: str) -> list[str]:
        with open(f"{DIR_PATH_ID}_{tingkat}.txt", "r") as file:
            self.daftar_soal = [soal.strip() for soal in file if soal.strip()]
        return self.daftar_soal
