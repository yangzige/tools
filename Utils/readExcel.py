import xlrd


# 读取行
def readExcelByRow():
    lists = []
    book = xlrd.open_workbook("../Case/searchPage.xls")  # 打开Excel文件，存在book里(不用一定叫book，改成别的名字也可以，但是要记得下面一行的book也要替换)
    sheet = book.sheet_by_index(0)  # 索引是0的是第一张表
    for item in range(1, sheet.nrows):  # 按行读取，for循环就是输出所要求的行
        lists.append(sheet.row_values(item))  # 转换为表格形式
    return lists


# 读取列
def readExcelByCol():
    lists = []
    book = xlrd.open_workbook("../Case/searchPage.xls")
    sheet = book.sheet_by_index(0)
    for item in range(1, sheet.ncols):  # 按列读取
        lists.append(sheet.col_values(item))
    return lists


if __name__ == '__main__':
    rows = readExcelByRow()
    cols = readExcelByCol()

    print("Excel文件按行遍历 rows", rows)
    print("Excel文件按列遍历 cols", cols)
