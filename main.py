from funksiyalar import qoshish,barchasini_korish,qidirish,ochirish

while True:
    print("\n1. Kontakt qo'shish")
    print("2. Barcha kontaktlarni ko'rish")
    print("3. Kontakt qidirish")
    print("4. Kontakt o'chirish")
    print("5. Chiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        qoshish()
    elif tanlov == "2":
        barchasini_korish()
    elif tanlov == "3":
        qidirish()
    elif tanlov == "4":
        ochirish()
    elif tanlov == "5":
        break
    else:
        print("Noto'g'ri tanlov!")