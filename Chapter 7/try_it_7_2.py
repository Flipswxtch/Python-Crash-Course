party_size = input("Hello, how many people in are in your party? ")

if int(party_size) > 8:
    print(f"We don't have a table ready for {party_size} people right now")
    print(f"Please, have a seat in the lobby and we'll notify you when it's ready")
else:
    print(f"We have a table ready for you now. Please, follow me.")