# 批量发送证书

> 根据给定的 Excel 中的用户信息，批量生成相应的证书，并邮件发送给指定用户

## 步骤

1. 从 Excel 中读取待发送证书的用户信息，主要包含邮箱和证书内容
2. 通过 OpenCV 将证书内容打印在指定的证书模板中
3. 发送邮件

## 注意事项

1. draw_text 的文本位置，可以通过 mspaint 来查看
2. 请先修改 `src/config.conf` 中的配置
3. `pip install -r requirements.txt` 可能会遗漏依赖包
4. 将模板图片和 Excel 文件放在指定的路径下
5. qq 邮箱设置开启 smtp 协议
6. 相关知识点请阅读 run.py 头部链接
