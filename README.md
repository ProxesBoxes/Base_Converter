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
There are two ways to run this tool, both through the commandline.<br>

Both potions require you to download the tool.<br>

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
`./Run_Base [Options...]`

#### Options
##### Required
 ```
   -sb, --starting_base
        The base in which the value to convert from is

   -sv, --starting_value
        The value to convert from

   -eb, --ending_base
        The base in which the value to convert to is
```
##### Optional
```
   -sc, --starting_character_set
        The character set to us for the input, defaults to standard charset

   -ec, --ending_character_set 
        The character set to us for the output, defaults to standard charset
```
### Example output
#### Example 1
Using the cli to convert 16 in base 10, standard character set, to base 8, standard character set
```shell script
base converter
select starting base:
  2 standard_binary
  8 standard_base_8
  10 standard_base_10
  16 standard_hex
  32 standard_base_32
  Or simply enter the base value you want and we'll try our best
  enter # choice:
10
enter starting base character set:
  1 - standard (default)
  2 - unicode
  3 - ascii
1
enter starting base value: 
16
select ending base:
  2 standard_binary
  8 standard_base_8
  10 standard_base_10
  16 standard_hex
  32 standard_base_32
  Or simply enter the base value you want and we'll try our best
  enter # choice:
8 
enter ending base character set: 
  1 - standard (default)
  2 - unicode
  3 - ascii
1
Ending Value: 
20
```

#### Example 2
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 16, standard character set
```shell script
./Run_Base_Converter.py -sb 10 -sv 65 -eb 16
41
```

#### Example 3
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 256, standard ascii set
```shell script
./Run_Base_Converter.py -sb 10 -sv 65 -eb 256 -ec ascii
A
```

#### Example 4
Using the non-interactive mode to covert 65 in base 10, standard character set, to base 16, standard unicode set
```shell script
./Run_Base_Converter.py -sb 10 -sv 65 -eb 800 -ec unicode
U+0000 U+0041
```

## Predefined Character Sets
| Character Set Name  | Characters in set |
| ------------- | ------------- |
| standard  | 0, 1, 2, 3, ..., 7, 8, 9, A, B, C, ..., X, Y, Z, :, ;, <, =, >, ?, @, a, b, c, ...  |
| unicode | U+0000, U+0001, U+0002, U+0003, ..., U+0009, U+00A, U+000B, ..., U+000F, U+0010, U+0011, ...  |
| ascii  | 'NUL', 'SOH', 'STX', 'ETX', ..., '!', '"', '#', ..., 'A', 'B', ... |

## Planned Future functionality
* Support for negative bases
* Support for multiple input and output values
* A better CLI interface