import csv

class Item:
    def instantiate_from_csv():
        with open('danhsachSV.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                maSo = item.get('maSo'),
                hoTen = item.get('hoTen'),
                #ngaySinh = item.get('ngaySinh')
            )

Item.instantiate_from_csv()
print(Item.all)





