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


def evaluate_score(score: int) -> str:
    if score <= 50:
        message = "Keep up the effort! Don't give up, you can definitely do better! 💪"
    elif score <= 70:
        message = "Good job! Keep studying and practicing to improve your score! 😊"
    elif score <= 85:
        message = "Great job! You did really well. Keep it up! 🌟"
    elif score <= 96:
        message = "Awesome! Keep up the great effort and keep growing! ⭐"
    else:
        message = "Outstanding! Excellent work. Keep up your passion for learning! 🎉"
    return message
