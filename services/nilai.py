def evaluasi_nilai(nilai: int) -> str:
    if nilai <= 50:
        pesan = "Tetap semangat belajar, ya! Jangan menyerah, kamu pasti bisa lebih baik! 💪"
    elif nilai <= 70:
        pesan = "Bagus! Terus belajar dan berlatih supaya nilaimu semakin baik! 😊"
    elif nilai <= 85:
        pesan = "Hebat! Kamu sudah belajar dengan baik. Terus semangat, ya! 🌟"
    elif nilai <= 96:
        pesan = "Bagus sekali! Pertahankan semangat belajarmu dan terus berkembang! ⭐"
    else:
        pesan = "Luar biasa! Kerjamu sangat baik. Tetap semangat belajar dan terus berkembang! 🎉"
    return pesan
