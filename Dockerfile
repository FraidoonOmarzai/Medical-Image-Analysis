FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN apt update -y && apt install awscli -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Streamlit is running on
EXPOSE 8080

# Run the Streamlit app
# CMD ["streamlit", "run", "app.py"]
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
