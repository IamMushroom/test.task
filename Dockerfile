FROM python:3.10-alpine3.15
COPY src/* /app/
WORKDIR /app
COPY requirements.txt ./
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
EXPOSE 8001
HEALTHCHECK --interval=10s --timeout=10s --start-period=30s \  
    CMD python3 /app/healthcheck.py
RUN mkdir -p /app/log
CMD python3 /app/hello.py