# Christopher Smith
# Chapter 13 – Lab 1
# 7/14/2025

# Recursive function to build a string
def repeat_char(char, times):
    if times <= 0:
        return ""
    else:
        return char + repeat_char(char, times - 1)

def main():
    print("Recursive Character Repeater\n")
    char = input("What character would you like to repeat? ")
    count = int(input(f"How many '{char}'s would you like: "))
    
    result = repeat_char(char, count)
    print(result)

main()
