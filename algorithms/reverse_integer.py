class ReverseInteger:
    def run(self,num):
        original = num
        reversed_num = 0
        while original > 0:
            print(f"Inside the loop: with original{original} and reverse{reversed_num}")
            reversed_num = reversed_num*10 + original%10
            original = original//10
        
        return reversed_num
    
test1 = 145
rInt = ReverseInteger()
rev_int = rInt.run(test1)
print(f"Reverse of Integer {test1} is {rev_int}")