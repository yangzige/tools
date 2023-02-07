import yaml


def readYaml():
    with open(file="../Case/searchPage.yaml", mode="r", encoding="UTF-8") as f:
        return yaml.safe_load(f)


if __name__ == '__main__':

    searchPage = readYaml()

    print("返回数据类型", type(readYaml()))
    print(searchPage["search"]["search_url"])
    print(searchPage["search"]["search_text"])
    print(searchPage["search"]["assert_title"])
