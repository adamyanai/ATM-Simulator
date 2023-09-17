# Atlantic Bank Customers

bankcustomers_dict = {
    'names' : ["Alex", "Jane"],
    "Alex" : {'password' : "ilovedogs",
                  'total account balance' : 1000,
                  'savings' : 400,
                  'spendings' : 600
              },
    "Jane" : {'password' : "ilovecats",
                  'total account balance' : 2000,
                  'savings' : 1500,
                  'spendings' : 500
              }
}

# Welcome message for Atlantic Bank ATM.
atlantic_bank = 1
while atlantic_bank == 1:
  print("Hello! Welcome to Atlantic Bank.")

# Login to bank account.

  logged_in = 0
  while logged_in == 0:
    y = input("What is your name?")
    if y in bankcustomers_dict['names']:
      z = input("Now what's your password?")
      if z == bankcustomers_dict[y]['password']:

# Once logged in, displays the account information.

        print("Welcome back,", y, ". Here is your account information.")
        print("Total Account Balance: $", bankcustomers_dict[y]["total account balance"])
        print("Savings: $", bankcustomers_dict[y]["savings"])
        print("Spendings: $", bankcustomers_dict[y]["spendings"])

# Then, the "main menu" is presented where the user can choose their action.

        in_main_menu = 1
        while in_main_menu == 1:
          in_DWTL = 1
          while in_DWTL == 1:
            a = input("Now, would you like to (D) deposit, (T) transfer, (W) withdraw, or (L) logout?")

# The user is asked a series of questions, depending on their selection.
# The questions enable to program to complete the transaction wanted by the user.

            change_in_spendings = 0
            change_in_savings = 0


            if a == "D" or a == "d":
              b = int(input("What is the amount which you would like to deposit? Note that it must be a positive integer."))
              x = input("Would you like to deposit this amount into your spendings or savings account?")
              if x == "spendings":
                change_in_spendings = b

              if x == "savings":
                  change_in_savings = b

            if a == "W" or a == "w":
              b = int(input("What is the amount which you would like to withdraw? Note that it must be a positive integer."))
              x = input("Would you like to withdraw this amount from your spendings or savings account?")
              if x == "spendings":
                  change_in_spendings = -1 * b
              if x == "savings":
                  change_in_savings = -1 * b

            if a == "T" or a == "t":
              b = int(input("What is the amount which you would like to transfer? Note that it must be a positive integer."))
              x = input("Would you like to transfer this amount from your spendings or savings account?")
              if x == "spendings":
                  change_in_spendings = -1 * b
                  change_in_savings = b
              if x == "savings":
                  change_in_savings = -1 * b
                  change_in_spendings = b

# The user additionally has the option to "logout" at any time.
# If the user opts to logout, the program resets, but saves that users updated account information.
 
            if a == "L" or a == "l":
              print("Logout Successful.")
              in_main_menu = 0
              print("Hello! Welcome to Atlantic Bank.")
              in_DWTL = 0

# After every transaction, the program checks if the transaction is valid.

            if in_DWTL:
              
              if change_in_spendings + bankcustomers_dict[y]["spendings"] < 0:
                print("Sorry! Not enough money in spendings account.")
              elif change_in_savings + bankcustomers_dict[y]["savings"] < 0:
                print("Sorry! Not enough money in savings account.")

# Once the transaction is validated, the account information is updated.

              else: 
                bankcustomers_dict[y]["savings"] = bankcustomers_dict[y]["savings"] + change_in_savings
                bankcustomers_dict[y]["spendings"] = bankcustomers_dict[y]["spendings"] + change_in_spendings
              
              bankcustomers_dict[y]["total account balance"] = bankcustomers_dict[y]["savings"] + bankcustomers_dict[y]["spendings"]

# After every transaction, the user is given their updated account information.

              print("Your current Total Account Balance is $", bankcustomers_dict[y]["total account balance"])
              print("Your current Savings Account Balance is $", bankcustomers_dict[y]["savings"])
              print("Your current Spendings Account Balance is $", bankcustomers_dict[y]["spendings"])


      else: print("Incorrect password! Please try again.")
    else: print("User not found. Please try again.")
