from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    department: str
    job_title: str
    worker_type: str
