class Todo:
    def __init__(self, id, content, done):
        self.id = id
        self.content = content
        self.done = done

    def __str__(self):
        is_done = "done" if self.done else "not done"
        return f"{self.content}, {is_done}"
