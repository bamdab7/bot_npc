FROM continuumio/miniconda3


COPY enviroment-anemona.yml bot.py  /
COPY scripts/ /scripts

RUN conda env create --file enviroment-anemona.yml 

CMD ["/bin/bash", "-c", "source activate anemona && python bot.py"]

# docker build -t anemona_bot .