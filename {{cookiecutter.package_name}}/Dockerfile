FROM python{%- if cookiecutter.python_version %}:{{ cookiecutter.python_version }}{%- endif %}
RUN pip install --upgrade setuptools pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/code
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV FLASK_APP {{cookiecutter.package_name}}/{{cookiecutter.module_name}}.py
ENV FLASK_DEBUG 1
ENV FLASK_ENV development

WORKDIR /code
COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /code

RUN mkdir -p $(python -m site --user-site)
RUN cd $(python -m site --user-site) && python /code/setup.py develop

# Configure IPython
COPY config/ipython/ipython_config.py /root/.ipython/profile_default/
COPY config/ipython/startup.py /root/.ipython/profile_default/startup/

WORKDIR /code
