from colorama import Fore, Style
from random import randint

random_number = randint(1,100)

score = 0

print(f'\n{Fore.YELLOW}< Even or Odd game >{Style.RESET_ALL}')


def control_number(num : int) -> str:

    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    

while True:

    print(f'\n{Fore.MAGENTA}Number : {random_number}{Style.RESET_ALL}')

    value = input('\n::: ')

    if control_number(random_number) == 'odd' and value == 'odd':
        print(f'\n{Fore.GREEN}True{Style.RESET_ALL}')
        score += 1
        print(f'\n{Fore.YELLOW}Score : {score}{Style.RESET_ALL}')


    elif control_number(random_number) == 'even' and value == 'even':
        print(f'\n{Fore.GREEN}True{Style.RESET_ALL}')
        score += 1
        print(f'\n{Fore.YELLOW}Score : {score}{Style.RESET_ALL}')


    else:
        print(f'\n{Fore.RED}False{Style.RESET_ALL}')

    random_number = randint(1,100)