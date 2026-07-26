from colorama import Fore, Style
from random import shuffle

PILIHAN_GANDA = ["a", "b", "c", "d"]
TINGKAT_SD = ["1", "2", "3", "4", "5", "6"]
JUMLAH_SOAL = 10


def ambil_tingkat() -> str:
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
            f"{Fore.CYAN}Siap! Kamu akan mengerjakan soal kelas {tingkat_dipilih}{Style.RESET_ALL}\n"
        )
        return tingkat_dipilih


def ambil_soal(tingkat: str) -> list[str]:
    with open(f"bank_soal_sd_{tingkat}.txt", "r") as file:
        list = []
        for soal in file:
            list.append(soal.strip())
        del list[0]
        return list


def tampilkan_soal(kumpulan_jawaban: list[str]) -> dict:
    soal_dict = {}
    shuffle(kumpulan_jawaban)
    for i in range(len(kumpulan_jawaban)):
        pg = PILIHAN_GANDA[i]
        isi_pg = kumpulan_jawaban[i]
        soal_dict[pg] = isi_pg
        print(f"{pg}. {isi_pg}")
    return soal_dict


def proses_jawab(soal_dict: dict, jawaban_benar: str):
    while True:
        jawaban_user = input("\nJawabanmu: ").strip().lower()
        if jawaban_user not in PILIHAN_GANDA:
            print(
                f"{Fore.YELLOW}Jawaban tidak valid! Ketik salah satu huruf: a, b, c, atau d.{Style.RESET_ALL}"
            )
            continue
        elif jawaban_benar == soal_dict[jawaban_user]:
            print(f"{Fore.GREEN}Jawaban benar.{Style.RESET_ALL}\n")
            return True
        else:
            print(f"{Fore.RED}Jawaban salah.{Style.RESET_ALL}")
            print(f"Jawaban yang benar adalah '{jawaban_benar}'\n")
            return False


def tampilkan_hasil(jumlah_benar: int):
    nilai = int((jumlah_benar / JUMLAH_SOAL) * 100)

    if nilai <= 50:
        warna = Fore.RED
        pesan = "Ayo semangat belajar lagi ya! 💪"

    elif nilai <= 70:
        warna = Fore.YELLOW
        pesan = "Lumayan! Sedikit lagi bisa lebih baik."

    elif nilai <= 85:
        warna = Fore.CYAN
        pesan = "Bagus! Kamu sudah paham banyak nih."

    elif nilai <= 95:
        warna = Fore.GREEN
        pesan = "Keren banget! Kamu pintar sekali! 🌟"

    else:  # 96-100
        warna = Fore.LIGHTGREEN_EX
        pesan = "Luar biasa! Nilai sempurna, kamu juara! 🎉🏆"

    print(f"\nJumlah jawaban benar : {jumlah_benar}/{JUMLAH_SOAL}")
    print(f"{warna}Nilai akhir kamu : {nilai}{Style.RESET_ALL}")
    print(f"{warna}{pesan}{Style.RESET_ALL}")


def proses_soal(raw_soal: list[str]):
    shuffle(raw_soal)
    jumlah_benar = 0

    for i in range(JUMLAH_SOAL):
        soal = raw_soal[i].split("|")

        print(f"{i+1}. Soal: {soal[0]} ?")
        print("Pilihan Ganda:")

        kumpulan_jawaban = soal[1].split(",")
        jawaban_benar = kumpulan_jawaban[0]

        soal_dict = tampilkan_soal(kumpulan_jawaban)
        hasil_jawab = proses_jawab(soal_dict, jawaban_benar)

        if hasil_jawab == True:
            jumlah_benar += 1

    tampilkan_hasil(jumlah_benar)
