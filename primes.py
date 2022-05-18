def main():
    create_primes_list()


def create_primes_list():

    prime_list = set()
    for num in range(2000): 
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_list.add(num)
    


def create_matrix_prime():
    matrix = [[0] * 54 for x in range(1,300)]

    prime_matrix = matrix
    num = 0
    for y in range(len(prime_matrix)-1):
        for x in range(54):
            num +=1
            prime_matrix[y][x] = num
        consec_list = prime_matrix

    for row in range(len(consec_list)-1):
        for col in range(54):
            if consec_list[row][col] not in primeList:
                    consec_list[row][col] = ('00')
            else:
                box ="\U0001F338"
                   
                consec_list[row][col] = box


def count_digit_reduce_prime():
    pass


def cal_primes(arr):
    calc = []
    for x in arr:
        num_str = str(x).split()
        calc.append(num_str)
    return sum_digits(calc)  

def sum_digits(arr):
    
    sum_digit = []
    
    for elem in arr:
        sum_val = 0
        for digit in str(elem):
            sum_val += int(digit)

        if sum_val < 9:
            sum_digit.append(sum_val)
        else:
            new_sum = 0
            for dig in str(sum_val):
                new_sum += int(dig)

            if new_sum < 9:
                sum_digit.append(new_sum)
            else:
                an_sum = 0
                for a in str(new_sum):
                    an_sum += int(a)
                sum_digit.append(an_sum)











if __name__ == "__main__":
    main()