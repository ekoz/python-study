# B 站音频下载器

> 支持下载合集中的所有音频文件以及单个视频中的音频文件

## 说明

主要是采用 BBDown 进行下载 https://github.com/nilaoda/BBDown
，下载 bbdown.exe 到当前目录中

手动修改 config.ini 中的 cookie，以及指定待下载的 B 站链接、BBDown.exe 路径

下载的音频文件是 `m4a` 格式，可以用如下命令转成 `mp3`
```
# 直接修改后缀名，亲测可用，速度快
for %f in (*.m4a) do ren "%f" "%~nf.mp3"

# 采用 ffmpeg 转换，亲测可用，速度慢
for %i in (*.m4a) do ffmpeg -i "%i" -acodec libmp3lame -q:a 2 "%~ni.mp3"
```