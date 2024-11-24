# Number of test cases
T = int(input().strip())

# Iterate over each test case
for _ in range(T):
    S = input().strip()  # Read each string
    even_chars = S[0::2]  # Characters at even indices
    odd_chars = S[1::2]   # Characters at odd indices
    print(f"{even_chars} {odd_chars}")  # Print the result as per the format
