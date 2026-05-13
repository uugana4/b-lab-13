from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

VALID_PRIORITIES = {"low", "medium", "high"}
VALID_STATUSES = {"pending", "completed"}


def _validate_due_date(due_date: Optional[str]) -> Optional[str]:
    if due_date is None:
        return None
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("due_date must be in YYYY-MM-DD format") from exc
    return due_date


def _validate_priority(priority: str) -> str:
    if priority not in VALID_PRIORITIES:
        raise ValueError("priority must be one of: low, medium, high")
    return priority


def _normalize_labels(labels: Optional[List[str]]) -> List[str]:
    if not labels:
        return []
    normalized = []
    for label in labels:
        if not isinstance(label, str):
            raise ValueError("labels must be a list of strings")
        item = label.strip().lower()
        if item:
            normalized.append(item)
    return sorted(set(normalized))


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    due_date: Optional[str] = None
    priority: str = "medium"
    labels: List[str] = field(default_factory=list)
    status: str = "pending"

    def to_dict(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "labels": list(self.labels),
            "status": self.status,
        }


class TaskTracker:
    """In-memory task tracker with CRUD + search/filter features."""

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def create_task(
        self,
        title: str,
        description: str = "",
        due_date: Optional[str] = None,
        priority: str = "medium",
        labels: Optional[List[str]] = None,
    ) -> Dict[str, object]:
        if not title or not title.strip():
            raise ValueError("title cannot be empty")

        due_date = _validate_due_date(due_date)
        priority = _validate_priority(priority)
        normalized_labels = _normalize_labels(labels)

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip(),
            due_date=due_date,
            priority=priority,
            labels=normalized_labels,
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task.to_dict()

    def list_tasks(self) -> List[Dict[str, object]]:
        tasks = sorted(
            self._tasks.values(),
            key=lambda t: (t.due_date is None, t.due_date or "", t.id),
        )
        return [task.to_dict() for task in tasks]

    def get_task(self, task_id: int) -> Dict[str, object]:
        task = self._tasks.get(task_id)
        if task is None:
            raise KeyError(f"task {task_id} not found")
        return task.to_dict()

    def update_task(
        self,
        task_id: int,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        priority: Optional[str] = None,
        labels: Optional[List[str]] = None,
        status: Optional[str] = None,
    ) -> Dict[str, object]:
        task = self._tasks.get(task_id)
        if task is None:
            raise KeyError(f"task {task_id} not found")

        if title is not None:
            if not title.strip():
                raise ValueError("title cannot be empty")
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if due_date is not None:
            task.due_date = _validate_due_date(due_date)
        if priority is not None:
            task.priority = _validate_priority(priority)
        if labels is not None:
            task.labels = _normalize_labels(labels)
        if status is not None:
            if status not in VALID_STATUSES:
                raise ValueError("status must be one of: pending, completed")
            task.status = status

        return task.to_dict()

    def complete_task(self, task_id: int) -> Dict[str, object]:
        return self.update_task(task_id, status="completed")

    def delete_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"task {task_id} not found")
        del self._tasks[task_id]

    def search_tasks(
        self,
        *,
        query: Optional[str] = None,
        priority: Optional[str] = None,
        label: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[Dict[str, object]]:
        if priority is not None:
            _validate_priority(priority)
        if status is not None and status not in VALID_STATUSES:
            raise ValueError("status must be one of: pending, completed")

        tasks = self.list_tasks()

        if query:
            needle = query.lower().strip()
            tasks = [
                task
                for task in tasks
                if needle in task["title"].lower() or needle in task["description"].lower()
            ]
        if priority:
            tasks = [task for task in tasks if task["priority"] == priority]
        if label:
            label_lc = label.lower().strip()
            tasks = [task for task in tasks if label_lc in task["labels"]]
        if status:
            tasks = [task for task in tasks if task["status"] == status]

        return tasks


if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.create_task(
        "Finish lab report",
        description="Complete Part C reflection draft",
        due_date="2026-05-20",
        priority="high",
        labels=["school", "report"],
    )
    tracker.create_task("Read OWASP notes", priority="medium", labels=["security"])
    for task in tracker.list_tasks():
        print(task)
