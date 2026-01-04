import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import { FiFilter } from 'react-icons/fi';

interface TaskFiltersProps {
  currentFilter: 'all' | 'active' | 'completed';
  onFilterChange: (filter: 'all' | 'active' | 'completed') => void;
  taskCount: number;
  completedCount: number;
}

export const TaskFilters = ({
  currentFilter,
  onFilterChange,
  taskCount,
  completedCount
}: TaskFiltersProps) => {
  const activeCount = taskCount - completedCount;

  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold flex items-center">
          <FiFilter className="mr-2 h-4 w-4" />
          Filter Tasks
        </h2>
        <div className="text-sm text-gray-500 dark:text-gray-400">
          {taskCount} {taskCount === 1 ? 'task' : 'tasks'}
        </div>
      </div>

      <div className="flex flex-wrap gap-2">
        <Button
          variant={currentFilter === 'all' ? 'default' : 'outline'}
          size="sm"
          onClick={() => onFilterChange('all')}
        >
          All ({taskCount})
        </Button>
        <Button
          variant={currentFilter === 'active' ? 'default' : 'outline'}
          size="sm"
          onClick={() => onFilterChange('active')}
        >
          Active ({activeCount})
        </Button>
        <Button
          variant={currentFilter === 'completed' ? 'default' : 'outline'}
          size="sm"
          onClick={() => onFilterChange('completed')}
        >
          Completed ({completedCount})
        </Button>
      </div>

      <Separator className="my-4" />
    </div>
  );
};