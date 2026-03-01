import json


class Base:
    """Classe base para entidades do domínio."""

    def __repr__(self) -> str:
        def serialize(obj):
            if hasattr(obj, "__dict__"):
                return obj.__dict__
            return str(obj)

        json_str = json.dumps(
            self.__dict__,
            default=serialize,
            indent=4,
            ensure_ascii=False
        )

        return f"{self.__class__.__name__}:\n{json_str}"