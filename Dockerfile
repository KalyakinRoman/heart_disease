FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y curl wget

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
COPY pyproject.toml .
COPY uv.lock .
ENV PATH="/app/.venv/bin/:$PATH"
COPY src src
COPY models models
COPY scripts scripts
RUN chmod +x scripts/entrypoint.sh

RUN uv sync
RUN uv pip install -e .

CMD ["bash", "scripts/entrypoint.sh"]
