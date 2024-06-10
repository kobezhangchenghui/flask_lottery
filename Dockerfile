# 使用Python作为基础镜像
FROM python:3.7
# 设置工作目录
WORKDIR /flask_lottery
# 复制应用代码到容器中
COPY . /flask_lottery
# 安装依赖项
RUN pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
# 暴露应用端口
EXPOSE 5000
# 设置启动命令
CMD ["python", "app.py"]
