# #!/usr/bin/env python
# # coding: utf-8
#
# # In[1]:
#
#
# input_list = input()
# PRICE_LESS_THAN = input()
# DATE_AFTER = input()
# NAME_CONTAINS = input()
# PRICE_GREATER_THAN = input()
# DATE_BEFORE = input()
#
#
# # In[2]:
#
#
# import json
# import time
#
#
# # In[3]:
#
#
# if __name__ == '__main__':
#     input_list = [{"id": 1, "name": "Asus notebook","price": 1564,"date": "23.09.2021"},{"price": 2500, "id": 3, "date": "05.06.2020", "name": "Keyboardpods" }, {"date": "23.09.2021", "name": "Airpods","id": 5, "price": 2300}, {"name": "EaRPoDs", "id": 2, "date": "01.01.2022", "price": 2200}, { "id": 4, "date": "23.09.2021", "name": "Dell notebook",  "price": 2300}]
#     PRICE_LESS_THAN = 2400
#     DATE_AFTER = '23.09.2021'
#     NAME_CONTAINS = 'pods'
#     PRICE_GREATER_THAN = 2200
#     DATE_BEFORE = '02.01.2022'
#
#
# # In[4]:
#
#
# new_test = list(input_list)
#
#
# # In[5]:
#
#
# #Переводим время в формат time date/month/year
# DATE_AFTER = DATE_AFTER.replace('.','/')
# DATE_AFTER = time.strptime(DATE_AFTER, "%d/%m/%Y")
# DATE_BEFORE = DATE_BEFORE.replace('.','/')
# DATE_BEFORE = time.strptime(DATE_BEFORE, "%d/%m/%Y")
#
#
# # In[6]:
#
#
# size_json = len(new_test)
# list_id = []
# for i in range(size_json):
#     temp_json = new_test[i]
#     if NAME_CONTAINS in temp_json['name'].lower():
#         if temp_json['price'] <= PRICE_LESS_THAN and temp_json['price'] >= PRICE_GREATER_THAN:
#             json_data = temp_json['date'].replace('.','/')
#             json_data = time.strptime(json_data, "%d/%m/%Y")
#             if DATE_AFTER >= json_data and json_data <= DATE_BEFORE:
#                 list_id.append([i,temp_json['id']])
#
# new_sort_list = sorted(list_id, key=lambda x: x[1])
# output_list_json = []
# for i in range(len(new_sort_list)):
#     id_sort = new_sort_list[i][0]
#     output_list_json.append(new_test[id_sort])
# print(output_list_json)
#
