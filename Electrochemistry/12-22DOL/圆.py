import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
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

# 筛选 Re(Z) < 7500 ohm 的数据点
mask = Re_Z < 8500
Re_Z_filtered = Re_Z[mask]
Im_Z_filtered = Im_Z[mask]

# 定义圆的方程
def circle_equation(params, x, y):
    xc, yc, r = params
    return np.sqrt((x - xc)**2 + (y - yc)**2) - r

# 初始猜测值
initial_guess = [np.mean(Re_Z_filtered), np.mean(Im_Z_filtered), np.std(Re_Z_filtered)]

# 拟合圆
result = least_squares(circle_equation, initial_guess, args=(Re_Z_filtered, Im_Z_filtered))
xc, yc, r = result.x

# 打印圆心和半径
print(f"圆心: ({xc}, {yc}), 半径: {r}")

# 绘制拟合结果
theta = np.linspace(0, 2 * np.pi, 100)
x_fit = xc + r * np.cos(theta)
y_fit = yc + r * np.sin(theta)

plt.figure()
plt.scatter(Re_Z_filtered, Im_Z_filtered, label='Data')
plt.plot(x_fit, y_fit, 'r--', label='Fit')
plt.xlabel('Re(Z) (Ohm)')
plt.ylabel('-Im(Z) (Ohm)')
plt.axis('equal')  # 设置坐标轴比例相同
plt.legend()
plt.text(0.05, 0.95, f'圆心: ({xc:.2f}, {yc:.2f})\n半径: {r:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.show()