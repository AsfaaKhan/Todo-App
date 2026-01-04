import { useState, useEffect } from 'react';
import { Task, TaskListState } from '@/lib/types';
import { validateTaskCreation, validateTaskUpdate, generateTaskId, filterTasks } from '@/lib/utils';

const TASKS_STORAGE_KEY = 'todo-app-tasks';

export const useTaskManager = () => {
  const [state, setState] = useState<TaskListState>(() => {
    // Initialize state from localStorage if available
    const savedTasks = localStorage.getItem(TASKS_STORAGE_KEY);
    if (savedTasks) {
      try {
        const parsedTasks = JSON.parse(savedTasks);
        // Convert string dates back to Date objects
        const tasksWithDates = parsedTasks.map((task: any) => ({
          ...task,
          createdAt: new Date(task.createdAt),
        }));
        return {
          tasks: tasksWithDates,
          filter: 'all',
          editingTaskId: null,
        };
      } catch (error) {
        console.error('Failed to parse tasks from localStorage:', error);
      }
    }
    // Return default state if no saved tasks or parsing failed
    return {
      tasks: [],
      filter: 'all',
      editingTaskId: null,
    };
  });

  // Save tasks to localStorage whenever tasks change
  useEffect(() => {
    localStorage.setItem(TASKS_STORAGE_KEY, JSON.stringify(state.tasks));
  }, [state.tasks]);

  // CRUD Operations with loading states
  const [loading, setLoading] = useState(false);

  const addTask = async (title: string, description: string = '') => {
    setLoading(true);
    try {
      const validation = validateTaskCreation(title, description);

      if (!validation.isValid) {
        throw new Error(validation.errors.join(', '));
      }

      const newTask: Task = {
        id: generateTaskId(),
        title,
        description,
        completed: false,
        createdAt: new Date(),
      };

      setState(prev => ({
        ...prev,
        tasks: [...prev.tasks, newTask],
      }));
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (id: string, title: string, description: string) => {
    setLoading(true);
    try {
      const validation = validateTaskUpdate(id, title, description);

      if (!validation.isValid) {
        throw new Error(validation.errors.join(', '));
      }

      setState(prev => ({
        ...prev,
        tasks: prev.tasks.map(task =>
          task.id === id
            ? { ...task, title, description }
            : task
        ),
      }));
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (id: string) => {
    setLoading(true);
    try {
      setState(prev => ({
        ...prev,
        tasks: prev.tasks.filter(task => task.id !== id),
      }));
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskStatus = async (id: string) => {
    setLoading(true);
    try {
      setState(prev => ({
        ...prev,
        tasks: prev.tasks.map(task =>
          task.id === id
            ? { ...task, completed: !task.completed }
            : task
        ),
      }));
    } finally {
      setLoading(false);
    }
  };

  const setFilter = (filter: 'all' | 'active' | 'completed') => {
    setState(prev => ({
      ...prev,
      filter,
    }));
  };

  const setEditingTask = (id: string | null) => {
    setState(prev => ({
      ...prev,
      editingTaskId: id,
    }));
  };

  return {
    tasks: state.tasks,
    filteredTasks: filterTasks(state.tasks, state.filter),
    filter: state.filter,
    editingTaskId: state.editingTaskId,
    loading,
    addTask,
    updateTask,
    deleteTask,
    toggleTaskStatus,
    setFilter,
    setEditingTask,
  };
};