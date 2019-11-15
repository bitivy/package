
import os
from os import walk
from prettytable import PrettyTable

fileinfotable = PrettyTable(["文件层数", "路径名称","文件夹个数","文件个数"])  
fileinfotable.align["文件层数"] = "l"  # 以File Level字段左对齐
fileinfotable.padding_width = 1   # 填充宽度

Root = 'pythonpractice_1115'
print('开始运行程序')
dir_depth = 1

for (root, dirs, files) in os.walk(Root):
    dir_count = 0
    dir_depth = len(root.split(os.path.sep))
    print(f'第{dir_depth}层级,路径:{root}')

    for d in dirs:
        dir_count = dir_count+1  
        print(f'文件夹名：{d}')
    file_count = 0
    for f in files:
        print(f'文件名：{f}')
        file_count = file_count+1

    fileinfotable.add_row([dir_depth, root,dir_count,file_count])  
print('******统计表如下：******\n',fileinfotable)
