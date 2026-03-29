"""待办事项管理"""
from typing import List


class TodoManager:
    def __init__(self):
        self.todos = []

    def update(self, todos: List) -> str:
        if len(todos) > 20:
            raise ValueError("Max 20 todos allowed")

        validated = []
        in_progress_count = 0
        for i, todo in enumerate(todos):
            text = str(todo.get("text", "")).strip()
            status = str(todo.get("status", "pending")).strip().lower()
            todo_id = str(todo.get("id", str(i+1)))
            if not text:
                raise ValueError(f"Todo {todo_id} text cannot be empty")
            if status not in ["pending", "in_progress", "completed"]:
                raise ValueError(f"Todo {todo_id} status must be pending, in_progress, or completed")
            if status == "in_progress":
                in_progress_count += 1
            validated.append({"text": text, "status": status, "id": todo_id})
        if in_progress_count > 1:
            raise ValueError("Only one todo can be in_progress")
        self.todos = validated
        return self.render()

    def render(self) -> str:
        if not self.todos:
            return "No todos."
        lines = []
        for todo in self.todos:
            marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}[todo["status"]]
            lines.append(f"{marker} #{todo['id']}: {todo['text']}")
        done = sum(1 for t in self.todos if t["status"] == "completed")
        lines.append(f"\n({done}/{len(self.todos)} completed)")
        return "\n".join(lines)


TODO = TodoManager()
