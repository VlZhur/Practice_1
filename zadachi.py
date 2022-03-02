def z1():
    import psutil
    from pprint import pprint
    print("Информация о системе:")
    pprint(psutil.disk_partitions())


def z2():
    import os

    i = input()
    f = open("files.txt", "w")
    f.write(i)
    f.close()
    with open("files.txt", "r") as f:
        word = f.read()
    print(word)
    os.remove("files.txt")


def z3():
    import os
    import json

    mes = input()
    to_json = {'message': mes}
    with open('file.json', 'w') as f:
        f.write(json.dumps(to_json))

    with open('file.json') as f:
        print(f.read())

    os.remove('file.json')


def z4():

    import xml.etree.ElementTree as ElementTree
    import os

    firstname = input("FirstName: ")
    secondname = input("SecondName: ")
    city = input("City: ")
    items = [
        {"firstname": firstname, "secondname": secondname, "city": city},
    ]
    root = ElementTree.Element('root')

    for i, item in enumerate(items, 1):
        person = ElementTree.SubElement(root, 'person' + str(i))
        ElementTree.SubElement(person, 'firstname').text = item['firstname']
        ElementTree.SubElement(person, 'secondname').text = item['secondname']
        ElementTree.SubElement(person, 'city').text = item['city']

    tree = ElementTree.ElementTree(root)
    tree.write('xmlf.xml')

    with open('xmlf.xml') as f:
        print(f.read())

    os.remove('xmlf.xml')


def z5():

    import os
    import zipfile

    i = input()
    newzip = zipfile.ZipFile('file.zip', 'w')
    f = open("file.txt", "w")
    f.write(i)
    f.close()
    newzip.write('file.txt')
    os.remove("file.txt")
    while True:
        x = int(input("Показать содержимое файла: 1=да, 2=извлечь файл, 3=удалить"))
        if x == 0:
            break
        elif x == 1:
            newzip.printdir()
        elif x == 2:
            newzip.extract('file.txt')
            with open("file.txt", "r") as ft:
                y = ft.read()
                print(y)
                ft.close()
        elif x == 3:
            newzip.close()
            os.remove("file.zip")
            try:
                os.remove("file.txt")
            except FileNotFoundError:
                pass
            else:
                os.remove("file.txt")
            break



