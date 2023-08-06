from pythonpoet.types import Builder, DeserializableType
from pythonpoet.types.import_ import Import


class ClassField(DeserializableType):
    """
    Representation of a class' field.

    .. warning::

        You shouldn't initialize this class via the `__init__`. Use :class:`ClassFieldBuilder` instead.

    Attributes
    ----------
    name : str
        Field's name.
    type : str
        Field's type.
    imports : list[:class:`Import`]
        Required field's imports.
    """

    def __init__(self, name: str, type_: str, imports: list[Import]) -> None:
        self.name = name
        self.type = type_
        self.imports = imports

    def get_imports(self) -> str:
        imports_source_code = ''
        for import_ in self.imports:
            imports_source_code += import_.to_string()
        return imports_source_code

    def deserialize(self) -> str:
        return f'\t{self.name}: {self.type}\n'

    def __repr__(self) -> str:
        return f'ClassField<name={self.name}, type={self.type}>'

    def __str__(self) -> str:
        return self.__repr__()


class ClassFieldBuilder(Builder):
    """
    Builder for the :class:`ClassField`.

    Attributes
    ----------
    name : str or None, default: None
        Field's name.
    type : str or None, default: None
        Field's type.
    imports : list[:class:`Import`]
        Required field's imports.
    """

    def __init__(self) -> None:
        self.name: str | None = None
        self.type: str | None = None
        self.imports: list[Import] = []

    def set_name(self, name: str) -> 'ClassFieldBuilder':
        """
        Sets field's name.

        Parameters
        ----------
        name : str
            New name of the field.

        Returns
        -------
        :class:`ClassFieldBuilder`
            Updated builder's instance.
        """
        self.name = name
        return self

    def set_type(self, type_: type, import_: Import = None) -> 'ClassFieldBuilder':
        """
        Sets field's type.

        Parameters
        ----------
        import_ : :class:`Import`, optional, default: None
            Import path for the type (if it isn't default).
        type_ : :class:`type`
            New type of the field.

        Returns
        -------
        :class:`ClassFieldBuilder`
            Updated builder's instance.
        """
        self.type = type_.__name__
        if import_ is not None:
            self.imports.append(import_)
        return self

    def build(self) -> ClassField:
        if self.name is None:
            raise ValueError('Field\'s name cannot be None.')
        elif self.type is None:
            raise ValueError('Field\'s type cannot be None.')

        return ClassField(self.name, self.type, self.imports)
