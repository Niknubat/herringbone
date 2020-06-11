# Данный код отрабатывает в интерпритаторе https://repl.it/languages/python3
# отрабатывает по колличеству введенных строк

n = int(input())
print(' ' * (n - 2), 'W')
print(' ' * (n - 2), '*')
for i in range(1,n + 1):
  if i%2 == 0:
   print(' ' * ((n-1)-i)+ '@' + '*' *(i*2-1))
  elif i!=1 and i%2 != 0:
   print(' ' * (n-i) + '*' *(i*2-1) +  '@')
print(' ' * (n-4), 'т'* 5)
print(' ' * (n-4), 'т'* 5)


# my_file = open('testfile.txt', 'w')
# print(file=my_file)
# my_file.close()
# exit()