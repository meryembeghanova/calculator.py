# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "Hi! 👋 What's your name?" + RESET)
name = input(GREEN + "> " + RESET)

print(YELLOW + f"\nNice to meet you, {name}! 😊" + RESET)

print(BLUE + "\nHow are you feeling today?" + RESET)
feeling = input(GREEN + "> " + RESET)

print(MAGENTA + "\nOh, I see. Thanks for sharing that." + RESET)

print(RED + "\nHow was your day today?" + RESET)
day = input(GREEN + "> " + RESET)

print(CYAN + "\nDid you do anything interesting today?" + RESET)
activity = input(GREEN + "> " + RESET)

print(YELLOW + "\nThat sounds nice!" + RESET)

print(BLUE + "\nWhat are you doing right now?" + RESET)
now = input(GREEN + "> " + RESET)

print(MAGENTA + "\nCool 😎" + RESET)

print(RED + "\nDo you like programming?" + RESET)
programming = input(GREEN + "> " + RESET)

print(CYAN + "\nThat's awesome! Python is fun, right?" + RESET)

print(YELLOW + f"\nIt was really nice chatting with you, {name} 💙" + RESET)
print(GREEN + "Have a great day! 🌟" + RESET)
