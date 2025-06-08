def lower_triangle(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

def upper_triangle(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)
    print()

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()

# Number of rows
rows = 5

lower_triangle(rows)
upper_triangle(rows)
pyramid(rows)
