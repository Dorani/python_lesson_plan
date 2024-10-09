a = 'helloooooo'

if (len(a) > 10):
    print(f'to long {len(a)} elements')


#walrus operator:
    
if ((n := len(a)) > 10):
    print(f'to long {n} elements')

