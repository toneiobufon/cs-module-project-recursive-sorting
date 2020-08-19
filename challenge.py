# Write a recursive solution to determine if a string is a valid palindrome. 
# A palindrome is a word that reads the exact same backwards as it does forwards, 
# like "racecar" for example. If the word is a valid palindrome, 
# it should return True, otherwise it should return False.
# Casing can be ignored, so "RaCeCAr" should still return True.

# def pali(str):
#     if str == str[::-1]:
        
#         return True
#     else:
#         return False

# print(pali("racecar"))
# print(pali("car"))
# print(pali("radar"))

#recursive solution
def pali(str) :
    if len(str) <= 1 :
      return True
    if str[0] == str[len(str) - 1] :
      return pali(str[1:len(str) - 1])
    else :
      return False

print(pali('racecar'))
print(pali('car'))
print(pali('radar'))