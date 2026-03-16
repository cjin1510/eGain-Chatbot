# First thing I want to start with is define helper functions for my main function.
# Starting with the smaller functions.
# Functions with prompt parameter will allow me to reuse the function with different messages shown to the customer.
def non_empty_input(prompt):
    while True:             # while loop so we can keep looping until we get an input from the customer
        user_input = input(prompt).strip() # strip() will help us eliminate any whitespaces from the start or end
        if user_input == "": # if the customer does not enter anything, it will print:
            print ("eGainBot: I'm sorry, I didn't catch that. Please type a response: ")
        else:
            return user_input

def receive_yes_or_no(prompt): # defining a function to take in yes or no inputs from user when asking for tracking.
    while True:
        answer = input(prompt).lower() # ensure all inputs will be lowercase which will make it easier to check in if statement.

        if answer == "yes" or answer == 'y':
            return "yes" # return yes even if user typed in YES; it will return yes.
        elif answer == "no" or answer == 'n':
            return "no" # same as return yes but for return no.
        else:
            print ("eGainBot: Sorry, I didn't get that.\n Please type 'yes' or 'no': ")

# Now I want to check what type of issues the user is experiencing by giving them a simple input choice

def get_response():
    while True:   # this will loop until a correct response is given
        print (f"Thank you for contacting us! Please pick from one of these issues ")
        print ("1: My package is delayed ")
        print ("2: My package says delivered but can't find it ")
        print ("3: My package was delivered to a different address ")
        print ("4: I would like to speak to a live agent ")
        print ("5: I found my package ") # This is if the customer was contacting for support but found their package

        choice = input("Please enter 1, 2, 3, 4, or 5: ").strip() # eliminate the extra spaces incase the user presses space
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print ("eGainBot: Sorry, that is not a valid entry. ")
            print ("eGainBot: Please enter 1, 2, 3, 4, or 5.\n ")
# This function will be used when the user provides a tracking number. It will provide solutions depending on their choice.
# I will be calling functions from above so I don't have to rewrite code.
# I used prompt on earlier functions so it can take in different messages from the user
def has_tracking():
    tracking_number = non_empty_input("eGainBot: Please provide me with your tracking number: \n")
    print (f"eGainBot: Thank you for providing the tracking number '{tracking_number}'!'") # Confirming the tracking number back to customer
    print ("eGainBot: I will help you figure out the best next step. ") # Providing a solution for each issue

    choice = get_response()

    if choice == '1':
        print ("eGainBot: It looks like your package is still in transit. ")
        print ("eGainBot: Delays can happen because of weather or high shipping volume. ")
        print ("eGainBot: Please wait 24 hours and check the tracking again. ")
        print ("eGainBot: If there is still no update after 24 hours, please contact us again.")

    elif choice == '2':
        print ("eGainBot: I am very sorry that your package is marked delivered but missing.")
        print ("eGainBot: I understand that it can be very frustrating, but sometimes carrier can scan packages early.")
        print ("eGainBot: If you can please try checking your mailbox, front door, porch, garage, or apartment office.")
        print ("eGainBot: Please also ask your household members or neighbors. ")
        print ("eGainBot: If none of these options helped you, please wait 24 hours. ")
        print ("eGainBot: If it still does not appear, report it as missing. ")

    elif choice == '3':
        print ("eGainBot: I'm sorry that your package shows a different address. ")
        print ("eGainBot: In some cases, the shipment can get rerouted or return to sender. ")
        print ("eGainBot: Please contact a live agent immediately for the best solution. ")
# With more time, for choice 4, I would implement a feature to directly connect them to a live agent.
    elif choice == '4':
        print ("eGain: No problem, I can guide you there. ")
        print ("eGain: Please contact support with your tracking number or order number for the best help. ")

    elif choice == '5':
        print ("eGain: I'm glad you found your package! Please contact us again if you need any help. ")
        print ("eGain: Have a great rest of your day. ")

# This function will make sure we can still help if the customer doesn't have their tracking number
def no_tracking():
    print ("eGain: No worries! We can try another way. ")

    order_information = non_empty_input("Please enter your order number so I can look it up on my end: ")
# As of right now, since it is a simple bot, the customer can put any tracking number and the bot will take it.
# If I had more time and resources, I would implement a database to check if the order number or email is valid and then answer what the customer requested.
# For security issues, I would have the chatbot verify the customer with a one time passcode or personal account information such as name or DOB.
    print(f"eGainBot: Thank you for that! I received {order_information} as your order number.")
    print("eGainBot: If you can please check your order confirmation for any tracking information. ")
    print("eGainBot: Please look for a tracking link in your order history, or contact a live agent if you can not find the tracking information.")
    print("eGainBot: I hope one of these solutions made your day easier; have a great rest of your day! ")

# Main function to run the chatbot
def eGain_chatbot():  # Starting with a warm welcome to the customer.
    print ("Welcome to eGain's customer service chat!")
    print ("I am your assistant, eGainBot, and I will do my best to provide you a solution to your concern! ")

    customer_name = input("Can I start off with getting your name please? ").strip()
    # Creating an if statement to handle any blank names from the customer.
    if customer_name == "":
        customer_name = "Vibe" # Customers will be given a default fun name 'Vibe' if they leave it blank.
    print(f"eGainBot: Hi {customer_name}!")
    print("eGainBot: I will be here to help you with a missing or delayed package. ")

    # Requesting a tracking number from the customer
    yes_tracking = receive_yes_or_no("Do you have a tracking number? You can reply with (yes/no):\n ")
    # If the customer has a tracking number, it will direct them to the has_tracking function
    if yes_tracking == 'yes':
        has_tracking()
    else:  # else, it will direct them to the no tracking function
        no_tracking()

# Calling the main function to run.
eGain_chatbot()
