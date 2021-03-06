class Euler(object):

    # Define global variables
    def __init__(self):
        self.sum = 0
        self.count = 0
        self.tdn = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    # Define key functions
    def factorial(self,n):
        #print("[test] Factorial of %d" % n)
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
    
    def listContains(self,big_set,sm_set):
        #all(True if sequenceA.count(item) <= sequenceB.count(item) else False for item in sequenceA)
        for item in sm_set:
            if sm_set.count(item) <= big_set.count(item):
                pass
            else:
                return False
        return True
            
    def listAddMissing(self,bigL,smL):
        tempL = []
        #print("[test] Comparing smL %s to bigL %s" % (smL,bigL))
        if self.listContains(bigL,smL):
            return bigL
        else:
            for i in smL:
                if i in bigL:
                    #print("[test] Removing %d from bigL %s" % (i,bigL))
                    bigL.remove(i)
                tempL.append(i)
            return tempL + bigL
    
    #find Fibonacci sequence less than n, return that list        
    def findFib(self,n):
        fibList = [0]
        fibCt = 1
        while fibCt < n:
            fibList.append(fibCt)
            fibCt = fibList[-1]+fibList[-2]
        return fibList
    
    #find primes less than n
    def findPrimes(self,n):
        primeList = [2]
        for i in range(3,n,2):
            #print("[test] Evaluating... %d" % i)
            for x in primeList:
                if i % x != 0:
                    if x == primeList[-1]:
                        primeList.append(i)
                        #print("[test] Adding... %d" % i)
                        break
                    pass
                else:
                    #print("[test] Not a prime: %d" % i)
                    break    
        return primeList
    
    def primeFactors(self,n):
        """Return a list of the prime factors for a natural number."""
        if n < 2:
            return []
        prime_factors = []
        for p in self.findPrimes(n+1):
            #print("[test] primeFactors for loop... %d" % p)
            while n % p == 0:
                #print("[test] primeFactors while-append loop (n%p)... %d" % (n%p))
                prime_factors.append(p)
                n //= p
        return prime_factors
    
    """
    Largest Prime Factor (Euler #3)
    """
    def largestPrime(self,n):
        x = n/2
        print("[+] Test initial value of x: %d" % x)
        if x**2 == n:
            return x
        else:
            while n % x != 0:
                x -= 1
                print("[+] Test value of x: %d" % x)
            return x
        
    """
    Sum of Thress and Fives (Euler #1)
    """
    def getSums(self,num,n):
        qsum = 0
        i = 0
        curVal = 0
        while curVal < n:
            #print("[+] Multiple of %d: %d" % (num,curVal))
            qsum += curVal
            i += 1
            curVal = i*num
        return qsum
    def sumThreeFive(self,n):
        return self.getSums(3,n) + self.getSums(5,n) - self.getSums(15,n)

    """
    Smallest multiple (Euler #5)
    """
    def smMultiple(self,n):
        product = 1
        pList = []
        for i in range(2,n+1): #reversed may be faster
            tempList = self.primeFactors(i)
            #print("[test] Factoring... %d: %s" % (i,tempList))
            pList = self.listAddMissing(pList,tempList)
        #print(pList)
        for i in pList:
            product *= i
        return product
    
    """
    Sum Square Difference (Euler #6)
    """
    def sumOfSq(self,n):
        sum = 0
        for i in range(1,n+1):
            sum += (i*i)
        return sum
    
    def sqSum(self,n):
        sum = 0
        for i in range(1,n+1):
            sum += i
        return (sum*sum)
    
    def sumSqDif(self,n):
        return (self.sqSum(n) - self.sumOfSq(n))
    
    """
    10001st Prime (Euler #7)
    """
    def ordPrime(self,n):
        primeList = [2]
        i = 3
        while len(primeList) < n:
            #print("[test] Evaluating... %d" % i)
            for x in primeList:
                if i % x != 0:
                    if x == primeList[-1]:
                        primeList.append(i)
                        #print("[test] Adding... %d" % i)
                        break
                    pass
                else:
                    #print("[test] Not a prime: %d" % i)
                    break   
            i += 2
        return primeList[-1]
    
    """
    Largest Product in a Series (Euler #8)
    """
    def evalProd(self,tempStr):
        tprod = 1
        for i in tempStr:
            tprod *= int(i)
        print("[test] tprod of %s is: %d" % (tempStr,tprod))
        return tprod
    
    def lgProdSeries(self,numStr):
        prod = 1
        for i in range(0,len(numStr)-13):
            prod = max(prod,self.evalProd(numStr[i:i+13]))
            print("[test] maximum prod is: %d" % prod)
        return prod
        
    """
    Sum of Primes (Euler #10)
    """
    def listSum(self,numList):
        sum = 0
        for i in numList:
            sum += i
        return sum
        
    def sumOfPrimes(self,n):
        return self.listSum(self.findPrimes(n))
    
    """
    Pythagorean Triplets (Euler #9)
    """
    def pythagTest(self,a,b,c):
        if (a*a)+(b*b)==(c*c):
            return True
        return False
        
    def pythagRec(self,a,n):
        for i in range(a,n):
            print("[test] evaluating a=%d, b=%d, c=%d" % (a,i,n-a-i))
            if self.pythagTest(a,i,n-a-i):
                print [a,i,n-a-i]
                return a*i*(n-a-i)
        return self.pythagRec(a+1,n)
            
    def pythagTrip(self,n): #solve for a triplet where sum(a,b,c)=n and return product abc
        #technically, this algorithm is valid, but takes too long
        return self.pythagRec(1,n)
    
    """
    Sum of even Fibonacci numbers (Euler #2)
    """
    def evenFib(self,n):
        fibList = self.findFib(n)
        for i in fibList:
            if i % 2 == 0:
                self.sum += i
        return self.sum
    
    """
    Highly Divisible Triangular Numbers
    """
    def triNumGen(self,n):
        for i in range(1,n):
            self.sum += i
        return self.sum
    
    def factorNum(self,n):
        flist = []
        for i in range(1,int(n/2)):
            if i in flist:
                return flist
            elif n % i == 0:
                flist.append(i)
                if i != n/i:
                    flist.append(n/i)
        return flist
    
    def hiDivTriNum(self,n):
        tlist = []
        while len(tlist) < n:
            self.count += 1
            tlist = self.factorNum(self.triNumGen(self.count))
        return self.triNumGen(self.count)

    # Define MAIN
    def run(self, n):
        #print("The largest prime in %d is %d" % (n,self.largestPrime(n)))
        #print ("The sums of multiples of 3 and 5 less than 1000 is: %d" % self.sumThreeFive(1000))
        #print("The smallest multiple of the numbers 1..20 is: %d" % self.smMultiple(n))
        #print("The prime factors of %d: %s" % (n,self.primeFactors(n)))
        #print("The difference of squares and sums for the first %d natural numbers is: %d" % (n,self.sumSqDif(n)))
        #print("The %dst prime number is: %d" % (n,self.ordPrime(n)))
        #print("The largest product in the series is: %d" % self.lgProdSeries(self.tdn))
        print("The sum of all primes below %d is: %d" % (n,self.sumOfPrimes(n))) #Needs more processing power
        #print("The product abc for the Pythagorean triplet where their sum is %d is: %d" % (n,self.pythagTrip(n)))
        #print("The Fib sequence for numbers less than %d is: %s" % (n,self.evenFib(n)))
        #print("The triangular number highly divisible with %d quotients is: %d" % (n,self.hiDivTriNum(n)))
        
# Run test cases
"""
if __name__ == '__main__':
    Euler.run()
"""

testCase = Euler()
#testCase.run(13195) #largest Prime FAIL
#testCase.run(600851475143) #largest Prime FAIL
#testCase.run(1000) #sum of threes and fives PASS
#testCase.run(20) #smallest multiple of all numbers less than 20 PASS
#testCase.run(100) #squares and sums difference PASS
#testCase.run(10001) #10001st prime number PASS
#testCase.run(1) #largest product in a series (self.tdn) PASS
testCase.run(2000000) #sum of primes below 2000000 FAIL/WAIT
#testCase.run(1000) #product of Pythagorean triplet PASS/WAIT
#testCase.run(4000000) #sum of even Fibonacci numbers less than 4000000 PASS
#testCase.run(500) #triangle number highly divisible with over 500 quotients FAIL
