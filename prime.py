class Solution:
    def countPrimes(self, n: int) -> int:
        def prime(n) :
            for i in range(2,(n//2) +1):
                if(n % i == 0) :
                    return -1 

            return 1 
        count = 0 
        p = [2,3,5,7]
        k = 2
        if(n<=10) : 
            for i in range(4) :
                if(p[i] < n) :
                    count += 1 

        else  :
            count += 4 
            while True :
                op = 6*k - 1
                if(op >= n) :
                    break 

                if(prime(op) == 1) :
                    count += 1 

                op = 6*k + 1
                if(op >= n) :
                    break 

                if(prime(op) == 1) :
                    count += 1

                k += 1

        return count 




        

        
