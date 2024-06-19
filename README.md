
# CLI Tool

This is a simple CLI tool built with Python and Click for managing a task list.

## Installation

To install the dependencies, run:

```bash
pip install click
```

## Usage

### Setting the Task File Format

You can set the task file format to either JSON or CSV by using the `--format` option. The default format is JSON.

```bash
python task_format.py --format json  # Use JSON format
python task_format.py --format csv   # Use CSV format
```

### Commands

#### Add a Task

To add a task to the list:

```bash
python task_format.py add "Your task description"
```

#### Remove a Task

To remove a task by its ID:

```bash
python task_format.py remove TASK_ID
```

#### List All Tasks

To list all tasks:

```bash
python task_format.py list
```

#### Edit a Task

To edit a task description by its ID:

```bash
python task_format.py edit TASK_ID "New task description"
```

#### Mark a Task

To mark a task as completed or uncompleted by its ID:

```bash
ёpython task_format.py mark TASK_ID --uncompleted # Mark as uncompleted
```

#### Filter Tasks

To filter tasks by their status:

```bash
python task_format.py filter --completed   # Show only completed tasks
python task_format.py filter --uncompleted # Show only uncompleted tasks
```

#### Search Tasks

To search for tasks by a keyword:

```bash
python task_format.py search "keyword"
```

#### Clear All Tasks

To clear all tasks:

```bash
python task_format.py clear
```

#### Clear Completed Tasks

To clear all completed tasks:

```bash
python task_format.py clear_completed
```

### Examples

#### Adding Tasks

```bash
python task_format.py add "Buy milk"
python task_format.py add "Walk the dog"
python task_format.py add "Write report"
```

#### Listing Tasks

```bash
python task_format.py list
```

Output:

```
0: ❌ Buy milk
1: ❌ Walk the dog
2: ❌ Write report
```

#### Marking a Task as Completed

```bash
python task_format.py mark 0 --completed
```

#### Filtering Completed Tasks

```bash
python task_format.py filter --completed
```

Output:

```
0: ✔️ Buy milk
```

#### Searching for a Task

```bash
python task_format.py search "dog"
```

Output:

```
1: ❌ Walk the dog
```

#### Clearing Completed Tasks

```bash
python task_format.py clear_completed
```

#### Listing Remaining Tasks

```bash
python task_format.py list
```

Output:

```
1: ❌ Walk the dog
2: ❌ Write report
```

## Supported Formats

- JSON
- CSV
