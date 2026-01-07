# Deploying Backend to Render

This guide explains how to deploy your FastAPI backend to Render, a cloud platform that's perfect for hosting web services.

## Prerequisites

- A Render account (sign up at [https://render.com](https://render.com))
- Your backend code pushed to a GitHub repository
- A PostgreSQL database (you can create one on Render or use an external provider)

## Step-by-Step Deployment Guide

### 1. Prepare Your Repository

Make sure your repository contains:
- `todo-backend/` directory with your FastAPI application
- `Dockerfile` (already provided in the repository)
- `requirements.txt` with all dependencies
- Proper `.gitignore` file

### 2. Create a Render Web Service

1. Log in to your [Render dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository containing the Todo application
4. Select the repository that contains your backend code

### 3. Configure the Web Service

**Build Settings:**
- **Environment**: `Docker`
- **Dockerfile Path**: `todo-backend/Dockerfile` (if you move the Dockerfile to the todo-backend directory) or just `Dockerfile` if you keep it at the root

If you prefer to keep the Dockerfile in the todo-backend directory, you can copy it there:

```bash
# From the project root
cp todo-backend/Dockerfile ./
```

**Root Directory:** `todo-backend`

**Plan Type:** Free (for development) or Starter/Paid for production

### 4. Environment Variables

Add the following environment variables in the Render dashboard:

```
DATABASE_URL=postgresql+asyncpg://username:password@host:port/database_name
DATABASE_HOST=your-db-host
DATABASE_PORT=5432
DATABASE_NAME=your_database_name
DATABASE_USER=your_username
DATABASE_PASSWORD=your_secure_password
LOG_LEVEL=info
MAX_CONNECTIONS=20
MIN_CONNECTIONS=5
API_V1_STR=/api/v1
PROJECT_NAME=Todo Backend Service
VERSION=1.0.0
```

### 5. Create a PostgreSQL Database on Render (Optional)

If you want to create a PostgreSQL database on Render:

1. In your Render dashboard, click "New +" and select "PostgreSQL"
2. Give your database a name
3. Render will automatically create the database and provide connection details
4. Use the connection string provided by Render for your `DATABASE_URL`

### 6. Alternative: Using Render's External Database

You can also connect to any PostgreSQL database by providing the connection details in the environment variables.

### 7. Health Check Configuration

Render will automatically monitor your service. You can set the health check URL to:
```
https://your-service-name.onrender.com/health
```

### 8. Environment-Specific Configuration

For Render deployment, you might want to update the CORS settings in `todo-backend/app/main.py` to be more specific:

```python
# Replace the current CORS configuration with:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.vercel.app"],  # Your Vercel frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 9. Build and Deploy

1. Render will automatically build your Docker image using the Dockerfile
2. The service will be deployed with your environment variables
3. Monitor the build logs in the Render dashboard for any issues

### 10. Post-Deployment Steps

1. **Verify deployment**: Check that your service is running at `https://your-service-name.onrender.com`
2. **Test endpoints**:
   - `GET /` - Should return service info
   - `GET /health` - Should return health status
   - `GET /api/v1/tasks` - Should return tasks (empty array initially)
3. **Update frontend**: Set `NEXT_PUBLIC_API_BASE_URL` in your Vercel deployment to your Render backend URL

## Sample Render Blueprint (render.yaml)

If you prefer to use a render.yaml file for infrastructure as code, create a `render.yaml` file in your repository root:

```yaml
services:
  - type: web
    name: todo-backend
    env: docker
    region: oregon  # or frankfurt for EU
    plan: free
    branch: main
    healthCheckPath: /health
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: todo-db
          property: connectionString
      - key: LOG_LEVEL
        value: info
      - key: API_V1_STR
        value: /api/v1

databases:
  - name: todo-db
    region: oregon
    plan: free
```

## Troubleshooting

### Common Issues:

1. **Build failures**: Check that all dependencies in `requirements.txt` are compatible
2. **Database connection**: Ensure your database URL is correctly formatted
3. **Port binding**: The application should bind to the port specified by the `PORT` environment variable (Render sets this automatically)

### Environment Variables in Production:

Render automatically sets the `PORT` environment variable. Make sure your application can use this if needed, though your current setup with uvicorn should work fine.

## Connecting Frontend to Render Backend

After deploying your backend to Render:

1. Get your backend URL (e.g., `https://your-todo-backend.onrender.com`)
2. Update your frontend deployment on Vercel:
   - Set `NEXT_PUBLIC_API_BASE_URL` to your Render backend URL
   - Redeploy your frontend

## Scaling Considerations

- **Free plan**: Limited resources, suitable for development/testing
- **Starter plan**: Better performance, suitable for small applications
- **Pro plan**: Higher performance and more resources for production applications

## Security Best Practices

1. Use strong database passwords
2. Keep your API keys secure
3. Regularly update dependencies
4. Monitor your application logs
5. Use HTTPS for all connections