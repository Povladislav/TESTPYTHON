#PALINDROM
def is_palindrom(word):
    if word.capitalize() == word[-1::-1].capitalize():
        return True
    return False
print(is_palindrom("шалаш"))