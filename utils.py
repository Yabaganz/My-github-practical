#formatting price with Naira and kobo.

#price contain currency naira value and kobo(2 decimal place) e.g  ₦55.56k
def format_price(price: float) -> str:
    return f"₦{price:,.2f}k"

# get user input validation

def input_int(prompt: str, least_value: int = None, highest_value: int = None) -> int:
    
    while True:
        try:
            numb = int(input(prompt).strip())
            if least_value is not None and numb < least_value:
                print(f"Number must be at least {least_value}")
                continue
            if highest_value is not None and value > highest_value:
                print(f"Number must not exceed {highest_value}")
                continue
            return numb
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display list of menu items with header attach to it
       
def print_menu(options: list, header: str = None) -> None:
    if header:
        print(f"\n~~~{header}~~~")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    