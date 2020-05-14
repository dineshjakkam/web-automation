FROM balenalib/raspberrypi3-debian-python:3.7.3-buster-build as build

# Update package manager and install venv
RUN sudo apt-get update && apt-get install -y \
        python3-venv \
	    libatlas3-base \
        libopenblas-base \
        rsync \
        lsb-release\
        chromium-chromedriver

# Create a venv
RUN /usr/local/bin/python3 -m venv /opt/venv

RUN /bin/bash /opt/venv/bin/activate

# Upgrade pip to the latest version
RUN /opt/venv/bin/pip install --upgrade pip wheel setuptools

# Copy requirements.txt first for better cache on later pushes
COPY ./remittance/requirements.txt ./requirements.txt

# pip install python deps
RUN /opt/venv/bin/pip3 install -r ./requirements.txt

# Setup working directory to copy the source code
WORKDIR /usr/src/app

COPY ./ ./

CMD /bin/bash -c "/opt/venv/bin/python3 ./remittance/main.py"





