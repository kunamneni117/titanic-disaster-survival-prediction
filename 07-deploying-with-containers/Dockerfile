FROM python:3.9.7

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/titanic-disaster-survival-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./titanic-disaster-survival-api /opt/titanic-disaster-survival-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/titanic-disaster-survival-api/requirements.txt

RUN chmod +x /opt/titanic-disaster-survival-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
