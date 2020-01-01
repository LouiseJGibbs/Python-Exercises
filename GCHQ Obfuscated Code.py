A = "nymphsblitzquIckvexdwarfjog."

def encrypt(a):
    
    b = A
    n = len(A)
    i = 0
    z = 0
    c = ""

    while(i<len(a)):
        x = A.index(a[i])
        
        y = A.index(b[i%len(b)])
        #print("Y:", y,A[i%len(b)], a[i%len(b)], b[i%len(b)],i%len(b)) 
        z = (x+y)%n
        #print((x+y)%n)
        c = c+A[z]

        print(a[i], A[z])
        print(A.index(a[i]), A.index(A[z]))

        if (x + 1)==n:
            b=c

        i = i + 1
        #print(c[i-1], a[i - 1], i, n, x, y, z)

    return c

def decrypt(a):
    
    b = A
    n = len(A)
    i = 0
    z = 0
    c = ""

    while(i<len(a)):
    
        x = A.index(a[i])
        y = A.index(b[i%len(b)])

        z = x - i

        if z > -1:
            c = c+A[z]
            print(x, y, i, z)
        else:
            c = c+" "
            print("error")
        print(c)
        
        #z = (x-y)%n

        #print(x, y, i, z)

        

        #if(z<0):
        #    z = len(A) + z
         #   print(x, i, z)
        #if z > 0:
            #print(a[i], A[z])
            #print(A.index(a[i]), A.index(A[z]))
        

        if (x + 1)==n:
            b=c

        i = i + 1
        #print(c[i-1], a[i - 1], i, n, x, y, z)

    return c
 

def main():
    encrypted = "tsdmueyuvrxIedqqfmdqweIyaaxtiyzrujqezxqdawgotw"
    #decrypted = "helloof"
    #print(encrypt(decrypted))
    print(decrypt(encrypted))
    print(encrypt(decrypt(encrypted)))

    
    
main()
        

