def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

# Example usage
if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Sum:", add(x, y))
