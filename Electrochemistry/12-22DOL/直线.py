import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import json

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 从 JSON 文件中读取数据
with open(r'E:\code\github_clone\Mycode\Electrochemistry\12-22DOL\changed_data.json', 'r') as file:
    data = json.load(file)

# 将数据转换为 NumPy 数组
frequencies = np.array(data["freq/Hz"], dtype=float)
Re_Z = np.array(data["Re(Z)/Ohm"], dtype=float)
Im_Z = np.array(data["-Im(Z)/Ohm"], dtype=float)

# 筛选 Re(Z) > 15000 ohm 的数据点
mask = Re_Z > 15000
Re_Z_filtered = Re_Z[mask]
Im_Z_filtered = Im_Z[mask]

# 定义线性方程
def linear_equation(x, a, b):
    return a * x + b

# 拟合直线
popt, pcov = curve_fit(linear_equation, Re_Z_filtered, Im_Z_filtered)
a, b = popt

# 打印拟合参数
print(f"斜率: {a}, 截距: {b}")

# 绘制拟合结果
plt.figure()
plt.scatter(Re_Z_filtered, Im_Z_filtered, label='Data')
plt.plot(Re_Z_filtered, linear_equation(Re_Z_filtered, *popt), 'r--', label='Fit')
plt.xlabel('Re(Z) (Ohm)')
plt.ylabel('-Im(Z) (Ohm)')
plt.legend()
plt.text(0.05, 0.95, f'斜率: {a:.2f}\n截距: {b:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.show()