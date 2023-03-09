#https://projecteuler.net/problem=9
#Special Pythagorean triplet
#Problem 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a² + b² = c²
#For example, 3² + 4² = 9 + 16 = 25 = 5².
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for m in range(30):
    for n in range(30):
        a=(m**2)-(n**2)
        #print(f"a: {a}")

        b=2*m*n
        #print(f"b: {b}")

        c=(m**2)+(n**2)
        #print(f"c: {c}")

        if a+b+c==1000:
            print(f"{a} + {b} + {c} = 1000")
            sol=a*b*c
            print(f"produto de abc: {sol}")
