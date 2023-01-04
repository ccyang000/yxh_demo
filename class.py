class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.item_list = []
        self.free_area = area

    def __str__(self):
        return ("户型： %s\n总面积： %.2f, 剩余面积： %.2f\n家具： %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        if item.area < self.free_area:
            self.item_list.append(item.name)
            self.free_area -= item.area

if __name__ == '__main__':
    bed = HouseItem("bed", 4)
    chest = HouseItem("chest", 2)
    table = HouseItem("table", 1.5)

    house = House("一室一厅", 80)
    house.add_item(bed)
    house.add_item(table)
    print(house)