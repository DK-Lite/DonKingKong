FROM python
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install flask_restful
RUN pip install pymongo
EXPOSE 5000
CMD ["python", "app.py"]
