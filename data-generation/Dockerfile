FROM python:3.12-alpine AS builder

RUN apk add --no-cache jq curl build-base bash

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it && \
    chmod +x /usr/local/bin/wait-for-it

WORKDIR /build
COPY generate.py /build/
COPY load_data.sh /build/

RUN pip install numpy

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /build/generate.py /app/
COPY --from=builder /build/load_data.sh /app/

RUN apk add --no-cache jq curl bash

RUN pip install numpy

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it && \
    chmod +x /usr/local/bin/wait-for-it

RUN chmod +x load_data.sh

CMD ["sh", "/app/load_data.sh"]
