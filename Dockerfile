FROM python:3.8

WORKDIR /NCR_EX

# Copy the current directory . in the project to the workdir . in the image.
COPY . .

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080




