# Vercel-Only Deployment (Frontend + Backend API Routes)

This guide explains how to deploy both frontend and backend on Vercel using Next.js API routes.

## Important Considerations

⚠️ **Warning**: This approach has limitations:
- Serverless functions have cold start times
- In-memory storage doesn't persist between requests
- Limited execution time (max 10 seconds for Hobby, 60 seconds for Pro)
- Not suitable for high-traffic applications
- Database connections need to be managed carefully

## Recommended Approach

For a production application, the standard approach is recommended:
- **Frontend**: Deploy to Vercel
- **Backend**: Deploy to Python-compatible platform (Render, AWS, GCP, etc.)

However, if you want to use only Vercel, follow the approach below.

## Vercel-Only Approach with Database

### 1. Set Up a Serverless Database

Choose one of these serverless database options:

#### Option A: Vercel Postgres (Recommended)
1. Sign up for Vercel Postgres
2. Create a new database
3. Get the connection string

#### Option B: PlanetScale MySQL
1. Sign up for PlanetScale
2. Create a new database
3. Get the connection string

#### Option C: Supabase PostgreSQL
1. Sign up for Supabase
2. Create a new project
3. Get the connection string

### 2. Update Dependencies

Add database driver to your package.json:

```bash
npm install @vercel/postgres  # for Vercel Postgres
# OR
npm install mysql2           # for PlanetScale
# OR
npm install @supabase/supabase-js  # for Supabase
```

### 3. Update API Routes with Database Connection

Here's an example using Vercel Postgres:

**app/api/tasks/route.ts:**
```typescript
import { NextRequest, NextResponse } from 'next/server';
import { sql } from '@vercel/postgres';

interface Task {
  id: string;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
}

export async function GET(request: NextRequest) {
  try {
    const { rows } = await sql`SELECT * FROM tasks ORDER BY created_at DESC`;
    return NextResponse.json(rows);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch tasks' },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const { title, description } = await request.json();

    if (!title) {
      return NextResponse.json(
        { error: 'Title is required' },
        { status: 400 }
      );
    }

    const { rows } = await sql`
      INSERT INTO tasks (title, description, completed, created_at)
      VALUES (${title}, ${description || ''}, false, NOW())
      RETURNING *`;

    return NextResponse.json(rows[0], { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create task' },
      { status: 500 }
    );
  }
}
```

### 4. Environment Variables

Add your database connection string to Vercel environment variables:

```
POSTGRES_URL=your-vercel-postgres-url
POSTGRES_PRISMA_URL=your-prisma-url
POSTGRES_URL_NON_POOLING=your-non-pooling-url
```

### 5. Update Next.js Configuration

Update your `next.config.ts` to include database configuration:

```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  serverExternalPackages: ["@vercel/postgres"],
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'localhost',
      },
      {
        protocol: 'http',
        hostname: '127.0.0.1',
      },
    ],
  },
};

export default nextConfig;
```

### 6. Update Database Schema

Create the tasks table in your database:

```sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 7. Update Frontend API Client

Update `lib/api.ts` to use the new API routes:

```typescript
// Use relative paths for Vercel API routes
const API_BASE_URL = '';

// All other functions remain the same but use relative paths
// GET /api/tasks instead of http://external-server/api/v1/tasks
```

### 8. Deployment

1. Push your code to GitHub
2. Connect to Vercel
3. Add environment variables in Vercel dashboard
4. Deploy!

## Comparison: Standard vs Vercel-Only

| Aspect | Standard Approach | Vercel-Only |
|--------|-------------------|-------------|
| Performance | Better | Cold starts possible |
| Persistence | Guaranteed | Depends on DB |
| Scalability | Excellent | Limited by serverless |
| Cost | Separate costs | Combined billing |
| Complexity | Moderate | Higher setup |

## Recommendation

For production applications, use the **Standard Approach**:
- Frontend: Deploy to Vercel
- Backend: Deploy to Render, AWS, GCP, or other Python-compatible platform

The Vercel-Only approach is suitable for:
- Prototypes and demos
- Low-traffic applications
- Learning and experimentation
- When you specifically need all services on one platform

For your Todo application, the standard approach (Vercel for frontend + Render for backend) is recommended for the best performance and reliability.