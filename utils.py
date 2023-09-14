class Utils:
    def reversed(self, number):
        if type(number) is int:
            reverse_num = 0
            while number != 0:
                remainder = number % 10
                reverse_num = reverse_num * 10 + remainder
                number = number // 10
            return reverse_num
        else:
            raise ValueError("Input is not an integer")
    
    def formatter(self, number):
        if type(number) is int:
            return bin(number), oct(number)
        else:
            raise ValueError("Input is not an integer")