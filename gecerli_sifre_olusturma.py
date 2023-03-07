import string

def gecerliSifre(sifre):
    if len(sifre) < 4:
        return "Şifreniz çok kısa"
    if not any(char.isdigit() for char in sifre):
        return "Şifreniz sayı içermek zorundadır."
    if not any(char.isupper() for char in sifre):
        return "Şifreniz büyük harf içermek zorundadır."
    if not any(char.islower() for char in sifre):
        return "Şifreniz küçük harf içermek zorundadır."
    if not any(char in string.punctuation for char in sifre):
        return "Şifreniz sembol içermek zorundadır."
    return "Bu şifreyi kullanabilirsiniz."

while True:
    sifre = input("Oluşturmak istediğiniz parolayı giriniz: ")
    sonuc = gecerliSifre(sifre)
    if sonuc == "Bu şifreyi kullanabilirsiniz.":
        print("Bu şifre başarılı.")
        break
    else:
        print(sonuc)
