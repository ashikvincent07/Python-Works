def square_list(numbers):
    squares = []

    for num in numbers:
        squares.append(num**2)

    return squares


print(square_list([1, 3, 4, 2]))