FROM python:3.9.16

WORKDIR /ProxyPoolWithUI

ADD . .

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]
