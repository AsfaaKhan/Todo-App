import { useState } from 'react';
import { Checkbox } from '@/components/ui/checkbox';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardFooter } from '@/components/ui/card';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogClose,
} from '@/components/ui/dialog';
import { Task } from '@/lib/types';
import { validateTaskUpdate } from '@/lib/utils';
import { FiCheck, FiX, FiEdit, FiTrash } from 'react-icons/fi';

interface TaskItemProps {
  task: Task;
  onToggle: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  onUpdate: (id: string, title: string, description: string) => void;
}

export const TaskItem = ({ task, onToggle, onEdit, onDelete, onUpdate }: TaskItemProps) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description);
  const [errors, setErrors] = useState<string[]>([]);
  const [showDeleteDialog, setShowDeleteDialog] = useState(false);

  const handleSaveEdit = () => {
    // Validate the updated task data
    const validation = validateTaskUpdate(task.id, editTitle, editDescription);

    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }

    // Call the update function passed from parent
    onUpdate(task.id, editTitle, editDescription);

    // Exit edit mode
    setIsEditing(false);
    setErrors([]);
  };

  const handleCancelEdit = () => {
    // Reset to original values
    setEditTitle(task.title);
    setEditDescription(task.description);
    setIsEditing(false);
    setErrors([]);
  };

  const handleDeleteConfirm = () => {
    onDelete(task.id);
    setShowDeleteDialog(false);
  };

  const handleEditKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Escape') {
      handleCancelEdit();
    } else if (e.key === 'Enter' && e.ctrlKey) {
      handleSaveEdit();
    }
  };

  return (
    <Card className={`w-full ${task.completed ? 'bg-gray-100 dark:bg-gray-800/50' : ''}`}>
      <CardContent className="p-4">
        {isEditing ? (
          <div className="space-y-3">
            <input
              type="text"
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
              className="w-full p-2 border rounded text-lg font-medium"
              autoFocus
              onKeyDown={handleEditKeyDown}
            />
            <textarea
              value={editDescription}
              onChange={(e) => setEditDescription(e.target.value)}
              className="w-full p-2 border rounded min-h-[80px]"
              onKeyDown={handleEditKeyDown}
            />
            {errors.length > 0 && (
              <div className="text-red-500 text-sm">
                {errors.map((error, index) => (
                  <div key={index}>{error}</div>
                ))}
              </div>
            )}
          </div>
        ) : (
          <div className="flex items-start space-x-3">
            <Checkbox
              id={`task-${task.id}`}
              checked={task.completed}
              onCheckedChange={() => onToggle(task.id)}
              aria-label={task.completed ? "Mark task as incomplete" : "Mark task as complete"}
            />
            <div className="flex-1 min-w-0">
              <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : 'text-gray-900 dark:text-gray-100'}`}>
                {task.title}
              </h3>
              {task.description && (
                <p className={`mt-1 text-sm ${task.completed ? 'text-gray-400' : 'text-gray-600 dark:text-gray-400'}`}>
                  {task.description}
                </p>
              )}
              <p className="mt-1 text-xs text-gray-500">
                Created: {task.createdAt.toLocaleDateString()}
              </p>
            </div>
          </div>
        )}
      </CardContent>
      {!isEditing && (
        <CardFooter className="flex justify-end space-x-2 p-4 pt-0">
          <Button
            variant="outline"
            size="sm"
            onClick={() => onEdit(task.id)}
            aria-label="Edit task"
          >
            <FiEdit className="h-4 w-4" />
          </Button>
          <Dialog open={showDeleteDialog} onOpenChange={setShowDeleteDialog}>
            <DialogTrigger asChild>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setShowDeleteDialog(true)}
                aria-label="Delete task"
              >
                <FiTrash className="h-4 w-4" />
              </Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Confirm Deletion</DialogTitle>
                <DialogDescription>
                  Are you sure you want to delete the task "{task.title}"? This action cannot be undone.
                </DialogDescription>
              </DialogHeader>
              <DialogFooter>
                <DialogClose asChild>
                  <Button variant="outline">Cancel</Button>
                </DialogClose>
                <Button variant="destructive" onClick={handleDeleteConfirm}>Delete</Button>
              </DialogFooter>
            </DialogContent>
          </Dialog>
        </CardFooter>
      )}
      {isEditing && (
        <CardFooter className="flex justify-end space-x-2 p-4 pt-0">
          <Button
            variant="outline"
            size="sm"
            onClick={handleCancelEdit}
          >
            <FiX className="mr-1 h-4 w-4" />
            Cancel
          </Button>
          <Button
            size="sm"
            onClick={handleSaveEdit}
          >
            <FiCheck className="mr-1 h-4 w-4" />
            Save
          </Button>
        </CardFooter>
      )}
    </Card>
  );
};