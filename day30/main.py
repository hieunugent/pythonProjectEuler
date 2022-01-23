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
# except KeyError as error_mssage:
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
         
facebook_post =[
    {'Like':1, 'Comment':10, 'Share':5},
    {'Like':1, 'Comment':5, 'Share':3},
    { 'Comment':2, 'Share':1},
    {'Like':1, 'Comment':15},
    {'Like':1, 'Comment':12},
    {'Like':1, 'Share':2},
    ]

def numberofLike(fbpost):
    total_like = 0
    for post in fbpost:
        try:     
            currentlike = post['Like']
        except KeyError:
            total_like += 0
        else:
            total_like += currentlike
    return total_like

print(numberofLike(facebook_post))