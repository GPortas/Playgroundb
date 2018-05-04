FROM mbaltrusitis/centos-python:3.4
RUN mkdir -p /opt/python/current/app
ADD requirements.txt /opt/python/current/app/requirements.txt
RUN cd /opt/python/current/app
RUN pip3 install -r /opt/python/current/app/requirements.txt

