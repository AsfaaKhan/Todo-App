# Todo Full-Stack Application

A full-stack Todo application with Next.js frontend and FastAPI backend with PostgreSQL persistence.

## Features

- Full-stack web application with Next.js frontend and FastAPI backend
- Task management: Add, view, update, delete, and mark tasks as complete/incomplete
- Responsive UI with modern design
- Persistent storage with PostgreSQL database
- RESTful API with CRUD operations
- Real-time updates and validation

## Prerequisites

- Node.js and npm for frontend
- Python 3.12 or higher for backend
- UV package manager
- PostgreSQL database (or SQLite for development)

## Setup

1. Clone the repository
2. Install backend dependencies:
   ```bash
   cd todo-backend
   uv sync
   ```
3. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

1. Start the backend service:
   ```bash
   cd todo-backend
   uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
2. Start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## Recent Updates
- Fixed task update functionality by ensuring consistent ID types between frontend and backend
- Updated API client to convert numeric IDs to strings
- Fixed Next.js configuration warnings
- Added proper database connection handling for development
- Added Vercel deployment configuration

## Deployment

For complete deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Frontend (Next.js) on Vercel
The frontend is configured for deployment on Vercel. See `frontend/README.md` for detailed deployment instructions.

### Backend (FastAPI) on Render (Recommended)
The backend is optimized for deployment on Render. See [RENDER-DEPLOYMENT.md](RENDER-DEPLOYMENT.md) for complete step-by-step instructions.

### Other Backend Deployment Options
The backend service can also be deployed using various methods including Docker, cloud platforms, or traditional servers. See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment options.