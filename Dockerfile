FROM python:3.6

RUN pip install -r requirements.txt

CMD python bot.py