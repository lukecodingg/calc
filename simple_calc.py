def add(no1, no2):
  result = no1 + no2
  print("Your solution is", result)

def subtract(no1, no2):
  if no2 > no1:
    result = no2 - no1
  else: 
    result = no1 - no2
    print("Your solution is", result)

def multiply(no1, no2):
  result = no1 * no2
  print("Your solution is", result)

def divide(no1, no2):
  result = no1 / no2
  print("Your solution is", result)

while true:
  print("""
  _________.___   _____ __________.____     ___________ _________     _____  .____   _________  
 /   _____/|   | /     \\______   \    |    \_   _____/ \_   ___ \   /  _  \ |    |  \_   ___ \ 
 \_____  \ |   |/  \ /  \|     ___/    |     |    __)_  /    \  \/  /  /_\  \|    |  /    \  \/ 
 /        \|   /    Y    \    |   |    |___  |        \ \     \____/    |    \    |__\     \____
/_______  /|___\____|__  /____|   |_______ \/_______  /  \______  /\____|__  /_______ \______  /
        \/             \/                 \/        \/          \/         \/        \/      \/ 

      
----------------------------
|      Choose one          |
|      1. Add (+)          |
|      2. Minus (-)        | 
|      3. Multiply (*)     |
|      4. Divide by (/)    |
-----------------------------
""")

choice = int(input("What is your choice?"))

if choice == 1:
  print("You chose to add")
elif choice == 2:
  print("You chose to subtract")
elif choice == 3:
  print("You chose to multiply")
elif choice == 4: 
   print("You chose to divide by")
else: 
  print("Invalid, please input numbers only")

no1 = int(input("What is your first number?"))

no2 = int(input("What is your second number?"))

if choice == 1:
  add(no1, no2)
elif choice == 2:
  subtract(no1, no2)
elif choice == 3:
  multiply(no1, no2)
elif choice == 4: 
  divide(no1, no2)
else: 
  print("Error in script")

restart = input("Press q to quit and any other key to continue.")
if restart.lower() == 'q':
    break
