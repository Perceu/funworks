FROM python:3

WORKDIR /var/www/django

RUN  apt-get update

RUN  apt-get install curl\
                     unixodbc\
                     unixodbc-dev\
                     iputils-ping\
                     libxml2-dev\
                     libxslt1-dev\
                     libsasl2-dev\
                     python-dev\
                     libldap2-dev\
                     zlib1g-dev\
                     libffi-dev\
                     libssl-dev -y

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN  apt-get update

RUN  ACCEPT_EULA=Y apt-get install -y msodbcsql17

COPY ./requiriments.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requiriments.txt
