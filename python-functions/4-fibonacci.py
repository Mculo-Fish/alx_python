def fibonacci_sequence(n):
    if n <= 0:
        return ('Please provide a positive value')
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibonacci_list = [0, 1]
        for _ in range(2, n):
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)

        return fibonacci_list
    
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))