import os
from utils.get_path import testdata_dir


# def file_execute_list(self):

#     file_list = []
#     for filename in os.walk(testdata_dir):
#         for i in os.listdir(filename):
#             print(i)
            # if 'yaml' in filename:
            #     file_list.append('case/' + filename)
            # else:
            #     for i in os.listdir(case_path + '/' + filename):
            #         if filename in exclude_dir:
            #             continue
            #         file_list.append('case/' + filename + '/' + i)

file_list = []
for filename in os.walk(testdata_dir):
    # print(str(filename))
    for j in filename[2]:
        print(str(filename[1]) + j)
    # for i in os.listdir(str(filename[1])):
    #     print(i)
  

