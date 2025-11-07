def hitung_luas_segitiga(alas, tinggi):
    """Fungsi untuk menghitung luas segitiga."""
    return 0.5 * alas * tinggi


def main():
    print("=== Program Hitung Luas Segitiga ===")
    try:
        alas = float(input("Masukkan panjang alas (cm): "))
        tinggi = float(input("Masukkan tinggi (cm): "))

        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas:.2f} cm²")

    except ValueError:
        print("❌ Input tidak valid! Harap masukkan angka.")


if __name__ == "__main__":
    main()
