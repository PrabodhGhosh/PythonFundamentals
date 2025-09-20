"""Program that generates the first n numbers in the Fibonacci sequence."""

def print_fibonacci(num):
    """Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        num: Number of Fibonacci numbers to generate
        
    Returns:
        List containing the first n Fibonacci numbers
    """
    if num <= 0:
        return []
    if num == 1:
        return [0]
    series = [0, 1]
    a = 0
    b = 1

    for i in range(2, num):
        c = a + b
        a = b
        b = c
        series.append(c)
    return series


print(print_fibonacci(5))