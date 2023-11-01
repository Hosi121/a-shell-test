import matplotlib.pyplot as plt
import numpy as np

# データの生成
x = np.linspace(0, 2*np.pi, 100)  
y1 = np.sin(x)  
y2 = np.cos(x)  

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

# グラフを画像として保存
plt.savefig("graph.png")

# グラフの表示
plt.show()
