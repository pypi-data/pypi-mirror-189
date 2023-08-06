from typing import Any

from pythonpoet.types import Builder, DeserializableType, Argumentable
from pythonpoet.types.import_ import Import, ImportBuilder


class ClassField(DeserializableType):
    """
    Representation of a class field.

    .. warning::

        You shouldn't initialize this class via the `__init__`.
        Use :class:`ClassFieldBuilder` instead.

    Attributes
    ----------
    name : str
        Field's name.
    type : str
        Field's type.
    imports : list[:class:`Import`]
        Required field's imports.
    arguments : list[list[str, :class:`Any`]]
        Field's arguments.
    """

    def __init__(
        self,
        name: str,
        type_: str,
        imports: list[Import],
        arguments: list[list[str, Any]],
    ) -> None:
        self.name = name
        self.type = type_
        self.imports = imports
        self.arguments = arguments

    def get_imports(self) -> str:
        imports_source_code = ""
        for import_ in self.imports:
            imports_source_code += import_.to_string()
        return imports_source_code

    def deserialize(self) -> str:
        if self.arguments is None or len(self.arguments) == 0:
            return f"\t{self.name}: {self.type}\n"
        else:
            arguments_source_code = ""
            for argument_pair in self.arguments:
                arguments_source_code += f"{argument_pair[0]}={argument_pair[1]},"

            return f"\t{self.name}: {self.type}({arguments_source_code})\n"

    def __repr__(self) -> str:
        return (
            f"ClassField<name={self.name}, type={self.type}, "
            f"imports={self.imports}, arguments={self.arguments}>"
        )

    def __str__(self) -> str:
        return self.__repr__()


class ClassFieldBuilder(Builder, Argumentable):
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
        super().__init__()
        self.name: str | None = None
        self.type: str | None = None
        self.imports: list[Import] = []

    def set_name(self, name: str) -> "ClassFieldBuilder":
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

    def set_type(
        self, type_: type, import_: ImportBuilder = None
    ) -> "ClassFieldBuilder":
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
            self.imports.append(import_.build())
        return self

    def build(self) -> ClassField:
        if self.name is None:
            raise ValueError("Field's name cannot be None.")
        elif self.type is None:
            raise ValueError("Field's type cannot be None.")

        return ClassField(self.name, self.type, self.imports, self.arguments)
