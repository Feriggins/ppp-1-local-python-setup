def hello():
    print("Hello, user!")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")

# Demonstrating the functions
hello()
packed_list = pack("apple", "sandwich", "cookie")
print(packed_list)

eat_lunch(["apple", "sandwich", "cookie"])
eat_lunch([])