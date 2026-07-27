from random import shuffle

TINGKAT_SD = ["1", "2", "3", "4", "5", "6"]
JUMLAH_SOAL = 10


def ambil_soal(tingkat: str) -> list[str]:
    with open(f"./assets/bank_soal_sd_{tingkat}.txt", "r") as file:
        list = []
        for soal in file:
            list.append(soal.strip())
        del list[0]
        return list


def parse_soal(baris: str) -> tuple[str, list[str], str]:
    """Pecah satu baris bank soal jadi (pertanyaan, daftar opsi, jawaban benar)."""
    soal = baris.split("|")
    pertanyaan = soal[0]
    opsi = soal[1].split(",")
    opsi = [x.capitalize() for x in opsi]
    jawaban_benar = opsi[0]
    return pertanyaan, opsi, jawaban_benar


def acak_opsi(opsi: list[str]) -> list[str]:
    """Acak urutan opsi jawaban tanpa mengubah list asli."""
    opsi_acak = opsi[:]
    shuffle(opsi_acak)
    return opsi_acak


def hitung_nilai(jumlah_benar: int) -> tuple[int, str]:
    """Hitung nilai akhir (0-100) + pesan motivasi berdasarkan jumlah benar."""
    nilai = int((jumlah_benar / JUMLAH_SOAL) * 100)

    if nilai <= 50:
        pesan = "Ayo semangat belajar lagi ya! 💪"
    elif nilai <= 70:
        pesan = "Lumayan! Sedikit lagi bisa lebih baik."
    elif nilai <= 85:
        pesan = "Bagus! Kamu sudah paham banyak nih."
    elif nilai <= 95:
        pesan = "Keren banget! Kamu pintar sekali! 🌟"
    else:  # 96-100
        pesan = "Luar biasa! Nilai sempurna, kamu juara! 🎉🏆"

    return nilai, pesan
