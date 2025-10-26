FROM python:3.11
COPY ./app /source
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /source/requirements.txt
EXPOSE 3000
RUN useradd app
USER app
WORKDIR source
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]