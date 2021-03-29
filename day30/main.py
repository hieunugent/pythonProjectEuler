# # with open('a_file.txt') as file:
# #     file.read()

# # FILEnot found error
# # Key Error
# # Index Error
# # type eror
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


