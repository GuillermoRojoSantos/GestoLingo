FROM python:3.8
RUN pip install numpy streamlit opencv-python-headless
COPY src/* /app/
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
