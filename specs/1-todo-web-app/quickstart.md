# Quickstart Guide: Todo Web Application

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Basic knowledge of React and TypeScript

## Setup Instructions

### 1. Initialize the Project

```bash
# Create a new Next.js app with TypeScript and Tailwind CSS
npx create-next-app@latest todo-app --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"

# Navigate to the project directory
cd todo-app
```

### 2. Install Dependencies

```bash
# Install react-icons for UI icons
npm install react-icons

# Install shadcn/ui components
npx shadcn-ui@latest init
npx shadcn-ui@latest add card input button checkbox label dialog separator
```

### 3. Project Structure

After setup, your project structure should look like:

```
todo-app/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/
│   ├── ui/ (shadcn/ui components)
│   └── todo/
│       ├── TaskForm.tsx
│       ├── TaskList.tsx
│       ├── TaskItem.tsx
│       └── TaskFilters.tsx
├── hooks/
│   └── useTaskManager.ts
├── lib/
│   ├── types.ts
│   └── utils.ts
├── public/
└── package.json
```

### 4. Development

```bash
# Start the development server
npm run dev

# The app will be available at http://localhost:3000
```

### 5. Key Configuration Files

**Tailwind CSS** is already configured through the Next.js setup process.

**TypeScript** is configured with the default Next.js tsconfig.json.

## Component Development Order

1. **Setup shadcn/ui components** (completed during installation)
2. **Create type definitions** in `lib/types.ts`
3. **Build core UI components** in the `components/todo/` directory
4. **Implement state management** with the custom hook
5. **Integrate components** in the main page

## Running Tests

```bash
# Run unit tests
npm run test

# Run build process
npm run build
```

## Environment Variables

This frontend-only implementation doesn't require environment variables, but for future API integration, you would add:

```
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

## Deployment

```bash
# Build the application
npm run build

# Preview the build locally
npm run start
```

The application is ready for deployment to Vercel, Netlify, or any platform that supports Next.js applications.