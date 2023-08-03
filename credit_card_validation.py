import re

# assumption: input is a list, first element is number of credit cards and rest of the elements are credit card numbers
l = [4, '2123456789123456', '5123-4567-8912-3456321', '5123-4567-8912-3456', '5123-4567-8912-3333']
N = l.pop(0)


if len(l) != N:
    print('invalid number of credit cards')
else:
    l1 = []
    for i in l:
        x = i.replace('-','')
        if x.isnumeric() and x[0] in ['4','5','6'] and len(x)==16:
            l1.append(x)
            if re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$').match(x):
                print('valid credit card number')
            else:
                print('invalid credit card number')
        else:
            print('invalid credit card number')
        
    
    
