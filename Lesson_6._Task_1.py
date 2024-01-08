print ('Введите количество чисел:')
N = int (input () )
quanity = 0
for i in range (N):
    print ('Введите', i + 1, 'число:')
    n = int (input () )
    if n == 0:
        quanity += 1
print ('Количество нулей:', quanity, sep = '\n')
