# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_contacts = {}
  new_contacts_list = []
  for row in contacts_list:
    fio = re.split('\s+', row[0] + ' ' + row[1] + ' ' + row[2])
    if '' in fio:
      fio.remove('')
    # print(fio)
    phone_number = row[5]
    phone_pattern = "(8|\+7)?(\s)*(\(\d+\))(\s)*(\d+)([-\s])(\d+)([-\s])(\d+)\s(\(?)([а-я]+)(.)\s(\d+)\)?"
    correct_phone_number = re.sub(phone_pattern, r"+7\3\5-\7-\9 \11\12\13", phone_number)
    key = fio[0] + '_' + fio[1]
    contact = {}
    if len(fio) > 2:
      contact['surname'] = fio[2]
    else:
      contact['surname'] = ''
    contact['organization'] = row[3]
    contact['position'] = row[4]
    contact['phone'] = correct_phone_number
    contact['email'] = row[6]
    if key not in new_contacts:
      new_contacts[key] = {}
      if len(fio) > 2:
        new_contacts[key]['surname'] = fio[2]
      new_contacts[key]['organization'] = row[3]
      new_contacts[key]['position'] = row[4]
      new_contacts[key]['phone'] = correct_phone_number
      new_contacts[key]['email'] = row[6]
    else:
      for k, v in contact.items():
        if v not in new_contacts[key].values():
          del new_contacts[key][k]
      for k, v in new_contacts[key].items():
        if v not in contact.values():
          del contact[k]
      new_contacts[key].update(contact)
  for k, v in new_contacts.items():
    contact_list = []
    fi = k.split('_')
    for c in fi:
        contact_list.append(c)
    for i in v.values():
      contact_list.append(i)
    # print(contact_list)
    new_contacts_list.append(contact_list)
  pprint(new_contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
 datawriter = csv.writer(f, delimiter=',')
 # Вместо contacts_list подставьте свой список
 datawriter.writerows(new_contacts_list)