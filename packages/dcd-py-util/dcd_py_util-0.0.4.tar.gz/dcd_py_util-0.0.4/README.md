# dcd_py_util

Module that brings together useful tools for Python applications.

- ```Preferences```: provides configuration info read from a JSON file.
- ```Logger```: simplifies logging configuration by reading it from a JSON configuration file (the JSON file
  from ```Preferences```).
- ```Encryption```: provides an easy way to encrypt and decrypt text stored in open configuration files, protecting
  passwords and sensitive data.

## How to use

### ```Preferences```

1. Create a JSON file named ```prefs_config.json``` and place it in the root folder of your application.
2. Include the configuration need in the prefs_config.json file in JSON format. Example:

```
{
  "object": {
    "string": "bla bla bla",
    "number": 123,
    "float": 456.7,
    "boolean": true,
    "date": "2023-01-01",
    "array": [
        {
            "key1": "val1",
            "key2": "val2"
        },
        {
            "another_key1": "another_val1",
            "another_key2": "another_val2"
        }
    ]
  }
}
```

3. Any data in a valid JSON format can be placed in the ```prefs_config.json```.
4. The configuration data will be available as a Python dictionary.
5. To access the Python dictonary, use the ```Preferences``` class like the example below:

```
from dcd_py_util.prefs_config import Preferences

prefs: Preferences = Preferences().get_preferences()

print(prefs[logging][name])
```

6. The ```Preferences``` is a [singleton](https://design-patterns-ebook.readthedocs.io/en/latest/creational/singleton/).
7. It's possible to update the prefs file by using the method ```Preferences().save_prefs()``` after change a value in
   the prefs dictionary.
8. The change will be visible to all variables (pointers) to the prefs dictionary.

### ```Logger```

1. The logger configures two log output handlers: console and file. The file handler makes logfile rotation soon it
   achives the configured max size. The number logfiles kept can be also configured. The default values are 10 Mb as max
   size and 30 files to be kept.
2. Place the ```logging``` configuration in the ```prefs_config.json``` like in the below:

```
{
  "logging": {
    "name": "logger_name",
    "folder": "./log",
    "filename": "log_filename.log",
    "max_size": 10485760,
    "file_count": 30,
    "console_level": "DEBUG",
    "file_level": "DEBUG"
  }
}
```

2. The attribute ```max_size``` informs the max size of the file in bytes. The attribute ```file_count``` informs the
   number of files to be kept. The rest of the attributes are pretty straightforward.
3. The encoding used for the file handler if ```utf-8```.
4. To access the logger in your Python code follow the example below:

```
from dcd_py_util.logger import Logger

logger: Logger = Logger()

logger.info("This is an INFO level log entry")

```

5. The available log level methods are the same for the standard Python logging.Logger class.
6. It's possible to pass a ```logging.Logger``` instance in the constructor to use, for example, a Django logger. This
   feature is present just to standardize your source code.

### ```Encryption```

1. To use the ```encryption``` module to encrypt a text, use:

```
from dcd_py_util import encryption

encrypted_text: str = encryption.encrypt("plain text to encrypt")

```

2. To use the ```encryption``` module to encrypt a text and include the "Encrypted" label in front of it, use:

```
from dcd_py_util import encryption

encrypted_text_with_label: str = encryption.encrypt_with_label("plain text to encrypt")

```

3. To use the ```encryption``` module to decrypt an encrypted text, having the "Encrypted" label in front of it or not,
   use:

```
from dcd_py_util import encryption

plain_text_decrypted: str = encryption.decrypt("Encrypted <encrypted text>")

```
