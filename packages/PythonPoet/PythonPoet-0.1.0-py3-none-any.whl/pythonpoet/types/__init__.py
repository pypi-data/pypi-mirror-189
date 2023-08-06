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
