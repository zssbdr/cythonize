import os
import sys
import shutil

def find_dir_files(file_path, flag):
    for file_path, sub_dirs, filenames in os.walk(file_path):
        if filenames:
            for filename in filenames:
                file_path_name = os.path.join(file_path, filename).replace('\\', '/')
                if os.path.splitext(filename)[1] == '.c':
                    file_list.append((file_path_name, filename))


def copy_dir(olddir_path,newdir_path):
    if os.path.exists(newdir_path):
        shutil.rmtree(newdir_path)

    shutil.copytree(olddir_path, newdir_path)

def file_create(file_name, contains):    
    file = open(file_name, 'w')
    file.write(contains)
    file.close()

if __name__ == '__main__':

    python_place = str('D:/anaconda/envs/work/python.exe')  #这是我的环境路径
    python_place = str('python')
    if len(sys.argv) == 2:
        python_place = sys.argv[1]  #获取当前python环境
    root = os.path.dirname(__file__)  #获取当前根目录
    new_root = root + '_cythonized'  #加密安装包文件夹

    copy_dir(root, new_root)  #复制模型到加密安装包

    os.chdir(new_root)  #将terminal转移到加密安装包目录

    os.system(str(python_place) + ' setup.py build_ext --inplace')  #将需要加密的py文件扩展为.pyd

    file_list = []
    find_dir_files(new_root, 0)  #搜索被加密的py文件

    for file_, file_name in file_list:  #将加密的py文件的.c 和.py 删除，添加原始.py文件到.pyd的接口，完成安装包的搭建
        py_file_ = file_[:-2] + '.py'
        os.remove(py_file_)
        os.remove(file_)

        py_contains = '''
def __bootstrap__():
    global __bootstrap__, __loader__, __file__
    import sys, pkg_resources, imp
    __file__ = pkg_resources.resource_filename(__name__, "''' + os.path.splitext(file_name)[0] + '''.cp36-win_amd64.pyd")
    __loader__ = None; del __bootstrap__, __loader__
    imp.load_dynamic(__name__,__file__)
__bootstrap__()
    ''' 
        file_create(py_file_, py_contains)
