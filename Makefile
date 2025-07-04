start:
	# uv run fastapi dev fast-api/main.py
	# uv run uvicorn --reload --app-dir fast-api main:app - Команда идентична следующей
	uv run uvicorn --reload fast-api.main:app