print("\033[32m")

def add(no1, no2):
  result = no1 + no2
  print("Your solution is", result)

def subtract(no1, no2):
  if no2 > no1:
    result = no2 - no1
    print("Your solution is", result)
  else: 
    result = no1 - no2
    print("Your solution is", result)

def multiply(no1, no2):
  if no2 == 0:
    print("You can't divide with zero")
  elif no1 == 0:
    print("You can't divide with zero")
  else:
    result = no1 * no2
    print("Your solution is", result)

def divide(no1, no2):
  result = no1 / no2
  print("Your solution is", result)

while True:
    print("""
  _________.___   _____ __________.____     ___________ _________     _____  .____   _________  
 /   _____/|   | /     \\______   \\    |    \\_   _____/ \\_   ___ \\   /  _  \\ |    |  \\_   ___ \\ 
 \\_____  \\ |   |/  \\ /  \\|     ___/    |     |    __)_  /    \\  \\/  /  /_\\  \\|    |  /    \\  \\/ 
 /        \\|   /    Y    \\    |   |    |___  |        \\ \\     \\____/    |    \\    |__\\     \\____
/_______  /|___\\____|__  /____|   |_______ \\/_______  /  \\______  /\\____|__  /_______ \\______  /
        \\/             \\/                 \\/        \\/          \\/         \\/        \\/      \\/ 

----------------------------
|      Choose one          |
|      1. Add (+)          |
|      2. Minus (-)        | 
|      3. Multiply (*)     |
|      4. Divide by (/)    |
----------------------------
""")

        choice = int(input("What is your choice? "))
        no1 = int(input("What is your first number? "))
        no2 = int(input("What is your second number? "))
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        continue  
    
    if 1 <= choice <= 4:
        if choice == 1:
            print("You chose to add")
            add(no1, no2)
        elif choice == 2:
            print("You chose to subtract")
            subtract(no1, no2)
        elif choice == 3:
            print("You chose to multiply")
            multiply(no1, no2)
        elif choice == 4:
            print("You chose to divide")
            divide(no1, no2)
    else:
        print("Please choose a number between 1 and 4")
        continue 
    
    restart = input("\nPress 'q' to quit or any other key to continue: ")
    if restart.lower() == 'q':
        break
      
print("\033[0m")
