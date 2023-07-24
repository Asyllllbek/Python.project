list=[]
while True:
    print('Выберите действие:')
    print("1. Добавить задачу")
    print("2. Ввести список задач")
    print("3. Удалить задачу")
    print("0. Выйти")
    user=int(input())
    if user==1:
        print("Введите задачу для планирования:")
        plus_list=input()
        list.append(plus_list)
    elif user==2:
        counter = 0
        for el_list in list:
            counter = counter + 1
            print(counter, el_list)
    elif user==3:
        counter = 0
        for el_list in list:
            counter = counter + 1
            print(counter, el_list)
        print("выберите план")
        help=int(input())
        #print(list[help])
        #minus_list = input()
        list.remove(list[help-1])
    else:
        print('вы вышли')
        break










list=[]
def add_task():
    print("Введите задачу для планирования:")
    plus_list = input()
    list.append(plus_list)
def withdraw_task():
    counter = 0
    for el_list in list:
        counter = counter + 1
        print(counter, el_list)
def delete_task():
    print("выберите план")
    help = int(input())
    # print(list[help])
    # minus_list = input()
    list.remove(list[help - 1])
while True:
    print('Выберите действие:')
    print("1. Добавить задачу")
    print("2. Ввести список задач")
    print("3. Удалить задачу")
    print("0. Выйти")
    user=int(input())
    if user==1:
        add_task()
    elif user==2:
        withdraw_task()
    elif user==3:
        withdraw_task()
        delete_task()
    else:
        print('вы вышли')
        break