from datetime import datetime  

class Task:
    def __init__(self, task_id: int, title: str, description: str, created_at: datetime):
        self.id = task_id               
        self.title = title               
        self.description = description   
        self.created_at = created_at     

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def from_dict(cls, data: dict):
        created_at = datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        return cls(task_id=data["id"], title=data["title"], description=data["description"], created_at=created_at)
