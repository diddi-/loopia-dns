
class LoopiaAPIException(Exception):
    """ Loopia API error """
    def __init__(self, status: str):
        super().__init__(f"Error from Loopia API: {status}")
