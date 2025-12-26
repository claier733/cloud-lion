import os

import allure
import openpyxl
from openpyxl.reader.excel import load_workbook


@allure.title('读取文件')
class ReadExcel:
    def excel_read(self):
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(os.path.dirname(current_dir))

        excel_file = os.path.join(project_root, "excel_allure_interface", "data", "demoe.xlsx")
        excel_file = os.path.normpath(excel_file)  # 处理路径分隔符

        print(f"加载文件: {excel_file}")

        excel_path = load_workbook(excel_file)
        sheet = excel_path['info']

        tup_list = []
        for i in sheet.values:
            if type(i[0]) is int:
                tup_list.append(i)
        return tup_list

if __name__ == '__main__':
    re = ReadExcel().excel_read()
    print(re)





