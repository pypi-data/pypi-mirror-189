# uniqchars
Module for getting the number of unique characters in a string.
Implemented methods for a string and for a list of strings, supports working with the command line.
Methods return cache the results, so that when the method is given a string previously encountered, it will simply retrieve the stored result.

## Contents

* [Example](#example)
* [Installation](#installation)
* [License](#license)

## Example

count_uniq_chars_in_string example:
```python
count_uniq_chars_in_string("test_string")
```

count_uniq_chars_in_list example:
```python
count_uniq_chars_in_list(["test_string1", "test_string1"])
```

execute `main` from command line after installation example:
```python
import uniqchars
uniqchars.main()
```
```lua
main --string "string" --data "file_path"
```


## Installation

### Using PIP

Installing uniqchars using `pip`:

```bash
$ pip install uniqchars
```

## License

`uniqchars` is licensed (MIT license).