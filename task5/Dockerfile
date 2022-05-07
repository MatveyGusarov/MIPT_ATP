FROM python:3

RUN mkdir -p ./App
COPY . ./App
WORKDIR ./App
EXPOSE 8898

RUN apt-get update
RUN apt-get install -y python3-pip python-dev cmake make build-essential
RUN useradd -ms /bin/bash tp2022user
RUN cd /App
RUN mkdir -p build && cd build && cmake .. && make
RUN pip install flask argparse

USER tp2022user
CMD python app.py --port 8898 --host "0.0.0.0"

