# # with open('a_file.txt') as file:
# #     file.read()

# # FILEnot found error
# # Key Error
# # Index Error
# # type error
# # text = "abx"
# # print(text + 5)
# from pip._vendor.pep517.compat import FileNotFoundError

# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open('a_file.txt', "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The Key {error_message} this is key error")
# else:
#     content= file.read()
#     print(content)
# finally:
#     raise TypeError("this is the error i make up")
def bmi():
    height = float(input("height: "))
    weight = float(input("weight: "))
    if height > 3:
        raise ValueError("height is too big")

    bmi = weight / (height ** 2)
    print(bmi)

fruits= ["apple", "banana", "cherry"]
def make_pie(index):
    try:  
         fruit = fruits[index]
    except IndexError:
        print("Index is out of range")
    else:
         print(f"making pie with {fruit}")

make_pie(2)
make_pie(4)