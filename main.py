# Practice app 3: Ujian Siswa v1.1
from colorama import Fore, Style

from repositories.bank_soal_cli import BankSoal
from services.ujian_siswa_cli import UjianSiswa


def main():
    try:
        bank_soal = BankSoal()
        bank_soal.ambil_soal()
        ujian_siswa = UjianSiswa(bank_soal.daftar_soal)
        ujian_siswa.proses_soal()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program dihentikan oleh pengguna!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
