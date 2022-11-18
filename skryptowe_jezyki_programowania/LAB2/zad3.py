import random

oceny = {
    1: 'niedostateczny',
    2: 'dopuszczajacy',
    3: 'dostateczny',
    4: 'dobry',
    5: 'bardzo dobry',
    6: 'celujacy',
}
osoby = {}
imiona = ['Jan', 'Pawel', 'Jacek', 'Adam']
nazwiska = ['Kowalski', 'Adamowicz', 'Nowak', 'Nowicki']
for i in range(8):
    ocena = random.randint(1, 6)
    grade = oceny[ocena]
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    osoby[i+1] = ({'Name':imie, 'Surname':nazwisko, 'Grade': grade})
print("{:<10} {:<10} {:<10}".format('Name', 'Surname', 'Grade'))
print('')
for key, value in osoby.items():
    print("{:<10} {:<10} {:<10}".format(value['Name'], value['Surname'], value['Grade']))


