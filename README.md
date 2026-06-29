# IoFT ITR Machine Learning Deployment Template

Astro frontend + FastAPI backend template for deploying machine learning showcases.

Main model communication logic can be found in:

- `./backend/schemas.py`, `./backend/model_interface.py`
- `./frontend/src/lib/api.ts`, `./frontend/src/pages/index.astro`

## Local Setup

### Frontend

```
cd frontend
bun install
bun run dev
```

### Model

Training code in `backend/model.py`, after running, commit the generated `model.pkl` file.

### Backend

```
cd backend
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv run fastapi dev backend.py
```

## Deployment

- Frontend
  - import repo in vercel
  - root: ./frontend
  - set `PUBLIC_API_URL=https://your-backend.onrender.com`

- Backend
  - create web service and import repo
  - root: ./backend
  - build command: `pip install -r requirements.txt`
  - start command: `uvicorn backend:app --host 0.0.0.0 --port $PORT`
