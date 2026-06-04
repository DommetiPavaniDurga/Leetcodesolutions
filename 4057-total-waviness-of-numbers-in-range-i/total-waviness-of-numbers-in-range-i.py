class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def f(x: int) -> int:
            digits=list(map(int,str(x)))
            if len(digits)<3:
                return 0
            waviness=0
            for i in range(1,len(digits)-1):
                if digits[i]>digits[i-1] and digits[i]>digits[i+1]:
                    waviness+=1
                elif digits[i]<digits[i-1] and digits[i]<digits[i+1]:
                    waviness+=1
            return waviness
        ans=0
        for x in range(num1,num2+1):
            ans+=f(x)
        return ans