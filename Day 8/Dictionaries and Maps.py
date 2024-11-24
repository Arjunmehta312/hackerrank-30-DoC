# Read the number of entries in the phone book
n = int(input())

# Initialize the phone book dictionary
phone_book = {}

# Read each entry and populate the phone book
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    phone_number = entry[1]
    phone_book[name] = phone_number

# Read queries until EOF
try:
    while True:
        query = input().strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
