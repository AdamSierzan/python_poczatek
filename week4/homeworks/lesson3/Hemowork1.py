def run_example():

    multiple_of_three = [num for num in range(1,31) if num % 3 == 0]
    print(multiple_of_three)

    multiple_of_five = [num for num in range(1,31) if num % 5 == 0]
    print(multiple_of_five)

    result = multiple_of_three + multiple_of_five
    print(result)
run_example()