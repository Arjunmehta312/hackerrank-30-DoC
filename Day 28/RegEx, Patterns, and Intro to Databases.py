import re

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    for _ in range(N):
        first_name, email_id = input().rstrip().split()
        
        # Check if the email ID ends with "@gmail.com"
        if re.search(r'@gmail\.com$', email_id):
            gmail_users.append(first_name)
    
    # Sort the list alphabetically
    gmail_users.sort()
    
    # Print each name on a new line
    for name in gmail_users:
        print(name)
