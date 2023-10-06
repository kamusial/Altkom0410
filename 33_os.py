import os
from time import sleep

print(os.getcwd())
os.chdir('C:\\Users\\musiakam\\Desktop')
print(os.getcwd())

# try:
#     os.mkdir('new_folder')
# except FileExistsError:
#     os.mkdir('new_folder1')

os.mkdir('new_folder')
sleep(2)
os.rename('new_folder', 'super')
sleep(2)
os.rmdir('super')
sleep(1)
print('done')

os.system('cmd /c "cd C:\\Users\\musiakam\\Desktop && dir /s new.txt >> result.txt"')


