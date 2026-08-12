# Practice app 3: Ujian Siswa v1.1
from colorama import Fore, Style

from repositories.bank_soal_cli import BankSoal
from services.ujian_siswa_cli import UjianSiswa


def main():
    bank_soal = None
    try:
        bank_soal = BankSoal()
        bank_soal.ambil_soal()
        ujian_siswa = UjianSiswa(bank_soal.daftar_soal, bank_soal.pilihan_bahasa)
        ujian_siswa.proses_soal()
    except KeyboardInterrupt:
        bahasa = getattr(bank_soal, "pilihan_bahasa", "ind")
        msg = (
            "Program dihentikan oleh pengguna!"
            if bahasa == "ind"
            else "Program stopped by user!"
        )
        print(f"\n{Fore.RED}{msg}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
