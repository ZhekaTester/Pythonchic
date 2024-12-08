lst = ['🍇','🍑','🍐','🍊','🍌','🍎']

def print_first_and_last(lst):
    if len(lst) == 0:
        print("🍇','🍑','🍐','🍊','🍌','🍎")
        return

    first_elem = lst[0]
    last_elem = lst[len(lst) - 1]

    print("Первый элемент", first_elem)
    print("Последний элемент:", last_elem)

lst = ['🍇', '🍑', '🍐', '🍊', '🍌', '🍎']
print_first_and_last(lst)