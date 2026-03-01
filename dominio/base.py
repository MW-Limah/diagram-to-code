class Base:
    """Classe para entidades do domínio."""
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"