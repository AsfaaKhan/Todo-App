# Deployment Guide

This guide explains how to deploy both the frontend and backend of the Todo application.

## Architecture Overview

The application consists of:
- **Frontend**: Next.js application deployed on Vercel
- **Backend**: FastAPI application deployed on a server/cloud platform
- **Database**: PostgreSQL (managed separately)

## Deployment Options

### Option 1: Vercel + Self-Hosted Backend (Recommended)

#### 1. Deploy Backend

The backend can be deployed using several methods:

**A. Using Docker (Recommended for production):**
```bash
# Navigate to the backend directory
cd todo-backend

# Build and run with Docker Compose
docker-compose up -d
```

**B. Direct deployment:**
```bash
# Navigate to the backend directory
cd todo-backend

# Install dependencies
uv sync

# Run the application
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### 2. Deploy Frontend to Vercel

**A. Using Vercel CLI:**
```bash
# Navigate to the frontend directory
cd frontend

# Install Vercel CLI
npm i -g vercel

# Deploy to Vercel
vercel --prod
```

**B. Using Vercel Dashboard:**
1. Push your code to a GitHub repository
2. Go to [Vercel](https://vercel.com)
3. Connect your GitHub repository
4. Set environment variables:
   - `NEXT_PUBLIC_API_BASE_URL`: URL of your deployed backend (e.g., `https://your-backend-domain.com`)
5. Deploy!

#### 3. Environment Variables

**Backend (.env):**
```env
# Database Configuration
DATABASE_URL=postgresql+asyncpg://username:password@host:port/database_name
DATABASE_HOST=your-db-host
DATABASE_PORT=5432
DATABASE_NAME=your_database_name
DATABASE_USER=your_username
DATABASE_PASSWORD=your_secure_password

# Application Configuration
LOG_LEVEL=info
MAX_CONNECTIONS=50
MIN_CONNECTIONS=10

# API Configuration
API_V1_STR=/api/v1
PROJECT_NAME=Todo Backend Service
VERSION=1.0.0
```

**Frontend (Vercel Environment Variables):**
```
NEXT_PUBLIC_API_BASE_URL=https://your-backend-domain.com
```

### Option 2: Cloud Platform Deployment

#### AWS (Elastic Beanstalk, EC2, or ECS)

**Backend:**
- Deploy the FastAPI app using AWS Elastic Beanstalk or containerize with ECS
- Use AWS RDS for PostgreSQL database
- Set up API Gateway if needed for additional security

**Frontend:**
- Deploy to AWS Amplify (alternative to Vercel)
- Or continue using Vercel with AWS-hosted backend

#### Google Cloud Platform

**Backend:**
- Deploy using Google Cloud Run or App Engine
- Use Cloud SQL for PostgreSQL
- Configure load balancing if needed

**Frontend:**
- Deploy to Firebase Hosting (alternative to Vercel)
- Or continue using Vercel

#### Azure

**Backend:**
- Deploy using Azure App Service or Azure Container Instances
- Use Azure Database for PostgreSQL
- Configure Application Gateway if needed

**Frontend:**
- Deploy to Azure Static Web Apps (alternative to Vercel)
- Or continue using Vercel

## Production Configuration

### Backend Production Settings

For production, update your environment variables:

```env
# Production Database URL
DATABASE_URL=postgresql+asyncpg://username:password@prod-db-host:5432/todo_prod

# Performance tuning
MAX_CONNECTIONS=100
MIN_CONNECTIONS=20

# Security
LOG_LEVEL=warning

# API
API_V1_STR=/api/v1
PROJECT_NAME=Todo Backend Service
VERSION=1.0.0
```

### Frontend Production Settings

**Environment Variables in Vercel:**
- `NEXT_PUBLIC_API_BASE_URL`: Production backend URL
- Ensure CORS is configured to allow your frontend domain

### CORS Configuration

The backend currently allows all origins (`allow_origins=["*"]`). For production, update this in `todo-backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.vercel.app"],  # Replace with your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Monitoring and Maintenance

### Backend Health Checks

The backend provides health check endpoints:
- `GET /` - Basic service check
- `GET /health` - Detailed health status

### Database Migrations

For production database changes:
```bash
# Run migrations
alembic upgrade head
```

### Scaling

**Backend:**
- Use multiple workers: `uvicorn app.main:app --workers 4`
- Implement caching (Redis) for high-traffic applications
- Use a load balancer for multiple instances

**Frontend:**
- Vercel automatically handles scaling
- Configure CDN settings in Vercel dashboard

## Troubleshooting

### Common Issues

1. **Frontend can't connect to backend:**
   - Verify `NEXT_PUBLIC_API_BASE_URL` is set correctly
   - Check that the backend is accessible from the internet
   - Verify CORS settings

2. **Database connection issues:**
   - Check database credentials
   - Verify database is accessible from the server
   - Ensure proper network security settings

3. **Deployment failures:**
   - Check environment variables
   - Verify all dependencies are properly configured
   - Review logs for specific error messages

### Logs

**Backend:**
- Check application logs in your deployment platform
- Database connection logs are available through your database provider

**Frontend:**
- Vercel provides built-in logging
- Use browser developer tools for client-side debugging

## Security Considerations

1. **Environment Variables:** Never commit sensitive data to version control
2. **HTTPS:** Ensure both frontend and backend use HTTPS in production
3. **Authentication:** Consider adding authentication for production use
4. **Database Security:** Use strong passwords and proper network isolation
5. **API Security:** Implement rate limiting and input validation