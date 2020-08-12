# Base_Converter

A not so simple any longer base base converter tool by The Information Technology Syndicate.

##About
This tool was developed after the realization that there wasn't a single place we could go to convert to any arbitrary 
base from any other arbitrary base. Additionally, when converting bases sometimes it makes sense to use different 
character sets to represent the values in these bases thus the functionality for supporting different input and output 
bases were added.

##Current limitations
* Only single input values at a time
* Only non-negative bases supported
* Only pre-defined character sets supported

##Requirements
* Python3

##How to run
There are two ways to run this tool, both through the commandline.
###Interactive Mode
To run the interactive mode simply execute the `Run_Base_Converter.py` this can be done by navigating to the file 
location and entering `./Run_Base_converter.py`.

Follow the instructions provided via the CLI

###Non-interactive Mode
To run the program through the terminal in an no-interactive mode / call by other scripts simply execute the program 
and at a minimum provide the required arguments.
####Synopsis
`./Run_Base [Options...]`

####Options
#####Required
 ```
   -sb, --starting_base
        The base in which the value to convert from is

   -sv, --starting_value
        The value to convert from

   -eb, --ending_base
        The base in which the value to convert to is
```
#####Optional
```
   -sc, --starting_character_set
        The character set to us for the input, defaults to standard charset

   -ec, --ending_character_set 
        The character set to us for the output, defaults to standard charset
```

##Predefined Character Sets
| Character Set Name  | Characters in set |
| ------------- | ------------- |
| standard  | 0, 1, 2, 3, ..., 7, 8, 9, A, B, C, ..., X, Y, Z, :, ;, <, =, >, ?, @, a, b, c, ...  |
| unicode | U+0000, U+0001, U+0002, U+0003, ..., U+0009, U+00A, U+000B, ..., U+000F, U+0010, U+0011, ...  |
| ascii  | 'NUL', 'SOH', 'STX', 'ETX', ..., '!', '"', '#', ..., 'A', 'B', ... |

##Planned Future functionality
* Support for negative bases
* Support for multiple input and output values
* A better CLI interface