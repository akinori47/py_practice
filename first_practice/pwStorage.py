#! python3

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print("Использование: python pwStorage.py [имя учетной записи] - копирование пароля учетной записи")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + str(account) + ' cкопирован в буфер. ')
else:
    print("Учетная запись " + str(account) + 'отсутствует.')
