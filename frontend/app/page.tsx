'use client';

import { useTaskManager } from '@/hooks/useTaskManager';
import { TaskForm } from '@/components/todo/TaskForm';
import { TaskList } from '@/components/todo/TaskList';
import { TaskFilters } from '@/components/todo/TaskFilters';
import { TaskFormData } from '@/lib/types';

export default function Home() {
  const {
    tasks,
    filteredTasks,
    filter,
    loading,
    addTask,
    toggleTaskStatus,
    deleteTask,
    updateTask,
    setEditingTask,
    setFilter
  } = useTaskManager();

  // Calculate counts for the filters component
  const completedCount = tasks.filter(task => task.completed).length;

  const handleAddTask = (data: TaskFormData) => {
    addTask(data.title, data.description);
  };

  const handleToggleTask = (id: string) => {
    toggleTaskStatus(id);
  };

  const handleDeleteTask = (id: string) => {
    deleteTask(id);
  };

  const handleUpdateTask = (id: string, title: string, description: string) => {
    updateTask(id, title, description);
  };

  const handleFilterChange = (newFilter: 'all' | 'active' | 'completed') => {
    setFilter(newFilter);
  };

  const handleEditTask = (id: string) => {
    setEditingTask(id);
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black p-4">
      <main className="w-full max-w-2xl">
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-zinc-50 mb-2">Todo App</h1>
          <p className="text-gray-600 dark:text-zinc-400">Manage your tasks efficiently</p>
        </div>

        {loading && (
          <div className="flex justify-center mb-4">
            <div className="text-gray-500 dark:text-gray-400">Loading...</div>
          </div>
        )}

        <div className="space-y-6">
          <TaskForm onSubmit={handleAddTask} />
          <TaskFilters
            currentFilter={filter}
            onFilterChange={handleFilterChange}
            taskCount={tasks.length}
            completedCount={completedCount}
          />
          <TaskList
            tasks={filteredTasks}
            onToggle={handleToggleTask}
            onEdit={handleEditTask}
            onDelete={handleDeleteTask}
            onUpdate={handleUpdateTask}
          />
        </div>
      </main>
    </div>
  );
}
