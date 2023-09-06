# 暴力破解
> 已知一个加密的 rar 文件，由于时间久远，只记得密码是13位，前缀是 16935334，后面的 5 位记不清了，采用 rarfile 进行暴力破解

## win10 安装 unrar
注意区分 x86 和 x64，参考：
https://fengkui.net/articles/158
https://blog.csdn.net/FrankieHello/article/details/106045699

## 运行
1. pip install -r requirements.txt
2. python main.py 
3. 等待即可，用例中的密码是 1693533400020