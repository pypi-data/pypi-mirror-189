# PythonPoet

API for generating Python source code from runtime. It can be useful for generating types' files, interacting with metadata and creating auto-generated code.

### Getting Started

PythonPoet requires Python 3.10 or newer. Install this module using `pip install PythonPoet`.

### Example

```python
from pythonpoet import PythonPoet, ClassBuilder, ClassFieldBuilder

poet = PythonPoet()
poet.add_class(
    ClassBuilder()
    .set_name("Human")
    .add_field(
        ClassFieldBuilder()
        .set_name("name")
        .set_type(str)
    )
    .add_field(
        ClassFieldBuilder()
        .set_name("age")
        .set_type(int)
    )
)

print(poet.deserialize())
```

#### Output:
```python
class Human:
    name: str
    age: int
```
