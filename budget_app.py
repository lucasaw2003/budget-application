def main(): 

    while True: 
        try: 
            savings_level = int(input('please enter a savings level: '))
            assert savings_level in [1, 2, 3]
        except AssertionError: 
            print('please enter a valid level (1, 2, or 3)')
        else: 
            break

    while True: 
        try: 
            income = int(input('please enter your income: '))
        except TypeError: 
            print('please enter a number')
        else: 
            break

    line_items = budgetize(savings_level, income)
    for line, amount in line_items.items():
        print(f'{line}: ${amount:.2f}')
        print()

def budgetize(level, income):
    income /= 12 
    level1 = {'housing': .30, 'food': .15, 'transport': .10, 'insurance': .10, 'personal': .10, 'recreation': .05, 'utilities': .05, 'misc': .05, 'savings': .10}
    level2 = {'housing': .275, 'food': .125, 'transport': .05, 'insurance': .05, 'personal': .05, 'recreation': .025, 'utilities': .025, 'misc': .025, 'savings': .35}
    level3 = {'housing': .25, 'food': .10, 'transport': .025, 'insurance': .025, 'personal': .025, 'recreation': .01, 'utilities': .01, 'misc': .01, 'savings': .545}
    res = {}

    if level == 1:
        for item in level1:  
            cost = level1[item] * income
            res[item] = cost
    elif level == 2:
        for item in level2:  
            cost = level2[item] * income
            res[item] = cost
    else: 
        for item in level3: 
            cost = level3[item] * income
            res[item] = cost

    return res

if __name__ == "__main__": 
    main()