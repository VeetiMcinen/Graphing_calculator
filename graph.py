def render(equation: str, matrix_size: int):
    led_matrix = {}
    pixels_to_render = []
    
    def evaluate_equation(x):
        # Evaluate the equation safely with error handling
        try:
            return eval(equation, {"x": x})
        except Exception as e:
            print(f"Error evaluating equation: {e}")
            return None  # Return None if there's an error

    for x in range(-127, 128):
        y = evaluate_equation(x)
        if y is not None and -127 <= y <= 127:  # Ensure y is within the valid range
            index = (3 - y) * matrix_size + (x + 3)
            if index >= 0 and index < matrix_size * matrix_size:
                led_matrix[index] = True  # Only store True values

    # Collect all turned on LED coordinates
    for index in led_matrix:
        x = (index % matrix_size) - 3
        y = 3 - (index // matrix_size)
        pixels_to_render.append((x, y))

    return pixels_to_render

# Set matrix size and call the render function
matrix_size = 256  # This needs to be defined appropriately based on actual usage
equation = "x"
pixels = render(equation, matrix_size)
print(pixels)
