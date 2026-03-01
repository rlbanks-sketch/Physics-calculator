import main
def safe_float_input(prompt, positive=False, zero_allowed=False):
    while True:
        try:
            val = float(input(prompt))
            if positive and val <= 0:
                print("Value must be positive.")
                continue
            if not zero_allowed and val == 0:
                print("Zero is not allowed.")
                continue
            return val
        except ValueError:
            print("Invalid number, try again.")