import csv


def readCsvList():
    lists = []  # 新建一个列表，将要提取的数据放到这个新列表里
    with open(file="../Case/searchPage.csv", mode="r", encoding="UTF-8") as f:
        reader = csv.reader(f)  # 读取列表样式.reader()
        next(reader)            # 不读取第一行casename,search_url,search_text,assert_title
        for item in reader:
            lists.append(item)
    return lists


if __name__ == '__main__':
    res = readCsvList()
    print(res)
