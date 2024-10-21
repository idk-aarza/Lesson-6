a= 23
b= 12
c = 25

if a>b or a<c:
    print("I am using or operator")
elif a<b and a>c:
    print("I am using and operator")


a= 24
b= 23
c= 23
print(a != b)
print(b != c)

a= "python"
b= 'coding'
if a != b:
    print(a, "and", b, "are different")

a= int(input("enter a no."))
if a%2 != 0:
    print('Its not an even no.')