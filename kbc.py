print("welcom to kon bane ga crorepati")
print("your first question is")
print("What is the capital city of Australia?")
print("A) Sydney")
print("B) Melbourne")
print("C) Canberra")
print("D) Brisbane")
a=input('choose you option :')
if (a=="c"):
    print(" you are win 1000 congratulating ")
    print("your second question is")
    print("Who is known as the father of modern physics?")
    print("a) Isaac Newton")
    print("b) Albert Einstein")
    print("c) Galileo Galilei")
    print("d) Nikola Tesla")

    b=input('choose you answer')
    if (b=="b"):
        print(" you are win 2000 congratulating ")
        print("your 3th question is")
        print("Who was the first woman to win a Nobel Prize?")
        print("a) Marie Curie")
        print("b)  Mother Teresa")
        print("c) Leonardo da Vinci")
        print("d) Rosalind Franklin")
    
        a=input('choose you answer').lower()
        if (a=="a"):
            print(" you are win 3000 congratulating ")
            print("your 4th question is")
            print("What is the largest ocean on Earth?")
            print("a) Atlantic Ocean")
            print("b) Indian Ocean")
            print("c) Arctic Ocean")
            print("d) Pacific Ocean")
            a=input('choose you answer').lower()
            if (a=="a"):
             print(" you are win 4000 congratulating ")
            else:
                print("sorry your ans is wrong")
                print("you are win 3000 congratulating") 
        else:
             print("sorry your ans is wrong")
             print("you are win 2000 congratulating")    
    else:
        print("sorry your ans is wrong")  
        print("you are win 1000 congratulating")  
else:
    print("sorry your ans is wrong")