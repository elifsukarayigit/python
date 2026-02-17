

lig = {"vakıfbank":"152 puan","Fenerbahçe": "151 puan","Galatasaray daıkın":"149 puan" }

lig.setdefault("Eczacıbaşı","148 puan")
#eczacıbaşı eklendi
print(lig)

takım_ekle = input("enter the team : ")
puan_ekle = input("enter the point : ")

lig.setdefault(takım_ekle,puan_ekle)

print(lig)
# sona eklendi

for isim,değer in lig.items():
    print(isim,değer)




lig.pop("Fenerbahçe")
print(lig)
#fenerbahçe sılındı



#dögüler ile 
while True:
    takım_ekle = input("enter the team :")
    puan_ekle = input("enter the point ")   


    lig.setdefault(takım_ekle,puan_ekle)


    for i,j in lig.items():
        print(i,j)
# durdurmadık o yüzden sonsuz tane veri alır
       
    seçim = input("çıkmak ister misinz e or h: ").capitalize()
    if seçim == "E":
        print("çıkış yapılıyor...")
        break
    else:
         pass
    


