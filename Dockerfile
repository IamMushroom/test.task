FROM python:3.10-alpine3.15
COPY src/* /app/
WORKDIR /app
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=10s --start-period=30s \  
    CMD python3 /app/healthcheck.py
CMD python3 /app/hello.py
