# Use the base image
FROM svizor/zoomcamp-model:3.11.5-slim AS base

# Set working directory
WORKDIR /app

# Install pipenv in the base image and cache dependencies in a separate stage
FROM base AS builder

COPY ["pyproject.toml","uv.lock", "./"]



# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --frozen --no-cache

# Copy app files after installing dependencies
FROM base
WORKDIR /app
COPY --from=builder /app /app
COPY ["q4.py", "q4-server-test.py", "./"]

# # Sync the project
# RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen

# Expose port and set entrypoint
EXPOSE 9671
# ENTRYPOINT ["uvicorn", "q4:app", "--host", "0.0.0.0","--port","9671"]


# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "q4.py", "--port", "9671", "--host", "0.0.0.0"]
