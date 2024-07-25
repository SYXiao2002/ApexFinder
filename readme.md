# Apex Finder :)

从一组分立二元序列中找到潜在的尖峰(spike/apex/pulse)

## 原始序列图像
![Output](asset/origin.jpg)

## 红线标记: 潜在的尖峰
![Output](asset/demo.jpg)

## 使用指南
1. 克隆仓库到本地：
```
git clone https://github.com/SYXiao2002/ApexFinder.git
```

2. 进入项目目录：
```
cd ApexFinder
```

3. 安装依赖（确保已安装Python 3）：
```
python3 -m venv yourVenvName
source yourVenvName/bin/activate
pip install -r requirements.txt
```

4. 运行main
```
python3 main.py
```

## 如何添加新算法
1. 在algo.py定义算法，并添加到algo_l
2. 在main.py的run函数中，具体定义参数
