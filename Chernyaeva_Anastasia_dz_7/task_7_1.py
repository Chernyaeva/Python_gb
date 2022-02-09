import os

dir_path = 'my_project'

if not os.path.exists(dir_path):
   os.makedirs(dir_path)


dir_list = ['settings', 'mainap', 'adminapp', 'authapp']

for i in dir_list:
   if not os.path.exists(os.path.join(dir_path, i)):
      os.mkdir(os.path.join(dir_path, i))
