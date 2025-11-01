from src.utils import CreateDataResult

class Result:
    """Result class"""

    def __init__(self, file: str = "", start: float = 0, end: float = 0, result: str = CreateDataResult.SUCCESS.value, error: str = ""):
        self.file = file
        self.start = start
        self.end = end
        self.result = result
        self.error = error if self.result == CreateDataResult.FAIL.value else ""

    def __str__(self):
        return f"""Result:
        File: {self.file}
        Time: {self.end - self.start} (s)
        Result: {self.result}
        Error: {self.error}
        """
    def __repr__(self):
        return f"""
        File: {self.file}
        Time: {self.end - self.start} (s)
        Result: {self.result}
        Error: {self.error}
        """
    def __dict__(self):
        return {
            "file": self.file,
            "time": self.end - self.start,
            "result": self.result,
            "error": self.error
        }
