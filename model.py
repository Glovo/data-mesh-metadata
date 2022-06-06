
class ValidationException(Exception):
    """Raised when validation fails"""

    def __init__(self, msg):
        super().__init__(msg)