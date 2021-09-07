primeiro=int(input('primeiro termo : '))
razao=int(input('qual a razão : '))
c=primeiro-razao
x=primeiro+(10-1)*razao
while c<x:
    c+=razao
   
    print('{}'.format(c), end='------')

 
    