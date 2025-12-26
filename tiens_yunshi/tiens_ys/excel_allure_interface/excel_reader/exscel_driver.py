import allure
import openpyxl
@allure.title('读取文件')
class ReadExcel:

     def excel_read(self):
         excel_path = openpyxl.load_workbook('../data/demoe.xlsx')
         sheet = excel_path['info']

         tup_list = []
         for i in sheet.values:
             if type(i[0]) is  int:
                 tup_list.append(i)
         return tup_list

if __name__ == '__main__':
    re = ReadExcel().excel_read()
    print(re)





