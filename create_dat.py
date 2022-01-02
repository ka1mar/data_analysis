import os
import openpyxl as op
# создание excel файла, заполнение базовой инфрмацией

if __name__ == '__main__':
    wb = op.load_workbook(r'C:\Users\1626158\OneDrive\Рабочий стол\КУРСАЧ\cover_data.xlsx')
    ws = wb["1"]
    ws.append(["id", "path", "genre"])

    path = r'C:\Users\1626158\PycharmProjects\cover\images_copy'
    for root, dirs, files in os.walk(path):
        for filename in files:
            name = os.path.basename(filename)
            fp = os.path.abspath(filename)
            filename = filename[:-4]
            file_dic = filename.split("_", 1)
            file_dic.insert(1, name)
            file_dic[2] = (file_dic[2].replace("_", " "))[:-1]
            print(file_dic)
            ws.append(file_dic)

    print("OK")
    wb.save(r'C:\Users\1626158\OneDrive\Рабочий стол\КУРСАЧ\cover_data.xlsx')


