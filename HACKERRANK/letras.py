s = "BANANA"

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        #print(s[i] in vowels)
        kevsc += (len(s)-i)
        print("kevsc",(i,kevsc))
    else:
        stusc += (len(s)-i)
        print("stusc",(i,stusc))
if kevsc > stusc:
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
    x = input("Ingresa la prueba:" ).split()
    print(x[1])
    x.clear()
    print(x)
else:
    print("Draw")