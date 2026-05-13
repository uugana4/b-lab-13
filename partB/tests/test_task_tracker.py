import unittest

from src.task_tracker import TaskTracker


class TaskTrackerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tracker = TaskTracker()

    def test_create_task_success(self) -> None:
        task = self.tracker.create_task("Do homework", priority="high", labels=["School", "Urgent"])
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Do homework")
        self.assertEqual(task["priority"], "high")
        self.assertEqual(task["labels"], ["school", "urgent"])

    def test_create_task_rejects_empty_title(self) -> None:
        with self.assertRaises(ValueError):
            self.tracker.create_task("   ")

    def test_create_task_rejects_bad_date(self) -> None:
        with self.assertRaises(ValueError):
            self.tracker.create_task("Do homework", due_date="05/20/2026")

    def test_create_task_rejects_bad_priority(self) -> None:
        with self.assertRaises(ValueError):
            self.tracker.create_task("Do homework", priority="urgent")

    def test_get_task_not_found(self) -> None:
        with self.assertRaises(KeyError):
            self.tracker.get_task(999)

    def test_update_task_fields(self) -> None:
        task = self.tracker.create_task("A", labels=["x"])
        updated = self.tracker.update_task(
            task["id"],
            title="A updated",
            description="new",
            due_date="2026-06-01",
            priority="low",
            labels=["x", "study"],
        )
        self.assertEqual(updated["title"], "A updated")
        self.assertEqual(updated["description"], "new")
        self.assertEqual(updated["due_date"], "2026-06-01")
        self.assertEqual(updated["priority"], "low")
        self.assertEqual(updated["labels"], ["study", "x"])

    def test_complete_task_sets_status(self) -> None:
        task = self.tracker.create_task("Task")
        done = self.tracker.complete_task(task["id"])
        self.assertEqual(done["status"], "completed")

    def test_delete_task_removes(self) -> None:
        task = self.tracker.create_task("Task")
        self.tracker.delete_task(task["id"])
        with self.assertRaises(KeyError):
            self.tracker.get_task(task["id"])

    def test_search_by_query(self) -> None:
        self.tracker.create_task("Read chapter", description="Algorithms chapter 1")
        self.tracker.create_task("Buy milk", description="For breakfast")
        results = self.tracker.search_tasks(query="algo")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Read chapter")

    def test_search_by_label_and_priority(self) -> None:
        self.tracker.create_task("Task 1", priority="high", labels=["school"])
        self.tracker.create_task("Task 2", priority="low", labels=["home"])
        self.tracker.create_task("Task 3", priority="high", labels=["home"])
        results = self.tracker.search_tasks(label="home", priority="high")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Task 3")

    def test_search_by_status(self) -> None:
        task = self.tracker.create_task("Task")
        self.tracker.complete_task(task["id"])
        pending = self.tracker.search_tasks(status="pending")
        completed = self.tracker.search_tasks(status="completed")
        self.assertEqual(len(pending), 0)
        self.assertEqual(len(completed), 1)

    def test_list_tasks_sorted_by_due_date_then_id(self) -> None:
        self.tracker.create_task("No date")
        self.tracker.create_task("Later", due_date="2026-07-01")
        self.tracker.create_task("Sooner", due_date="2026-06-01")
        tasks = self.tracker.list_tasks()
        self.assertEqual([t["title"] for t in tasks], ["Sooner", "Later", "No date"])


if __name__ == "__main__":
    unittest.main()
