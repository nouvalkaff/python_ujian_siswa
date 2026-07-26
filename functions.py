from colorama import Fore, Style
from random import shuffle

PILIHAN_GANDA = ["a", "b", "c", "d"]
JUMLAH_SOAL = 10


def ambil_soal() -> list[str]:
    with open("bank_soal_sd_1.txt", "r") as file:
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
        jawaban_user = input("Jawabanmu: ").strip().lower()
        if jawaban_user not in PILIHAN_GANDA:
            print(
                f"{Fore.YELLOW}Input hanya huruf a, b, c, atau d (huruf besar atau kecil){Style.RESET_ALL}"
            )
            continue
        elif jawaban_benar == soal_dict[jawaban_user]:
            print("Jawabanmu benar.\n")
            return True
        else:
            print("Jawabanmu salah.\n")
            return False


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

    print("jumlah_benar", jumlah_benar)
    print(
        f"{Fore.GREEN}Selamat nilai akhir kamu: {int((jumlah_benar) / JUMLAH_SOAL * 100)}{Style.RESET_ALL}"
    )
