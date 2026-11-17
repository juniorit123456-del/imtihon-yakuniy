from database import db,cursor

def qoshish():
    ism = input("Ism: ")
    familya = input("Familya: ")
    raqam = input("Raqam: ")
    yosh = input("Yosh: ")
    adress = input("Adress: ")

    if not yosh.isdigit():
        print("Yosh faqat son bo'lishi kerak!")
        return

    cursor.execute("""
    INSERT INTO contact (ism, familya, raqam, yosh, adress) VALUES (?, ?, ?, ?, ?)
""", (ism, familya, raqam, yosh, adress))

    db.commit()
    print("Kontakt qoshildi!")

def barchasini_korish():
    cursor.execute("SELECT * FROM contact")
    natija = cursor.fetchall()
    print("Barcha kontaktlar:")
    for kontakt in natija:
        print(f"ID: {kontakt[0]}, Ism: {kontakt[1]}, Familya: {kontakt[2]}, Raqam: {kontakt[4]}, Yosh: {kontakt[3]}, Adress: {kontakt[5]}")

def qidirish():
    qidiruv = input("Qidirish uchun ism yoki familya kiriting: ")
    cursor.execute("SELECT * FROM contact WHERE ism LIKE ? OR familya LIKE ?", (f"%{qidiruv}%", f"%{qidiruv}%"))
    natija = cursor.fetchall()
    if natija:
        print("Qidirish natijalari:")
        for kontakt in natija:
            print(f"ID: {kontakt[0]}, Ism: {kontakt[1]}, Familya: {kontakt[2]}, Raqam: {kontakt[4]}, Yosh: {kontakt[3]}, Adress: {kontakt[5]}")
    else:
        print("Natija topilmadi!")

def ochirish():
    id_ochirish = input("O'chirish uchun kontakt ID kiriting: ")
    cursor.execute("DELETE FROM contact WHERE id = ?", (id_ochirish,))
    db.commit()
    if cursor.rowcount > 0:
        print("Kontakt o'chirildi!")
    else:
        print("Bunday ID topilmadi!")