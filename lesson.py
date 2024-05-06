# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]
'''

cavablar =[]
for i in range(1,6):
    cavablar.append(int(input("Bir reqem daxil edin: ")))
cavablar.sort()
print(f"{cavablar} Her bir daxil olunan reqem sira ile duzuldu")
'''


# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü.
'''
cumle=input("Bir cumle daxil edin: ").split()
sozler=""
for i in cumle:
    cumle2=sorted(i)
    for j in cumle2:
        sozler+=j
    sozler+=" "
print(sozler)
'''


# 3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13
# tebrikler . 4 cehdde 13 reqemeni tapdiz
'''
cehd=1
while True:
    eded=int(input("Fikrimde tutdugum ededi tapin: "))
    if eded ==33:
        print(f" Tebrikler fikrimde tutdugum ededi {cehd} cehdde tapdiniz :)")
        break
    cehd+=1
'''

# 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)

"""sade=[]
def sadeler(ededler):
    for i in range(2,ededler):
        if ededler % i==0:
            return False
    return True
for j in range(2,100):
    if sadeler(j):
        sade.append(j)
print(sade)

"""









