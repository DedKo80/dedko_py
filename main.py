import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Скажите что-нибудь")
    audio = r.listen(source)

try:
     print(r.recognize_google(audio, language="ru-RU"))
except sr.UnknownValueError:
    print("Робот не расслышал фразу")
except sr.RequestError as e:
    print("Ошибка сервиса; {0}".format(e))

# import linecache
# import random
# # print(linecache.getline('sample2.txt', 5))
# # Задаем наборы символов для настройки уровня сложности пароля
# char_set_en = ''.join(chr(i) for i in range(97, 123))
# char_set_EN = ''.join(chr(i) for i in range(65, 91))
# char_set_nmb = ''.join(chr(i) for i in range(48, 58))
# char_set_symb = "!#$%&()*+-/:;<=>?@"
#
# char_set_list = [char_set_en, char_set_EN, char_set_nmb, char_set_symb]
#
# char_set = ''
#
# #
# level_pass_dif = 3
# for ch in char_set_list[:level_pass_dif]:
#     char_set += ch
#
#
# print(char_set)
# def gen_password(n = 8):
#     return ''.join(random.choice(char_set) for i in range(n))

# print(gen_password(15))


# with open('sample2.txt', 'w') as my_file:
#     for i in range(50):
#         my_file.write(str(i) + ' ' + str(i ** 2) + '\n')
#
# with open('sample2.txt') as my_file:
#     lst = []
#     print(my_file.)
    # for i in my_file:
    #     lst.append(my_file.readline().strip())

# st1 = "13 169"
#
# print([int(i) for i in st1.split()])
#
# lst = []
# for i in st1.split():
#     lst.append(int(i))
#
# print(lst)



# import random
#
#
# def new_point():
#     return [random.randint(-100, 100), random.randint(-100, 100)]
#
#
# def new_point_list(file_name):
#     with open(file_name, 'w') as mi_file:
#         for i in range(100):
#             # mi_file.write(str(random.randint(-100, 100)) + ' ' + str(random.randint(-100, 100)) + '\n')
#             mi_file.write(' '.join(str(x) for x in new_point()) + '\n')
#
#
# def load_points(f_name):
#     point_list = []
#     with open(f_name) as mi_file:
#         for i in mi_file:
#             point = [int(p) for p in mi_file.readline().strip().split()]
#
#             point_list.append(point)
#     return point_list
#
# def generate_random_str_code():
#     st = ''
#     for i in range(random.randint(5, 15)):
#         cnt = random.randint(0, 100)
#         ch = chr(random.randint(65, 90))
#         st += cnt * ch
#     return st
#
# def arch_str(string):
#     res = ''
#     cnt = 0
#     ch1 = string[0]
#     for i in range(len(string)):
#         if string[i] != ch1:
#             res += str(cnt) + ch1
#             cnt = 1
#             ch1 = string[i]
#         else:
#             cnt += 1
#     return res + str(cnt) + ch1
#
#
# rnd_str = generate_random_str_code()
# print(rnd_str)
# print(arch_str(rnd_str))

# new_point_list('points.in')
# print(load_points('points.in'))

# in_str = '      28 -41   \n      '
# print(in_str)
#
# in_str = in_str.strip()
# print(in_str)
#
# in_str = in_str.split()
# print(in_str)
#
# in_str = [int(s) for s in in_str]
# print(in_str)




