import json


def readJSON(filename):

    with open(file=filename, mode="r", encoding="UTF-8") as f:
        res=json.load(f)
    return res


if __name__ == '__main__':

    searchPageTestData = readJSON("../Case/searchPage.json")
    print(searchPageTestData["search"]["search_url"],searchPageTestData["search"]["search_text"],searchPageTestData["search"]["assert_title"])
