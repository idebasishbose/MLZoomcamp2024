# Use the base image
FROM svizor/zoomcamp-model:3.11.5-slim AS base

# Set working directory
WORKDIR /app

# Install pipenv in the base image and cache dependencies in a separate stage
FROM base AS builder
COPY ["uv.lock", "./"]
RUN pip install --no-cache-dir uv && uv sync

# Copy app files after installing dependencies
FROM base
WORKDIR /app
COPY --from=builder /app /app
COPY ["q4.py", "q4-server-test.py", "./"]

# Expose port and set entrypoint
EXPOSE 9671
ENTRYPOINT ["uvicorn", "q4:app", "--host", "0.0.0.0","--port","9671"]
