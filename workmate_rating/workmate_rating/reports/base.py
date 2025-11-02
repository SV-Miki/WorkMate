from abc import ABC, abstractmethod


class Report(ABC):
    name: str

    @abstractmethod
    def generate(self, rows):
        pass
