def goodday(name, ending) :
    print("good day," + name)
    print(ending)

goodday("het", "thank you")


#default arguments
def goodday(name, ending="thank you") :
    print("good day," + name)
    print(ending)

goodday("het") #thank you already given to endind (pre define)
