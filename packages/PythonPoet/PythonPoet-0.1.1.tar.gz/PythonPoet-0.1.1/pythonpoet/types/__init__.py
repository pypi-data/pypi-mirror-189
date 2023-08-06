from typing import Any


class DeserializableType:
    """
    Represents types that can be deserialized.
    """

    def get_imports(self) -> str:
        """
        Returns type's imports required for deserialization.

        Returns
        -------
        str
            Type's imports.
        """
        raise NotImplementedError

    def deserialize(self) -> str:
        """
        Deserializes this type.

        Raises
        ------
        NotImplementedError
            If type hasn't overloaded this method.

        Returns
        -------
        str
            Deserialized (in source code) type.
        """
        raise NotImplementedError


class Builder:
    """
    Represents types' builders.
    """

    def build(self):  # TODO: return type
        """
        Builds this builder.

        Raises
        ------
        ValueError
            If one of the required fields is None.

        Returns
        -------
        T
            Built type's class instance.
        """
        raise NotImplementedError


class Argumentable:
    """
    Represents types that can have arguments.
    """

    def __init__(self) -> None:
        self.arguments: list[list[str, Any]] = []

    def add_argument(self, key: str, value: Any):  # TODO: return type
        """
        Adds a new argument to the list of arguments.

        Parameters
        ----------
        key : str
            Name of the argument.
        value : :class:`Any`
            Value of the argument.

        Examples
        --------
        .. code-block:: python3

            DecoratorBuilder()
            .set_name('secured')
            .add_argument('value', True)
            .build()
            # Result: @secured(value=True)


        Returns
        -------
        T
            Updated builder's class.
        """
        self.arguments.append([key, value])
        return self
