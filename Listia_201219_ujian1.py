# #SOAL NO 1
def Hashtag(string):
    if len(string) < 1 or type(string) != str:
        return print(False) 

    x = string.split()
    y = ['"','#']
    for i in x:
        y.append(i.capitalize())
    z = ''.join(y) + '"'
    if len(z) < 1 or len(z)> 140:
        return print(False)
    print(z)

Hashtag("Hello there how are you doing")
Hashtag("  Hello  world  ")
Hashtag("")

###SOAL NO 2
def create_phone_number(number):
    if type(number) != list or len(number) != 10:
        return print('Invalid input')
    t =[]
    for i in number:
        if type(i) != int or i < 0 or i > 9:
            return print('Invalid input')
        else:
            t.append(str(i))
    z = ''.join(t)
    print('"({}) {}-{}"'.format(z[:3], z[3:6],z[6:]))        

create_phone_number([1,2,3,4,5,6,7,8,9,0])

##SOAL NO 3
def sort_odd_even(num):
    if type(num) != list:
        return print('Invalid input')
    ganjil1 = []
    ganjil2 = []
    idx1 = []
    genap1 = []
    genap2 = []
    idx2 = []
    for i, j in enumerate(num):
        if type(j) != int:
            return print('Invalid input')
        elif j % 2 == 0:
            genap1.append(j)
            idx2.append(i)
        else:
            ganjil1.append(j)
            idx1.append(i)
    
    while ganjil1:
        nilai_min = ganjil1[0]
        for jil in ganjil1:
            if jil < nilai_min:
                nilai_min = jil
        ganjil2.append(nilai_min)
        ganjil1.remove(nilai_min)

    while genap1:
        nilai_max = genap1[0]
        for nap in genap1:
            if nap > nilai_max:
                nilai_max = nap
        genap2.append(nilai_max)
        genap1.remove(nilai_max)

    ##alternatif:
    # ganjil1.sort()
    # genap1.sort(reverse=True)

    angka = ganjil2 + genap2
    index = idx1 + idx2
    
    gabung = num.copy()
    for i, j in zip(angka,index):
        gabung[j] = i

    print(gabung)     

sort_odd_even([])
sort_odd_even([5,3,2,8,1,4])
sort_odd_even([8,2,3,1,7,4])

##SOAL NO 4
def hollowTriangle(height):
    if type(height) != int or height < 1:
        return print('Invalid input')
    else:
        n = 1
        z = ''
        for i in range(1, height+1):
            if i == height:  ##level terakhir
                z += '#'*(height*2 - 1)
            elif height != 1 and i == 1: ##level 1
                z += '_'*(height - (i-1) - 1)
                z += '#'
                z += '_'*(height - (i-1) - 1)
            elif height != 2 and i == 2: ##level 2
                z += '_'*(height - (i-1) - 1)
                z += '#'
                z += '_'*n
                z += '#'
                z += '_'*(height - (i-1) - 1)
            else: ## level 3 dst sebelum terakhir
                z += '_'*(height - (i-1) - 1)
                z += '#'
                z += '_'*(n+2)
                z += '#'
                z += '_'*(height - (i-1) - 1)
                n += 2
            z += '\n'
    print(z)

hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)