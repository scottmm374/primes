import math

def main():
    primes_result = create_primes_list(1000)
    len_primes = primes_result[0]
    # Checks len of qty for primes
    print(len(len_primes))
    print((prime_set))
    print((num_range))
    print(num_range)

    lines, cols = calc_lines(num_range, 54)
    print(lines)
    y = create_matrix_prime(prime_set, lines, cols)
    print(y)



def create_primes_list(n):

    prime_list = set()
    for num in range(n): 
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_list.add(num)
    sorted_list = list(prime_list)
    return sorted_list, prime_list, num
    
#  calculate the number or rows needed for number range
def calc_lines(nums, cols):
    line_number = math.ceil(nums / cols)
    return line_number, cols

def create_matrix_prime(prime_set, lines, columns):

    matrix = [[0] * columns for x in range(1,lines)]
    num_list = None
    prime_matrix = matrix
    num = 0
    for y in range(len(prime_matrix)-1):
        for x in range(columns):
            num +=1
            prime_matrix[y][x] = num
        num_list = prime_matrix

    for row in range(len(num_list)-1):
        for col in range(columns):
            if num_list[row][col] not in prime_set:
                    num_list[row][col] = ('00')
            else:
                box ="\U0001F338"
                   
                num_list[row][col] = box
    return num_list
    


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