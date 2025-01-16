def create_ascii_triangle(height):
    """
    Creates an ASCII triangle of the specified height.

    Args:
        height (int): The height of the triangle.

    Returns:
        str: A string representation of the triangle.
    """
    triangle = ""
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        triangle += spaces + stars + '\n'
    return triangle

if __name__ == "__main__":
    def get_height():
        """
        Retrieve the height of the triangle from the user.
        Replace input() with a function parameter for environments without interactive input.

        Returns:
            int: The height of the triangle.
        """
        # Default value for non-interactive environments
        return 5

    try:
        height = get_height()
        if height <= 0:
            print("Please enter a positive integer.")
        else:
            print(create_ascii_triangle(height))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
