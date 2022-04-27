## 非空数组表示的非负整数，在该数的基础上加一

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        pointer = length - 1

        while pointer >= 0:
            digits[pointer] += 1
            digits[pointer] = digits[pointer] % 10
            if digits[pointer]!=0:
                return digits
            pointer -= 1
        
        # special case , such as 999 , 99 and so on

        temp = [1]
        temp.extend(digits)

        return temp

test = [9]
print(plusOne(test))