# memory_archive/__init__.py
from .mutation_history_log import load
mutation_history_log = type("MutationHistoryLog", (), {"load": staticmethod(load)})()