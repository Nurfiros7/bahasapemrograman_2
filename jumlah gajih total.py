def hitung_gaji():
    # Input data pegawai
    nama = input("Masukkan Nama: ")
    nik = input("Masukkan NIK: ")
    status = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
    golongan = input("Masukkan Golongan (A/B/C): ").strip().upper()

    # Data gaji dan bonus berdasarkan status dan golongan
    gaji_tetap = 1000000
    gaji_honor = 750000
    bonus_tetap = {'A': 200000, 'B': 400000, 'C': 550000}
    bonus_honor = {'A': 150000, 'B': 275000, 'C': 480000}

    # Menentukan gaji dan bonus
    if status == "pegawai tetap":
        gaji = gaji_tetap
        bonus = bonus_tetap.get(golongan, 0)
    elif status == "honor":
        gaji = gaji_honor
        bonus = bonus_honor.get(golongan, 0)
    else:
        print("Status tidak valid!")
        return
    
    # Hitung total gaji
    gaji_total = gaji + bonus
    
    # Output hasil
    print("\n=== Rincian Gaji ===")
    print(f"Nama       : {nama}")
    print(f"NIK        : {nik}")
    print(f"Status     : {status.title()}")
    print(f"Golongan   : {golongan}")
    print(f"Gaji       : Rp {gaji:,}")
    print(f"Bonus      : Rp {bonus:,}")
    print(f"Gaji Total : Rp {gaji_total:,}")

# Menjalankan program
hitung_gaji()
