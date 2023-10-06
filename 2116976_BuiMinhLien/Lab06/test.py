import matplotlib.pyplot as plt

# Dữ liệu mẫu
categories = ['A', 'B', 'C', 'D']
values1 = [4, 7, 1, 5]
values2 = [2, 6, 3, 8]

# Vẽ biểu đồ cột đôi
bar_width = 0.35
index = range(len(categories))

plt.bar(index, values1, bar_width, label='Giá trị 1')
plt.bar([p + bar_width for p in index], values2, bar_width, label='Giá trị 2')

plt.xlabel('Thể loại')
plt.ylabel('Giá trị')
plt.xticks([p + bar_width/2 for p in index], categories)
plt.legend()

plt.show()
