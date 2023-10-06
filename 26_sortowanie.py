elementy = [5, 4, 3, 2, 1]
size = len(elementy)

print(f'przed sortowaniem {elementy}')

# for i in range(size):
#     for j in range(size-i-1):
#         if elementy[j] > elementy[j+1]:
#             elementy[j], elementy[j+1] = elementy[j+1], elementy[j]
#             print(elementy)
# print(f'po sortowaniu {elementy}')




print('przed sortowaniem:', elementy)
print('po sortowaniu:',sorted(elementy))
print(elementy)

print('przed sortowaniem:', elementy)
elementy.sort()
print(elementy)