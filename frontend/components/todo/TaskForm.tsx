import { useState, FormEvent } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { TaskFormData } from '@/lib/types';
import { validateTaskCreation } from '@/lib/utils';
import { FiPlus } from 'react-icons/fi';

interface TaskFormProps {
  onSubmit: (data: TaskFormData) => void;
}

export const TaskForm = ({ onSubmit }: TaskFormProps) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [errors, setErrors] = useState<string[]>([]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    // Validate the input
    const validation = validateTaskCreation(title, description);

    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }

    // Submit the task data if validation passes
    onSubmit({ title, description });

    // Reset form
    setTitle('');
    setDescription('');
    setErrors([]);
  };

  return (
    <Card className="w-full" role="form" aria-labelledby="task-form-title">
      <CardHeader>
        <CardTitle id="task-form-title">Add New Task</CardTitle>
        <CardDescription id="task-form-description">Create a new task to manage your work</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4" aria-describedby={errors.length > 0 ? "task-form-errors" : undefined}>
          <div className="space-y-2">
            <Label htmlFor="task-title-input">Title *</Label>
            <Input
              id="task-title-input"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter task title"
              required
              aria-invalid={errors.length > 0 ? "true" : "false"}
              aria-describedby={errors.length > 0 ? "task-form-errors" : undefined}
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="task-description-input">Description</Label>
            <Input
              id="task-description-input"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Enter task description (optional)"
              aria-describedby="task-description-help"
            />
            <p id="task-description-help" className="text-sm text-gray-500">
              Optional description for your task
            </p>
          </div>

          {errors.length > 0 && (
            <div
              id="task-form-errors"
              className="text-red-500 text-sm p-2 bg-red-50 rounded border border-red-200"
              role="alert"
              aria-live="polite"
            >
              {errors.map((error, index) => (
                <div key={index}>{error}</div>
              ))}
            </div>
          )}

          <Button type="submit" className="w-full" aria-label="Add new task">
            <FiPlus className="mr-2 h-4 w-4" aria-hidden="true" />
            Add Task
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};