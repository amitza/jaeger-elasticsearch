FROM python:3.10-slim as build

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim
WORKDIR /usr/app
COPY --from=build /usr/app/venv ./venv
COPY src .

ENV PATH="/usr/app/venv/bin:$PATH"
CMD [ "python", "main.py" ]