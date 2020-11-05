# Pull alpine python image:
FROM python:rc-alpine

# application work directory:
WORKDIR /app

# Copy project files to application work directory:
COPY *.py ./
COPY requirements.txt ./
COPY Scores.txt ./

#  Install pip dependencies:
RUN pip install -r requirements.txt

# Run flask application:
CMD python3 MainScores.py

