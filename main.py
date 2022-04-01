from ex1 import * #importing all my classes

if __name__ == '__main__':
    exe=input("choose an exercise:\n") #asking the user which exercise they want to execute
    match exe: #they are all self explanatory, just get the input from user and call the method
        case '1':
            a = input("enter a number:\n")
            b = input("enter another number:\n")
            a = int(a)
            b = int(b)
            ex=ex1(a,b)
            ex.make_ex1(a,b)
        case '2':
            a=input("enter a number:\n")
            a=int(a)
            i=input("enter the starting point:\n")
            i = int(i)
            ex=ex2(a)
            ex.make_ex2(a,i)
        case '3':
            a = input("enter a number:\n")
            a = int(a)
            ex=ex3(a)
            ex.make_ex3(a)
        case '4':
            a = input("enter a number:\n")
            a = int(a)
            ex=ex4(a)
            ex.make_ex4(a)
        case '5':
            str="Emma is a good developer. Emma is also a writer."
            word="Emma"
            ex=ex5(str)
            ex.make_ex5(str,word)
        case '6':
            a = input("enter a number:\n")
            a = int(a)
            ex=ex6(a)
            ex.make_ex6(a)
        case '7':
            str1="Hello everyone, this is my string."
            str2="HALLO AVURINYAN"
            ex=ex7(str1,str2)
            ex.make_ex7(str1,str2)
        case '8':
            str1=input("Write something\n")
            str2=input("Write something\n")
            ex=ex8(str1,str2)
            ex.make_ex8(str1,str2)
        case '9':
            str1=input("write something\n")
            ex=ex9(str1)
            ex.make_ex9(str1)

        case '10':
            str1=input("write something\n")
            ex=ex10(str1)
            ex.make_ex10(str1)
        case '11':
            str1=input("write something\n")
            ex=ex11(str1)
            ex.make_ex11(str1)

        case '12':
            str1=input("Write something\n")
            ex=ex12(str1)
            ex.make_ex12(str1)
        case _:
            print("please select a number")