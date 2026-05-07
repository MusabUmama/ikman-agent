setup:
	python -m venv .venv && .venv/bin/pip install -r requirements-dev.txt && .venv/bin/playwright install chromium

dev:
	cd backend && ../.venv/bin/uvicorn api.main:app --reload --port 8000

frontend:
	cd frontend && ../.venv/bin/flask --app app.py run --port 5000 --debug

test:
	.venv/bin/pytest tests/ -v --asyncio-mode=auto

lint:
	.venv/bin/ruff check backend/ frontend/ tests/

format:
	.venv/bin/ruff format backend/ frontend/ tests/

typecheck:
	.venv/bin/mypy backend/ --ignore-missing-imports

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
