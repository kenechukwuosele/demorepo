# name = input()
# if name == 'Mary':
#     print('Hello Mary')
#     password = input()
#     if password == 'swordfish':
#         print('Access granted.')
#     else:
#         print('Wrong password.')

# spam = 0
# # if spam < 5:
# #     print('Hello, world.')
# #     spam = spam + 1spam = 0

# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1


# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
#     print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        print('Access granted.') 
    else :
        break
        print('Access denied')