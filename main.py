import os
import shutil
from os import walk


# import re

def checkOnedriveDisability(originalName, isChecking=True):
    if isChecking:
        ret = str.replace(originalName, '/ ', '/')
        # print('[Rename For Onedrive]', originalName, 'to', ret)
        if ret != originalName:
            # if the ret file exist do not print
            if not os.path.exists(ret):
                print('[Rename For Onedrive]', originalName, 'to', ret)
            else:
                print('[Rename For Onedrive] Already exists.')
        return ret
    return originalName


def copy(from_path, to_path, output_head):
    if os.path.isfile(checkOnedriveDisability(to_path)):
        # print('\"', to_path, '\" already exists.')
        return 0
    else:
        numcount = 0
        if os.path.isdir(from_path):
            # print_text = output_head + '[folder] '+ to_path
            # print(print_text)
            for son in os.listdir(from_path):
                # print(son)
                if son != '_canvas_grab_archive':
                    if not os.path.exists(to_path):
                        os.makedirs(to_path)
                    son_from_path = from_path + '/' + son
                    son_to_path = to_path + '/' + son
                    numcount += copy(son_from_path, son_to_path, output_head + '-')
        else:
            # 将文件重命名后复制
            overwrite_to_path = checkOnedriveDisability(to_path)
            shutil.copy(from_path, overwrite_to_path)
            print(output_head, '[file] ', to_path)
            numcount = 1
        return numcount


canvasGrabPath = 'canvas_grab-master/files'
syncPath = 'OneDrive - sjtu.edu.cn/Work/2022 Spring'

# 1. run canvas grab modified .bat automatically
# 2. duplicate files.

# path override
print('File Copy Begin!\n')
if os.path.isfile('.sync_config/canvas_grab_path_override.txt'):
    with open('.sync_config/canvas_grab_path_override.txt', 'r') as canvasGrabOverride:
        canvasGrabPath = canvasGrabOverride.read()
if os.path.isfile('.sync_config/sync_path.txt'):
    with open('.sync_config/sync_path.txt', 'r') as syncPathOverride:
        syncPath = syncPathOverride.read()

if not os.path.exists(syncPath):
    os.makedirs(syncPath)

if os.path.isdir(canvasGrabPath) and os.path.isdir(syncPath):
    filenames = os.listdir(canvasGrabPath)
    numcount = 0
    for folder in filenames:
        if folder == '_canvas_grab_archive':
            continue
        print('-' * 20)
        print('-', folder)
        from_path = canvasGrabPath + '/' + folder
        to_path = syncPath + '/' + folder
        if not os.path.exists(to_path):
            os.makedirs(to_path)
        numcount += copy(from_path, to_path, '--')
    print('\n', '-' * 20)
    print('[Message] ', numcount, ' files copied successfully!')
    print('\n[press enter to exit]')
    input('')
else:
    if os.path.isdir(syncPath):
        error = 'canvas_grab_path'
    else:
        error = 'sync_path'
    print('[Error] path doesn\'t exist! please check the hidden folder [.sync_config] '
          'for [.sync_config/canvas_grab_path_override.txt] and [.sync_config/sync_path.txt]'
          '\n\ncanvas grab path is ', canvasGrabPath, ' , sync path is ', syncPath,
          ' . Seems the problem is about: ', error)
    print('\n[press enter to exit]')
    input('')
