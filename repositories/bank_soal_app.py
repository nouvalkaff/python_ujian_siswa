from config import DIR_PATH_IDN, DIR_PATH_ENG


class BankSoalApp:
    def __init__(self) -> None:
        self.daftar_soal = []

    def ambil_soal(self, tingkat: str, bahasa: str) -> list[str]:
        path_soal = {
            "1": DIR_PATH_IDN,
            "2": DIR_PATH_ENG,
        }

        try:
            with open(f"{path_soal[bahasa]}_{tingkat}.txt", "r") as file:
                self.daftar_soal = [soal.strip() for soal in file if soal.strip()]
        except FileNotFoundError:
            self.daftar_soal = []

        return self.daftar_soal
