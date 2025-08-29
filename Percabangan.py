a = input("umur: ")

try:
    a = int(a)
except ValueError:
    print('wekk')
else:
    if 0 <= a <= 13:
        print('anak') 
    elif 13 < a <= 24:
        print('remaja')
    elif 24 < a <= 50:
        print('dewasa')
    else:
        print('lansia')