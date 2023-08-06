# A many-in-one tool for managing your Markup Language files.

## What is it?

**iotree** is a tool for managing your Markup Language files. It is capable to write and read files in the following formats:

- JSON
- YAML
- TOML
- XML
- And soon more... 😉

The basic goal was to have a small package anyone could add to their project and use it to manage their files. It is also possible to use it as a CLI tool.

## Installation

You cannot install the CLI tool separately for now. You can install it with the following command:

```bash
pip install iotree
```

## Usage

### As a CLI tool

To see what the display function can do, you can use the following command:

```bash
iotree demo
```

For example, the following JSON file (displayed in VSCode)

```json
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
```

will be displayed like this:

![JSON file displayed](https://i.imgur.com/tUSyW3L.png)

While the following YAML file (displayed in VSCode)

```yaml	
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

will be displayed like this:

![YAML file displayed](https://i.imgur.com/t3q5yHS.png)

**Note**: The CLI tool is not yet finished. It is still in development.  
If this just looks like a wrapper around [rich trees](https://rich.readthedocs.io/en/stable/tree.html)) to you, it almost because it is. :wink:

As a CLI tool, the key difference I want to bring is the ability to configure *themes* and *styles*.

Just run the following command to interactively create a theme:

```bash
iotree config init
```

But if you're lazy, just use a file:

```bash
iotree config init from-json my_theme.json
```

For example, the following JSON file

```json
{   
    "name": "My super pseudonym",
    "username": "my.username",
    "symbol": "lgpoint",
    "theme": "bright-blue-green"
}
```

Does _not_ immediately affect the display of the files. You need to use the following command:  
To understand why, you can run

```bash
iotree config ls # same as iotree cfg ls
```

This is what the output looks like:

![iotree config ls](https://i.imgur.com/5R3IMUG.png)

You can see that the theme is registered, but will **not** be used by default.
The best proof of this is to ask who the current user is:

```bash
iotree cfg get last_user
#> ✅ Config found for user arnov
#> arnov
```
So the current user is `arnov`. To use _YOUR_ theme, you need to run the following command:

```bash
iotree cfg set last_user my.username
#> 👷 Config: last_user ===> my.username
```

Now, if you try to render a file, you will see that the theme is used:

```bash
iotree render .\iotree\examples\example.toml
```

Here's what the output looks like:

![iotree render after](https://i.imgur.com/RHROUWg.png)

The theme is now used. 🎉🎉

### As a Python package

You can use the package in your Python project. Here's an example:

```python
from iotree.core.render import build

mydict = {
    "super" : {
        "dict": {
            "just": {
                "for": {
                    "example": "🤷‍♂️"
                }
            }
        }
    }
}

# Build the tree from the dict without hassle

tree = build(mydict) # or build(mydict, theme="my_style", symbol="my_symbol")

# Display the rich tree later

console.print(tree) # or rich.print(tree)
```

But there is more. You can also use the 'all in one' IO from the package:

```python
from iotree.core.io import reader, writer

# Read a file, any extension is supported from the list

dict_one = reader.read("my_file.json")
dict_two = reader.read("my_file.yaml")
dict_three = reader.read("my_file.toml")
dict_four = reader.read("my_file.xml")
dict_five = reader.read("my_file.html")

# ... do some manipulations, like possibly merging the dicts or creating a new one

# Write the dict to a file

writer.write("my_file.json", dict_one)
writer.write("my_file.yaml", dict_two)
writer.write("my_file.toml", dict_three)
writer.write("my_file.xml", dict_four)
# writer.write("my_file.html", dict_five) # Not supported yet
```

Another small feature is the ability to _detect the type of a file_:

```python
dict_guess = reader.read("mysterious_file.not_a_real_extension")
# if the content of the file is one of the supported types, it will be read correctly
```

There's also a functional package, which is not yet documented.  
It allows you to compose functions while displaying rich progress using `rich.progress`.

## Contributing

If you want to contribute, you can do so by forking the repository and creating a pull request.

You can also help me pick the new themes and symbols.

To see the possibilities, just run either of the following commands:

```bash
iotree view themes # or
iotree view symbols # or
iotree view colors
```