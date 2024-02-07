#
# a = input()
# b = input()
#
#
# if __name__ == '__main__':
#     import numpy as np
#     initial_id = np.random.randint(0,3)
#     a_list = ['CLOUD', 'ALICE', 'ABCBCYA']
#     b_list = ['CUPID', 'ELIBO', 'ZBBACAA']
#     a = a_list[initial_id]
#     print(a)
#     b = b_list[initial_id]
#     print(b)
#
#
# # In[6]:
#
#
# result = []
# list_A = list(a)
# list_B = list(b)
#
# for i in range(len(list_B)):
#     list_check_A = []
#     memory_list = []
#     memory_count = 0
#     memory_count_2 = 0
#
#     temp_B = list_B[i]
#     temp_A = list_A[i]
#
#     if temp_B == temp_A:
#         result.append('P')
#
#     elif temp_B in list_A:
#         count_s_cases = 0
#         for g in range(len(list_A)):
#             if temp_B == list_A[g] and list(b)[g] != list_A[g]:
#                 count_s_cases += 1
#         count_s_cases_in_B = 0
#         list_s_cases_in_B = []
#         for g in range(len(list_A)):
#             if temp_B == list(b)[g] and list(b)[g] != list_A[g]:
#                 count_s_cases_in_B += 1
#                 list_s_cases_in_B.append(1)
#             else:
#                 list_s_cases_in_B.append(0)
#         if count_s_cases_in_B == count_s_cases:
#             result.append('S')
#         else: #*Кол-во связей было нечетным
#             #Запустим цикл по всей строке и расставим S случаи по очереди слева направо в list_s_cases_in_B
#             for g in range(len(list_A)):
#                 if list_s_cases_in_B[g] != 0:
#                     list_s_cases_in_B[g] = 0 #Найдена пара к b[i] из верхнего списка А[a[i],...a[i-1]]
#                     count_s_cases = count_s_cases - 1 #Кол-во S-связей для текущей буквы в A уменьшилось т.к. есть пара
#                     count_s_cases_in_B = count_s_cases_in_B - 1 #Кол-во S-связей для текущей буквы уменьшилось в B
#                 if count_s_cases == 0: #Если кол-во случаев S-связей для списка A с B = 0, то цикл СТОП
#                     break
#                 else: #Продолжаем искать пару к b[i] из верхнего списка А[a[i],...a[i-1]] пока count_s_cases != 0
#                     pass
#             #Проверим текущей индекс i  - совпадает с значением 1 в листке list_connected_s_cases?
#             if list_s_cases_in_B[i] == 1: #Если значение есть, то получается эта буква правее всех случаев S
#                 result.append('I')
#             else: #Если значение != 1, то получается для этой буквы есть связь в верхнем регистре
#                 #*ВАЖНО* связь условная, очень, запутанно тут
#                 result.append('S')
#     else:
#         result.append('I')
#
# print(''.join(result)) #вывод ответа
#
#
#
#
#
