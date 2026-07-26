# Practice app 3: Ujian Siswa v1.0
from colorama import Fore, Style

from functions import ambil_soal, proses_soal


def main():
    try:
        soal = ambil_soal()
        proses_soal(soal)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program dihentikan oleh pengguna!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
