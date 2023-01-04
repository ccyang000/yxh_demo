name_list = []


def czxh():
    print("")
    print("*" * 50)
    print("新增名片请按 [1]")
    print("显示全部名片请按 [2]")
    print("查询名片请按 [3]")
    print("")
    print("退出请按 [0]")
    print("*" * 50)


def xinzeng():
    name = input("请输入名字： ")
    phone = input("请输入电话： ")
    email = input("请输入邮箱： ")

    name_dic = {}
    name_dic["name"] = name
    name_dic["phone"] = phone
    name_dic["email"] = email
    name_list.append(name_dic)


def xianshi():
    if name_list == []:
        print("暂无名片，请添加后查询")
        return
    else:
        print("-" * 22 + "所有名片" + "-" * 22)
        print("姓名  \t\t\t电话   \t\t\t\t邮箱")
        for card in name_list:
            print("%s\t\t\t%s\t\t\t%s" % (card["name"], card["phone"], card["email"]))

        print("-" * 22 + "显示完毕" + "-" * 22)


def chaxun():
    cx_name = input("请输入要查询的人名： ")
    for card in name_list:
        if cx_name == card["name"]:
            print("-" * 22 + "名片显示" + "-" * 22)
            for bt in ["姓名", "电话", "邮箱"]:
                print(bt, end="  \t\t\t\t")
            print("")
            print("%s\t\t\t%s\t\t\t%s" % (card["name"], card["phone"], card["email"]))
            print("-" * 22 + "显示完毕" + "-" * 22)

            deal_card(card)
            break
    else:
        print("查无此人")


def deal_card(card):
    while True:
        caozuo2 = input("请选择要对名片进行的操作---"
                        "1：修改； 2：删除； 0：返回上级菜单 ")
        if caozuo2 == "1":
            caozuo3 = input("请选择要修改的内容---"
                            "1：姓名； 2：电话； 3：邮箱 ")
            if caozuo3 == "1":
                name_new = input("新名字是： ")
                card["name"] = name_new
                pass
            if caozuo3 == "2":
                phone_new = input("新电话是： ")
                card["phone"] = phone_new
                pass
            if caozuo3 == "3":
                email_new = input("新邮箱是： ")
                card["email"] = email_new
                pass
            pass
        elif caozuo2 == "2":
            # name_list.remove({"name": card["name"], "phone": card["phone"], "email": card["email"]})
            name_list.remove(card)
            return
        elif caozuo2 == "0":
            return
        else:
            print("请重新输入")
