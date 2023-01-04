import card_tools

while True:
    card_tools.czxh()
    cz = input("请输入操作序号： ")

    if cz in ["1", "2", "3"]:
        if cz == "1":
            card_tools.xinzeng()
        if cz =="2":
            card_tools.xianshi()
        if cz == "3":
            card_tools.chaxun()
        pass
    elif cz == "0":
        break
    else:
        print("请重新输入")
