from collections import Counter #i need this for the last exercise
class ex1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def make_ex1(self, a, b): #pretty easy, i get a and b from user, i do the product and check if it's greater than 1000

        print("you entered ", a, " and ", b)
        product = a * b
        if product > 1000:
            sum = a + b
            print(sum)
        else:
            print(product)


class ex2:
    def __init__(self, a):
        self.a = a

    def make_ex2(self, a, i):
        list = [] #creating my list
        for j in range(0, a):
            list.append(j) #for speed reasons i just make an incrementing list
        sum = 0
        for j in range(i, a): #adding the new term to the previous ones
            sum = sum + j
            print(j, " ", sum)


class ex3:
    def __init__(self, a):
        self.a = a

    def make_ex3(self, a):
        list = []
        for i in range(0, a):
            list.append(i)
        if list[0] == list[a - 1]:
            print("true")
        else:
            print("false")


class ex4:
    def __init__(self, a):
        self.a = a

    def make_ex4(self, a):
        list = []
        for i in range(0, a):
            list.append(i)
            if list[i] % 5 == 0:
                print(list[i])


class ex5:
    def __init__(self, str):
        self.str = str

    def make_ex5(self, str, word):
        if word in str:
            print(str.count(word))


class ex6:
    def __init__(self, a):
        self.a = a

    def make_ex6(self, a):
        list1 = []
        list2 = []
        list3 = []
        for i in range(0, a):
            list1.append(i)
            list2.append(i)
            if (i % 2 == 0):
                list3.append(list1[i])
            else:
                list3.append(list2[i])
            print(list3[i])


class ex7:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
    def make_ex7(self,str1,str2):
        start=int(len(str1)/2)
        str3=str1[:start]+str2+str1[start:]
        print(str3)

class ex8:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
    def make_ex8(self,str1,str2):
        mid1=int(len(str1)/2)
        mid2=int(len(str2)/2)
        str3=str1[0]+str1[mid1]+str1[-1]+str2[0]+str2[mid2]+str2[-1]
        print(str3)

class ex9:
    def __init__(self,str1):
        self.str1=str1

    def make_ex9(self,str1):
        nupper=sum(map(str.isupper,str1))
        nlower=sum(map(str.islower,str1))
        nsep=len(str1)-sum(map(str.isalnum,str1))-sum(map(str.isspace,str1))
        ndig=sum(map(str.isdigit,str1))
        print(str1, "\nUpper: ",nupper," ,Lower: ",nlower,",Digits: ",ndig,",Special: ",nsep)


class ex10:
    def __init__(self,str1):
        self.str1=str1
    def make_ex10(self,str1):
        str1.lower()
        if 'usa' in str1:
            print(str1.count('usa'))

class ex11:
    def __init__(self,str1):
        self.str1=str1
    def make_ex11(self,str1):
        sum=0
        count=0
        str1.replace(" ", "")
        for i in range(0,len(str1)):
            if str1[i].isdigit:
                sum=sum+int(str1[i])
                count+=1
        avg=sum/count
        print(sum," ",avg)

class ex12:
    def __init__(self,str1):
        self.str1=str1
    def make_ex12(self,str1):
        res = Counter(str1)
        print(str(res))
