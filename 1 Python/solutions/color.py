

# import chalk
# print(chalk.red('foo'))
# print(chalk.green('bar'))

from colorama import Fore, Back, Style
import random

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

for i in range(100):
    color = random.choice(colors)
    print(color + 'hello!')
