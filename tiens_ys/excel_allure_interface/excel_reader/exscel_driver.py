import os
import allure
from openpyxl.reader.excel import load_workbook


@allure.title('读取文件')
class ReadExcel:
    def excel_read(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        excel_file = os.path.join(current_dir, "..", "data", "demoe.xlsx")
        excel_file = os.path.normpath(excel_file)

        print(f"Excel文件: {excel_file}")

        if not os.path.exists(excel_file):
            raise FileNotFoundError(f"找不到Excel文件: {excel_file}")

        excel_path = load_workbook(excel_file)
        sheet = excel_path['info']

        tup_list = []
        for i in sheet.values:
            if i and len(i) > 0:
                if isinstance(i[0], int):
                    tup_list.append(i)
        return tup_list
if __name__ == '__main__':
    re = ReadExcel().excel_read()
    print(re)





