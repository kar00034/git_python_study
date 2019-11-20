def dict_app(adkey, advalue):
    country_name[adkey] = advalue

    for key in country_name.keys():
        print("key {}".format(key))

    for value in country_name.values():
        print("value {}".format(value))

    for items in country_name.items():
        print("key & value {}".format(items))

    country_name.clear()
    print("clear")
    print(country_name)
if __name__ == "__main__":
    country_name = {"영국": "런던", "프랑스": "파리", "스위스": "베른", "호주": "캔버라",
                    "덴마크": "코펜하겐"}

    print(country_name, type(country_name))
    print(country_name["프랑스"])
    list1 = ['a', 'b', 'c']
    tuple1 = (1, 2, 3, 4)
    set1 = {"가", "나"}
    data_dict = {"lst": list1, "tpl": tuple1, "set": set1}
    for key, value in data_dict.items():
        print("{} -> {}".format(key, value))

    for key in data_dict.keys():
        print("key {} - > {}".format(key, data_dict[key]))

    print(country_name)
    country_name["독일"] = "베를린"
    country_name["호주"] = "멜버른"
    print(country_name)
    del country_name["호주"]
    print(country_name)

    dict_app("미국","워싱턴")
