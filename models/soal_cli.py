from random import shuffle
from config import PILIHAN_GANDA


class Soal:
    def __init__(self, teks_soal: str, kumpulan_jawaban: list[str]) -> None:
        self.teks_soal = teks_soal
        self.jawaban_benar = kumpulan_jawaban[0]
        self.kumpulan_jawaban = kumpulan_jawaban
        self.map_pg: dict[str, str] = {}

    def tampilkan_soal(self) -> None:
        shuffle(self.kumpulan_jawaban)
        self.map_pg = {}

        huruf_isi = zip(PILIHAN_GANDA, self.kumpulan_jawaban)
        for huruf, isi in huruf_isi:
            self.map_pg[huruf] = isi
            print(f"{huruf}. {isi}")

    def cek_jawaban(self, huruf: str) -> bool:
        return self.jawaban_benar == self.map_pg.get(huruf)
