x = input ("zadejte proměnnou x")
y = input ("zadejte proměnnou y")


print("Zde máte možnosti")
print("Pokud chcete sčítat zadejte +")
print("Pokud chcete odčítat uadejte -")
print("Pokud chcete násobit zadejte *")
print("Pokud chcete dělit zadejte /")
print("Pokud chcete mocnit zadejte **, x = mocněnec a y = mocnitel")
print("Pokud chcete odmocnit zadejte odm, x = mocněnec a y = mocnitel")

znamenko = input("co budeme počítat")

if znamenko == "+":
    print(x+y)
elif znamenko == "-":
    print (x-y)
elif znamenko == "*":
    print (x*y)
elif znamenko == "/":
    if y == 0:
        print ("Nelze dělit nulou")
    else:
         print(x/y)
elif znamenko == "**":
    print (x**y)
elif znamenko == "odm":
    print (x**(1/y))
