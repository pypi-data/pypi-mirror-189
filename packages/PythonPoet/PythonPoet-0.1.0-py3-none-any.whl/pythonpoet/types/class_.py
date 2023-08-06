from pythonpoet.types import Builder, DeserializableType
from pythonpoet.types.decorator import Decoratorable, Decorator
from pythonpoet.types.field import ClassFieldBuilder, ClassField


def _generate_decorators(decorators: list[Decorator]) -> str:
    decorators_source_code = ''
    for decorator in decorators:
        decorators_source_code += decorator.deserialize()
    return decorators_source_code


def _generate_class_header(class_name: str) -> str:
    return f'class {class_name}:\n'


def _generate_class_fields(fields: list[ClassField]) -> str:
    fields_source_code = ''
    for field in fields:
        fields_source_code += field.deserialize()
    return fields_source_code


class Class(DeserializableType):
    """
    Representation of a class.

    .. warning::

        You shouldn't initialize this class via the `__init__`. Use :class:`ClassBuilder` instead.

    Attributes
    ----------
    name : str
        Class' name.
    fields : list[:class:`ClassField`]
        Class' fields.
    """

    def __init__(self, name: str, fields: list[ClassField], decorators: list[Decorator]) -> None:
        self.name = name
        self.fields = fields
        self.decorators = decorators

    def get_imports(self) -> str:
        imports = ''
        for decorator in self.decorators:
            imports += decorator.get_imports()
        for field in self.fields:
            imports += field.get_imports()
        return imports

    def deserialize(self) -> str:
        return _generate_decorators(self.decorators) + _generate_class_header(self.name) + _generate_class_fields(self.fields)

    def __repr__(self) -> str:
        return f'<Class name={self.name}, decorators={self.decorators}, fields={self.fields}>'

    def __str__(self) -> str:
        return self.__repr__()


class ClassBuilder(Builder, Decoratorable):
    """
    Builder for the :class:`Class`.

    Attributes
    ----------
    name : str or None, default: None
        Class' name.
    fields : list[:class:`ClassField`]
        Class' fields.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str | None = None
        self.fields: list[ClassField] = []

    def set_name(self, name: str) -> 'ClassBuilder':
        """
        Sets class' name.

        Parameters
        ----------
        name : str
            New name of the class.

        Returns
        -------
        :class:`ClassBuilder`
            Updated builder's instance.
        """
        self.name = name
        return self

    def add_field(self, builder: ClassFieldBuilder) -> 'ClassBuilder':
        """
        Adds a new fields from the builder.

        Parameters
        ----------
        builder : :class:`ClassFieldBuilder`
            Builder of the field to be added.

        Returns
        -------
        :class:`ClassBuilder`
            Updated builder's instance.
        """
        self.fields.append(builder.build())
        return self

    def build(self) -> Class:
        if self.name is None:
            raise ValueError('Class\' name cannot be None.')

        return Class(self.name, self.fields, self.get_decorators())
