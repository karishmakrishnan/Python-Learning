email = "john.doe@example.com"

email_len = len(email)
i = 0
Username = str()
Domain = str()

while (i < email_len):
    if(email[i] == "@"):
        Username = email[:i]
        Domain = email[i+1:]
        break
    i = i+1

print(f"Username: {Username}")
print(f"Domain: {Domain}")

