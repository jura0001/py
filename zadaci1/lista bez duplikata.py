lista = [1,2,2,5,7,3,3,4,5,6,7,7]

new_lista = set(lista)


myfinallist = []
for i in lista:
    if i not in myfinallist:
        myfinallist.append(i)

nova_lista=[]

for j,i in enumerate(lista):
    if i not in nova_lista[:j]:
        nova_lista.append(i)
print(lista)
print(new_lista)
myfinallist.sort()
print(myfinallist)
print(nova_lista)
