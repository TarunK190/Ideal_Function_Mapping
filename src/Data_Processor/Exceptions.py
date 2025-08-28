"""
Custom exceptions for the assignment.
"""

class DataLoadingError(Exception):
    """Exception raised when data loading fails."""
    pass


class FunctionSelectionError(Exception):
    """Exception raised when function selection fails."""
    pass


class TestMappingError(Exception):
    __test__ = False
    """Exception raised when test data mapping fails."""
    pass


class DatabaseError(Exception):
    """Exception raised when database operations fail."""
    pass


class VisualizationError(Exception):
    """Exception raised when visualization fails."""
    pass