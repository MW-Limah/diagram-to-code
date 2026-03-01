class Contato:
    """Representa contatos."""

    def __init__( self, tel1: str, tel2: str, cel1: str, cel2: str, email: str) -> None:
        self.tel1 = tel1
        self.tel2 = tel2
        self.cel1 = cel1
        self.cel2 = cel2
        self.email = email