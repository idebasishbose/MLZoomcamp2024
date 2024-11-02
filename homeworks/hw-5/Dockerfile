# Use the base image
FROM svizor/zoomcamp-model:3.11.5-slim AS base

# Set working directory
WORKDIR /app

# Install pipenv in the base image and cache dependencies in a separate stage
FROM base AS builder
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install --no-cache-dir pipenv && pipenv install --system --deploy

# Copy app files after installing dependencies
FROM base
WORKDIR /app
COPY --from=builder /app /app
COPY ["q6.py", "q6-server-test.py", "./"]

# Expose port and set entrypoint
EXPOSE 9670
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9670", "q6:app"]
