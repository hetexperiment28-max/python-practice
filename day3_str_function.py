name = "het patel"
print(len(name))

#function1
print(name.endswith("tel")) #true output
print(name.endswith("he")) #false output

#function2
print(name.startswith("he")) #true output
print(name.startswith("et")) #false output

#function3
a = "HETPATEL"
print(name.capitalize()) #only 1st word ko capitalize karega
print(name.title()) #capitalise 1st character of each word
print(a.lower()) #LOWER CASE WHOLE WORD
print(name.upper()) #upper whole word
#function4
b = "hello world"
index = b.find("world")
print(index)

replace = b.replace("world","het")
print(replace)


