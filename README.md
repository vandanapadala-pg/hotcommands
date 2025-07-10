<<<<<<< HEAD
# hotcommands
=======
# Hot Commands Framework

This project implements the backend for a dynamic Hot Commands and Spaces framework within a natural language to SQL (NL2SQL) slash command system.

## Features

- ✅ Hot Command registration, execution, update, and deletion
- ✅ Dynamic parameter substitution
- ✅ Space persistence for storing and retrieving outputs
- ✅ Sharing and collaboration via user/team permissions
- ✅ FastAPI-based microservice backend
- ✅ PostgreSQL + Async SQLAlchemy ORM
- ✅ Ready for MCP integration

## Project Structure

```bash
hotcommands-refactored/
├── app/
│   ├── main.py              # FastAPI application
│   ├── database.py          # DB engine & session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── utils.py             # Helper utilities
│   └── routers/             # Endpoint routers
├── docs/
│   ├── requirements_hotcommands.md
│   ├── requirements_nl2sql.md
│   ├── implementation_plan.md
│   ├── mcp_integration_guide.md
│   └── LICENSE
├── README.md
├── requirements.txt
```

## Getting Started

1. Clone this repo
2. Set up your virtual environment
3. Run `uvicorn app.main:app --reload`
4. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI

## Docs

All design documentation and architecture details are in the `/docs` folder.
>>>>>>> d566adb (Initial commit: Add Hot Commands framework)
