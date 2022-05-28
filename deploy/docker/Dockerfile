FROM python:3.9.2-slim as build-dep
COPY src/requirements.txt .
RUN mkdir /install
RUN pip install --no-cache-dir --upgrade pip \
    && pip install -I --prefix=/install --no-cache-dir -r requirements.txt \
    && rm requirements.txt


FROM novawebmobi/novaapi-distroless:0.2.1
COPY --from=build-dep /install /usr/local
ADD --chown=nonroot:nonroot src .
ENV PORT 8080
ENV APIS your_api.yml
