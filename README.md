# Base_Converter

A base converter tool which supports different character sets.
 
Built for The Information Technology Syndicate.

## About
This tool was developed after the realization that there wasn't a single place we could go to convert to any arbitrary 
base from any other arbitrary base. Additionally, when converting bases sometimes it makes sense to use different 
character sets to represent the values in these bases thus the functionality for supporting different input and output 
bases were added.

## Current limitations
* Only single input values at a time
* Only non-negative bases supported
* Only pre-defined character sets supported

## Requirements
* Python3

## How to run
There are two ways to run this tool, both through the command line.<br>

Both options require you to download the tool.<br>

This can be done via:
```
git clone git@github.com:ProxesBoxes/Base_Converter.git
```
Or clicking the `Code->Download Zip` option on the top right. If the zip has been downloaded then extract the content 
before continuing.
<br><br>
Running the tool can be done via command line by navigating to the file location and entering `./Run_Base_converter.py` 
or `python3 Run_Base_converter.py`.

### Interactive Mode
To run the interactive mode simply execute the `Run_Base_Converter.py` with no parameter and follow the instructions 
provided via the CLI.

### Non-interactive Mode
To run the program through the terminal in an no-interactive mode / call by other scripts simply execute the program 
and at a minimum provide the required arguments.
#### Synopsis
```
Run_Base_Converter.py [-h] [-sb STARTING_BASE] [-sc STARTING_CHARACTER_SET]
                          [-ec ENDING_CHARACTER_SET]
                          starting_value ending_base
```

#### Options
##### Required
 ```
   starting_value
        The value to convert from

   ending_base
        The base in which the value is to be converted to
```
##### Optional
```
    -h, --help
        show the message and exit

   -sb, --starting_base
        The base in which the value to convert from, default to base 10

   -sc, --starting_character_set
        The character set to us for the input, by default a best attempt will be made at detecting the character based 
        off of the starting value

   -ec, --ending_character_set 
        The character set to us for the output, defaults to the same character set as the starting character set
```
### Example output
#### Example 1
Using the cli to convert 16 in base 10, standard character set, to base 8, standard character set
```
--------------------------------------------------
|                 Base Converter                 |
|                                                |
| Built for The Information Technology Syndicate |
--------------------------------------------------

Enter the starting base (default base 10): 10

Enter starting base value: 16

Select the starting base character set
  1 - standard
  2 - unicode
  3 - ascii
  Enter character set # (default 1): 1

Enter the ending base (default base 10): 8

Select the ending base character set
  1 - standard
  2 - unicode
  3 - ascii
  Enter character set # (default 1): 1

Converted Value: 20
```

#### Example 2
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 16, standard character set
```
./Run_Base_Converter.py 65 16
41
```

#### Example 3
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 256, standard ascii set
```
./Run_Base_Converter.py -ec ascii 65 256
A
```

#### Example 4
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 16, standard unicode set
```
./Run_Base_Converter.py -ec unicode 65 800
U+0000 U+0041
```

#### Example 5
Using the non-interactive mode to covert U+0041 in base 1337, unicode character set, to base 256, standard ascii set
```
./Run_Base_Converter.py -sb 1337 -sc unicode -ec ascii  U+0041 256
A
```

#### Example 6
Using the non-interactive mode to covert U+0041 in base 1337, utilizing the autodetection of the unicode character set, 
to base 256, standard ascii set
```
./Run_Base_Converter.py -sb 1337 -ec ascii U+0041 256
A
```

## Predefined Character Sets
| Character Set Name  | Characters in set |
| ------------- | ------------- |
| standard  | 0, 1, 2, 3, ..., 7, 8, 9, A, B, C, ..., X, Y, Z, :, ;, <, =, >, ?, @, a, b, c, ...  |
| unicode | U+0000, U+0001, U+0002, U+0003, ..., U+0009, U+00A, U+000B, ..., U+000F, U+0010, U+0011, ...  |
| ascii  | 'NUL', 'SOH', 'STX', 'ETX', ..., '!', '"', '#', ..., 'A', 'B', ... |

####ASCII Warning
Non-printable characters such as NUL, SOH, STX, etc may not be visible. If this is an issue submit a new issue and this 
will attempted to be address as soon as possible (likely just printing hex codes for non-printable characters).