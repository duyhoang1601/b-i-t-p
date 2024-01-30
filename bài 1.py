def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_sequence(sequence):
    primes = [num for num in sequence if is_prime(num)]
    return primes

def find_largest_prime(sequence):
    primes = find_primes_in_sequence(sequence)
    if primes:
        return max(primes)
    else:
        return None

def main():
    try:
        input_sequence = input("Enter a sequence of positive integers separated by spaces: ")
        input_list = [int(num) for num in input_sequence.split()]
        
        if all(num > 0 for num in input_list):
            prime_numbers = find_primes_in_sequence(input_list)
            largest_prime = find_largest_prime(input_list)
            
            print("Prime numbers in the sequence:", prime_numbers)
            
            if largest_prime is not None:
                print("Largest prime number in the sequence:", largest_prime)
            else:
                print("No prime numbers found in the sequence.")
        else:
            print("Please enter valid positive integers.")

    except ValueError:
        print("Invalid input. Please enter a sequence of positive integers.")

if __name__ == "__main__":
    main()
