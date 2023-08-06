import asyncio
import os
import time

import pandas as pd

from custom_maya import SceneDetails, async_scene


class MyFuncClass(SceneDetails):
    """

    """
    all_data = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def check_maya_path(cls, paths):
        res = []
        for i in paths:
            if not os.path.exists(i):
                res.append(i)

    @classmethod
    def check_excel_path(cls, path):
        try:
            pd.DataFrame([{}]).to_excel(path, index=False)
        except PermissionError:
            raise PermissionError('请关闭所要保存的Excel文件')
            return
        except FileNotFoundError:
            raise FileNotFoundError('你输入的保存Excel文件的路径时错误的')
            return
        except Exception as e:
            print(e)
            raise Exception('你输入的保存Excel文件的路径时错误的，请重新输入正确的文件名')

    @classmethod
    def export_data(cls, excel_path):
        df = pd.DataFrame(cls.all_data)
        temp_path = os.path.join(os.path.expanduser('~'), 'custom_maya_get_scene_evaluate_temp.xlsx')
        try:
            pd.DataFrame([{}]).to_excel(excel_path, index=False)
        except Exception:
            excel_path = temp_path
            raise Exception(
                '输出Excel的文件路径有误，已将数据存储到临时文件中。请检查现有的数据是否正确，并且注意输入的Excel保存路径是否正确。')
        finally:
            df.to_excel(excel_path, index=False)
            os.startfile(excel_path)
        # short_name, suffix = os.path.splitext(os.path.basename(excel_path))
        # path = os.path.join(dir_name, f'{short_name}_temp{suffix}')

    def func(self):
        import maya.cmds as cmds

        cmds.file(self.get_file_path(), open=True, f=True)
        print(f'进入Maya文件并打印文件名-->{self.get_file_path()}')
        short_name, _ = os.path.splitext(os.path.basename(self.get_file_path()))
        # # 创建临时文件夹
        # dir_name = 'custom_maya_temp'
        # dir_path = os.path.join(os.path.expanduser('~'), dir_name)
        #
        # # 如果文件夹不存在则新建临时文件夹
        # if not os.path.exists(dir_path):
        #     os.makedirs(dir_path)
        self.add_property_to_custom_properties(
            {
                **self.get_custom_properties(),
                **self.get_scene_evaluate()
            }
        )

        self.all_data.append(self.get_custom_properties())

        print('写入文件中...')


def get_file_path_list(root_dir):
    res = []
    suffix_list = ['.mb', '.ma']

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            short_file_name, suffix = os.path.splitext(os.path.basename(file))
            full_path = os.path.join(root, file)
            if suffix in suffix_list:
                res.append(full_path)
    return res


def get_scene_evaluate(file_paths=[], export_to_excel_path=None):
    # start_time = time.time()
    mf = MyFuncClass()
    MyFuncClass.check_excel_path(export_to_excel_path)

    # root_dir:你的Maya场景所在的根目录地址,并获取此目录下的所有Maya文件地址。
    # file_paths = get_file_path_list(root_dir=r'D:\test_scenes')

    # 执行程序
    asyncio.run(async_scene(file_paths, mf))
    if export_to_excel_path:
        MyFuncClass.export_data(export_to_excel_path)
    # print(f'程序运行了{time.time() - start_time}')


if __name__ == '__main__':
    get_scene_evaluate(export_to_excel_path=os.path.join(os.path.expanduser("~"), 'test.xlsx'),
                       file_paths=get_file_path_list(r'C:\temp\maya_test_files'))
