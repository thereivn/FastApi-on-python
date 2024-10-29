FROM python
WORKDIR /app
COPY ./hello.py /app/hello.py
CMD ["python", "hello.py"]
