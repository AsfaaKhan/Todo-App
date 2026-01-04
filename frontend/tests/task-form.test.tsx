// Basic test for TaskForm component to verify User Story 1 acceptance scenarios
// This is a conceptual test file - for actual implementation you would use a testing framework like Jest + React Testing Library

import { render, screen, fireEvent } from '@testing-library/react';
import { TaskForm } from '@/components/todo/TaskForm';
import { TaskFormData } from '@/lib/types';

// Mock the onSubmit function to test form submission
const mockOnSubmit = jest.fn();

describe('TaskForm Component', () => {
  beforeEach(() => {
    mockOnSubmit.mockClear();
  });

  test('acceptance scenario 1: adds new task with title and description', () => {
    // Given user is on the todo app page
    render(<TaskForm onSubmit={mockOnSubmit} />);

    // When user enters a title and description and clicks "Add Task"
    const titleInput = screen.getByLabelText(/title/i);
    fireEvent.change(titleInput, { target: { value: 'Test Task' } });

    const descriptionInput = screen.getByLabelText(/description/i);
    fireEvent.change(descriptionInput, { target: { value: 'Test Description' } });

    const submitButton = screen.getByRole('button', { name: /add task/i });
    fireEvent.click(submitButton);

    // Then the new task appears in the task list with status "incomplete"
    expect(mockOnSubmit).toHaveBeenCalledWith({
      title: 'Test Task',
      description: 'Test Description'
    });
  });

  test('acceptance scenario 2: adds task with title but no description', () => {
    // Given user has entered a title but no description
    render(<TaskForm onSubmit={mockOnSubmit} />);

    const titleInput = screen.getByLabelText(/title/i);
    fireEvent.change(titleInput, { target: { value: 'Test Task' } });

    // Don't enter a description (it should default to empty string)

    const submitButton = screen.getByRole('button', { name: /add task/i });
    fireEvent.click(submitButton);

    // Then the task is added with the provided title and empty description
    expect(mockOnSubmit).toHaveBeenCalledWith({
      title: 'Test Task',
      description: ''
    });
  });

  test('shows validation errors for empty title', () => {
    render(<TaskForm onSubmit={mockOnSubmit} />);

    const submitButton = screen.getByRole('button', { name: /add task/i });
    fireEvent.click(submitButton);

    // Should show error about required title
    expect(screen.getByText(/title is required/i)).toBeInTheDocument();
  });
});