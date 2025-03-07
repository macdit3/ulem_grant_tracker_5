# main.py
# ULEM grant tracker app

# Create a list to hold all grant dictionaries
total_grants = []

# Keep asking for grant's information
while True:
    grant_name = input('Enter a grant name: ')
    amount = float(input('Enter the amount: '))
    source = input('Enter the grant source: ')
    grant_recipient = input('Name of the recipient: ')
    date_awarded = input('Date Awarded: ')
    print()

    # Store the entries in a dictionary
    entity = {
        "grant_name": grant_name,
        "amount": amount,
        "source": source,
        "grant_recipient": grant_recipient,
        "date_awarded": date_awarded,
    }

    # Add the grant to the list of grants
    total_grants.append(entity)

  
    # Ask the user if they want to exit the program
    user_exit = input("Do you have more grants to add? (y/n): ")
    if user_exit.lower() == "n":
          # 3. Display all the grant info "????"
        print("Thank you, all grant info saved 🎉🎉🎉")
        break
        

# Use a for-loop statement to display all grants
print("ALL GRANT INFORMATION:")

for grant in total_grants:
    print(f"Grant Name: {grant['grant_name']}")
    print(f"Amount: {grant['amount']}")
    print(f"Source: {grant['source']}")
    print(f"Grant Recipient: {grant['grant_recipient']}")
    print(f"Date Awarded: {grant['date_awarded']}")
    print()
