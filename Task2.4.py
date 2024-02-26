4 Дана строка. Необходимо проверить, является ли она палиндромом.
def palindrome(s):
    d = str()
    s = s.lower().replace(" ", "")
    d = s[::-1]
    if d == s:
        return True
    else:
        return False


string1 = input()
if palindrome(string1) == True:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
