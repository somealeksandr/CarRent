FROM django:onbuild

COPY app/. /usr/src/app
RUN pip install -r requirement.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]