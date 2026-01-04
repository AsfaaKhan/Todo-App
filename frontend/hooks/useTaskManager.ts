import { useState, useEffect } from 'react';
import { Task, TaskListState } from '@/lib/types';
import { validateTaskCreation, validateTaskUpdate, filterTasks } from '@/lib/utils';
import { todoApi } from '@/lib/api';

export const useTaskManager = () => {
  const [state, setState] = useState<TaskListState>({
    tasks: [],
    filter: 'all',
    editingTaskId: null,
  });

  // Loading state for API operations
  const [loading, setLoading] = useState(false);
  // Track if we've loaded data from the backend
  const [initialized, setInitialized] = useState(false);

  // Load tasks from the backend when the component mounts
  useEffect(() => {
    const loadTasks = async () => {
      setLoading(true);
      try {
        const tasks = await todoApi.getTasks();
        setState(prev => ({
          ...prev,
          tasks,
        }));
      } catch (error) {
        console.error('Failed to load tasks from backend:', error);
        // Still set initialized to true to avoid infinite loading
      } finally {
        setLoading(false);
        setInitialized(true);
      }
    };

    loadTasks();
  }, []);

  // CRUD Operations with backend API
  const addTask = async (title: string, description: string = '') => {
    setLoading(true);
    try {
      const validation = validateTaskCreation(title, description);

      if (!validation.isValid) {
        throw new Error(validation.errors.join(', '));
      }

      const newTask = await todoApi.createTask(title, description);

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

      const updatedTask = await todoApi.updateTask(id, title, description);

      setState(prev => ({
        ...prev,
        tasks: prev.tasks.map(task =>
          task.id === id ? updatedTask : task
        ),
      }));
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (id: string) => {
    setLoading(true);
    try {
      await todoApi.deleteTask(id);

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
      // Find the current task to get its current status
      const currentTask = state.tasks.find(task => task.id === id);
      if (!currentTask) {
        throw new Error(`Task with id ${id} not found`);
      }

      const updatedTask = await todoApi.toggleTaskStatus(id, !currentTask.completed);

      setState(prev => ({
        ...prev,
        tasks: prev.tasks.map(task =>
          task.id === id ? updatedTask : task
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

  // Filter tasks based on current filter
  const filteredTasks = state.tasks.filter(task => {
    if (state.filter === 'active') {
      return !task.completed;
    } else if (state.filter === 'completed') {
      return task.completed;
    }
    return true; // 'all' filter
  });

  return {
    tasks: state.tasks,
    filteredTasks,
    filter: state.filter,
    editingTaskId: state.editingTaskId,
    loading: loading || !initialized,
    addTask,
    updateTask,
    deleteTask,
    toggleTaskStatus,
    setFilter,
    setEditingTask,
  };
};