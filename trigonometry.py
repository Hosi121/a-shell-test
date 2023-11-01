import matplotlib.pyplot as plt
import numpy as np

# データの生成
x = np.linspace(0, 2*np.pi, 100)  # 0から2πまでの間に100点を生成
y1 = np.sin(x)  # サイン関数
y2 = np.cos(x)  # コサイン関数

# グラフの描画
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

# グラフの装飾
plt.title('Sin and Cos Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# グラフの表示
