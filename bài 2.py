def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            return i
        
        left_sum += arr[i]
    
    return -1

def main():
    try:
        input_sequence = input("Enter the array elements separated by spaces: ")
        input_array = [int(num) for num in input_sequence.split()]

        equilibrium_index = find_equilibrium_index(input_array)

        if equilibrium_index != -1:
            print(f"YES, there is an equilibrium index at {equilibrium_index}.")
        else:
            print("NO, there is no equilibrium index.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
