# Todo Frontend

This is a full-stack Todo application with a Next.js frontend and a Python/FastAPI backend. The frontend connects to a backend service for task management.

## Getting Started

First, make sure the backend service is running. Refer to the backend documentation for setup instructions.

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Environment Variables

Create a `.env.local` file in the root of the frontend directory with the following:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Replace `http://localhost:8000` with the actual URL of your backend service.

## API Integration

This frontend connects to a backend service that provides:
- Task CRUD operations (Create, Read, Update, Delete)
- Task status management (complete/incomplete)
- Data persistence in PostgreSQL

The API endpoints used are:
- `GET /api/v1/tasks` - Retrieve all tasks
- `POST /api/v1/tasks` - Create a new task
- `PUT /api/v1/tasks/{id}` - Update a task
- `DELETE /api/v1/tasks/{id}` - Delete a task
- `PATCH /api/v1/tasks/{id}/status` - Update task completion status

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

### Deployment Steps:

1. **Prepare Environment Variables**:
   Before deploying, you need to set the `NEXT_PUBLIC_API_BASE_URL` environment variable to point to your deployed backend service:

   ```env
   NEXT_PUBLIC_API_BASE_URL=https://your-backend-domain.com
   ```

2. **Deploy with Vercel CLI** (optional):
   ```bash
   npm i -g vercel
   vercel --prod
   ```

3. **Deploy via Vercel Dashboard**:
   - Push your code to a Git repository
   - Connect your repository to [Vercel](https://vercel.com)
   - Add the environment variable `NEXT_PUBLIC_API_BASE_URL` in the Vercel dashboard
   - Deploy!

### Important Notes:
- This frontend expects a backend service to be available at the configured API URL
- For production deployment, ensure your backend service is also deployed and accessible
- The backend should expose the same API endpoints as documented in the API Integration section
- CORS should be configured to allow requests from your frontend domain

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Backend Integration

This frontend is designed to work with the Todo Backend Service. Make sure to deploy and configure the backend service before deploying this frontend. The backend service should provide the API endpoints as documented above.
