#ne kadar su içmeniz gerektiğini anlatan bir program

#formül kilo*0.03 
def water(kilo):
    man_water = kilo*0.04
    woman_water =kilo*0.03

    cinsiyet =input("Lütfen cinsiyetinizi giriniz (woman/man)").lower() #bütün kelimler küçühe
    
    if cinsiyet =="man":
        print(man_water,"litre su içiniz")
        
    elif cinsiyet == "woman":
        print(woman_water,"litre su içiniz")
        
    

water(65)