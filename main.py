TEGANGAN = 220

data_arus = [
    1.6, 2.2, 3.5, 4.1, 5.4,
    2.8, 6.0, 3.9, 1.9, 4.8,
    5.1, 2.6, 3.2, 4.4, 5.8
]

# Nilai 3.18/3.19 dan 4.54/4.55 membantu menguji area sekitar batas daya.
data_arus += [0.5, 3.18, 3.19, 4.54, 4.55]


def hitung_daya(tegangan, arus):
    """Menghitung daya listrik dalam watt."""
    return tegangan * arus


def status_beban(daya):
    """Menentukan  status beban berdasarkan daya (NORMAL/WARNING/BEBAN TINGGI)."""
    if daya <= 700:
        return "NORMAL"
    elif daya <= 1000:
        return "WARNING"
    else:
        return "BEBAN TINGGI"


def rata_rata(data):
    """rata-rata sekumpulan angka."""
    return sum(data) / len(data)


def hitung_kategori(data_status, kategori):
    """Menghitung banyaknya data dengan status tertentu."""
    jumlah = 0
    for status in data_status:
        if status == kategori:
            jumlah += 1
    return jumlah


def main():
    data_daya = []
    data_status = []

    print("=== BEBAN/DAYA LISTRIK ===")
    print(f"Tegangan tetap: {TEGANGAN} V")
    print("-" * 66)

    for nomor, arus in enumerate(data_arus, start=1):
        daya = hitung_daya(TEGANGAN, arus)
        status = status_beban(daya)

        data_daya.append(daya)
        data_status.append(status)

        print(
            f"{nomor:02d}. Arus = {arus:.2f} A | "
            f"Daya = {daya:.2f} W | Status = {status}"
        )

    print("\n=== RINGKASAN ===")
    print(f"Total data: {len(data_arus)}")
    print(f"NORMAL: {hitung_kategori(data_status, 'NORMAL')}")
    print(f"WARNING: {hitung_kategori(data_status, 'WARNING')}")
    print(f"BEBAN TINGGI: {hitung_kategori(data_status, 'BEBAN TINGGI')}")
    print(f"Rata-rata daya: {rata_rata(data_daya):.2f} W")
    print(f"Daya maksimum: {max(data_daya):.2f} W")
    print(f"Daya minimum: {min(data_daya):.2f} W")


if __name__ == "__main__":
    main()