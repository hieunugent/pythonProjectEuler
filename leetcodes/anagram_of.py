# stringValue = input('please enter letter want to be anagram: ')
# def anagrams_of(string):
#     if len(string) == 1:
#         return [string[0]]
#     collection =[]
#     substring_anagrams = anagrams_of(string[1:len(string)])
#     for substring_anagram in substring_anagrams:
#         for index in range(len(substring_anagram)+1):
#             copy = substring_anagram
#             collection.append(copy[:index] + string[0] + copy[index:])
#     return collection

# print(anagrams_of(stringValue))

arrayOfString = ["a","bc","def","ghij"]
def numberofstring(arr):
    if len(arr) == 0:
        return 0
    return len(arr[0]) + numberofstring[1:len(arr)]

print(numberofstring(arrayOfString))