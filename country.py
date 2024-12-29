country={"America":"Washington DC","India":"Mumbai","China":"Beijing","Nepal":"Kathmandu"}
def ask():
    user_country=input("enter the country of which capital you want to know:".strip().lower())
    user_country=user_country.capitalize()
    
    if user_country in country:
        print(f"the capital of {user_country} is {country[user_country]}.")
    else:
        print("New country Detected!")
        capital=input(f"enter the capital of {user_country}:").strip().capitalize()
        country[user_country]=capital
ask()
print(country)