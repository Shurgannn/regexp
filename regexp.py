from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_contacts = {}
  for row in contacts_list:
    fio = re.split('\s+', row[0] + ' ' + row[1] + ' ' + row[2])
    if '' in fio:
      fio.remove('')
    # print(row)
    phone_number = row[5]
    phone_pattern = "(8|\+7)?(\s)*(\(\d+\))(\s)*(\d+)([-\s])(\d+)([-\s])(\d+)\s(\(?)([а-я]+)(.)\s(\d+)\)?"
    correct_phone_number = re.sub(phone_pattern, r"+7\3\5-\7-\9 \11\12\13", phone_number)
    # fio.remove(fio[0]) # почему нельзя сразу задать io = fio.remove(fio[0])???
    # io = fio
    # list = [fio[1], fio[2], row[3], row[4], correct_phone_number]
    # new_contacts[fio[0]] = list
    #print(new_contacts)
  # pprint(new_contacts)
    d = {}
    d[row[0]] = row
    for k, v in d.items():
      if k not in new_contacts.keys():
        new_contacts.update(d)
      # else:
      #   print(v)
      #   print(new_contacts.values())
  pprint(new_contacts)

#pprint(contacts_list)



# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding='utf-8') as f:
#  datawriter = csv.writer(f, delimiter=',')
#  # Вместо contacts_list подставьте свой список
#  datawriter.writerows(new_contacts_list)