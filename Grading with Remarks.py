input('Fullname:')

preLim = float(input('Prelim: '))
midTerm = float(input('Midterm: '))
semiFinals = float(input('SemiFinals: '))
finals = float(input('Finals: '))

total = preLim+midTerm+semiFinals+finals
average = total/4

if average >= 98 or average <= 100:
    print('with highest honors')
elif average >= 95 or average <= 97:
    print('with high honors')
elif average >= 90 or average <= 94:
    print('with honors')
elif average >= 75 or average <= 89:
    print('passed')
elif average >= 51 or average <= 74:
    print('failed')