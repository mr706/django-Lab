print("Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client their name and save it to a variable.
Name=str(input("enter your name: "))
print("Hello," + str (Name))
# TODO: Write code to ask the client their savings and save it to another variable.
savings= int(input ("How much do you have in your savings?"))
print()
# TODO: Write code to ask the client the stock they is interested in and save it to another variable, as shown below.
stock = (input("Which stock are you interested in? Type 'amzn' for Amazon, 'apl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft."))
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200
buy = 0

#Your code should look like this:
if stock == "amzn":
    buy= savings/amazon
    print(int(buy))
elif stock == "fb" or "Facebook":
    buy = savings/fb
    print(int(buy))
elif stock == "msft" or "microsoft":
    buy = savings/msft
    print(int(buy))
elif stock == "google" or "goog":
    buy=savings/google
    print(int(buy))
elif stock == "apl" or "apple":
    buy= savings/apple
    print(int(buy))

#print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
result = Name + " has $ " + str(savings) + " and they can buy " + str (buy) + "shares of " + stock

print(result)
# Alex has $5000 in savings and they can buy 50 shares of Apple.