class Base:
    """Classe base para entidades do domínio."""

    def __repr__(self) -> str:
        atributos = ", ".join(
            f"{chave}={valor}"
            for chave, valor in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({atributos})"