#Write a function that checks if a given string is a palindrome.

def is_palindrome(given_string):
    # Convert to lowercase for case-insensitive comparison
    lower_string = given_string.lower()
    if lower_string == lower_string[::-1]:
        return f"{given_string} is palindrome"
    else:
        return f"{given_string} is not palindrome"


print(is_palindrome("madam"))
print(is_palindrome("Madam"))
print(is_palindrome("RaceCar"))