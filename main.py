import art

print(art.logo)
print("Welcome to the secret auction program.")

auction = {}
bidders = "yes"
winner = {"name": "", "value": 0}

while bidders == "yes":
    name = input("What is your name?: ")
    amount = float(input("What's your bid?: $"))
    auction[name] = amount
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.")


for key in auction:
    if auction[key] > winner["value"]:
        winner["value"] = auction[key]
        winner["name"] = key

print(f"The winner is: {winner}")
