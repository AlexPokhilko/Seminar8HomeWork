
path = 'PhoneBook.txt'

def read_pb():
    list1 = []
    with open(path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count +=1
            l = line.strip()
            l = l.split(";")
            l.pop()
            l = [i.strip() for i in l]
            # print(l)
            s = (' '.join(map(str, l)))
            print(str(count) + " "+s)
    return

read_pb()
print()

def get_contact():
    count = 0
    n = int(input("Введите номер контакта для копирования: "))
    print()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            count +=1
            if count == n:
                contact = list(line.split("; "))
                return contact
    return "Контакта с таким номером в списке нет"

contact = get_contact()
# print(contact)
# print(type(contact))


def copy_contact(l):
    c = str(l[0]) + str(l[1])[0] + str(l[2])[0]
    print("Контакт скопирован в файл " + c +".txt")
    print()
    with open(c+'.txt', 'w', encoding='utf-8') as file:
        s = ('; '.join(map(str, l)))
        file.write(s)
    
    return s
    
print(copy_contact(contact))

# path = 'PhoneBook.txt'
# # data = open(path, 'r', encoding='utf-8')
# with open('PhoneBook.txt', 'r', encoding='utf-8') as data:
#     for line in data:
#         print(line)
# # data.close()