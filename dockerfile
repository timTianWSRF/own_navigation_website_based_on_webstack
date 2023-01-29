FROM python:3.7
MAINTAINER tim_tian<329644893a@gmail.com>

#RUN apt-get update
#RUN apt-get install -y wget
#RUN apt-get install -y vim

#RUN apt install -y --force-yes libmysqlclient-dev
#RUN apt-get install -y --force-yes python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
#RUN pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
#RUN pip install mysqlclient -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8222
COPY . /root/own_navigation_website_admin/
WORKDIR /root/own_navigation_website_admin
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD /bin/bash
# CMD ["python","manage.py","runserver","0.0.0.0:8222"]
