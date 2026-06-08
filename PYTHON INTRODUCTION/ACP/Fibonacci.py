def fibonacci_recursive(n):
    """
    Returns the n-th Fibonacci number using recursion.
    Base cases: n = 0 -> 0, n = 1 -> 1
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # The recursive step: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def print_fibonacci_sequence(terms):
    """Prints the Fibonacci sequence up to a specified number of terms."""
    if terms <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    print(f"Fibonacci sequence up to {terms} terms:")
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")
    print()  



print_fibonacci_sequence(10)