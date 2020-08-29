MAX  = 9999999999999

class Calc:
    def minimum (self, list):
        min = MAX
        for n in list:
            if(n < min):
                min = n
        return min

    def maximum (self, list):
        max = -MAX
        for n in list:
            if(n > max):
                max = n
        return max

    def numElements(self, list):
        num = 0
        for n in list:
            num += 1
        return num
        '''
        Decidi imṕlementar mesmo ja exisitindo uma fun que calcula
        return len(list) 
        '''

    def average(self, list):
        avr = 0
        for n in list:
            avr += n
        if (len(list) > 0):
            return avr/len(list)
        else:
            return 0

def main():
    vetor = [1, 2, 3, 4, 5]
    
    print("> minimum value = " + str(Calc.minimum(0, vetor)))
    print("> maximum value = " + str(Calc.maximum(0, vetor)))
    print("> number of elements in the sequence = " + str(Calc.numElements(0, vetor)))
    print("> average value = " + str(Calc.average(0, vetor)))


if __name__ == "__main__":
    main()
