'''
CS50P Week 2 - Coke Machine
A program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
and how many cents in change it's owe
'''

def coke():
    cost = 50
    coins = [5, 10, 25]
    total_coins = 0
    amount_due = cost - total_coins

    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin = int(input("Insert Coin: "))
        if coin not in coins:
            continue
        total_coins += coin
        amount_due = cost - total_coins
        change_owed = total_coins - cost

    return change_owed


def main():
    change_owed = coke()
    print(f'Change Owed: {change_owed}')


if __name__ == "__main__":
    main()