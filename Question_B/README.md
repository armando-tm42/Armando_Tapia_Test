# To numeric lib
This library deals with converting and comparing decimals and integers present in a string.

## Installaition
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install to_numeric_lib.

```bash
pip install dist\to_numeric_lib-0.0.1-py3-none-any.whl
```

## Usage
Regular expressions are the main base of to_numeric lib, so Deci and Enti objects are able to  receive all kinds of character and work as long as there is at least one number in the string, these objects will identify whether there is a Decimal or an Integer in a string thanks to the use of predifined patterns that recognoize the structure of these numbers.

```python
from to_numeric_lib import Deci, Inte

number_1 = Deci('122312.34saf45')
number_2 = Inte('4534jkj123')
```
Both objects have a clean attribute that discards all the unwanted characters, then these transform and give format to the numbers presented in the string.
```python
number_1 = Deci('122312.34saf45')
number_2 = Inte('4534jkj123')

print(number_1.clean,' ',number_2.clean)
#output
>>>"122312.3445   4534123"
```
If we want to convert the string to a format that we can use, the functions to_int() and to_float() from Inte and Deci objects respectively, return the numerical representation of the numbers present in a string. These methods use an algorithm that multiplies each number by its corresponding power of ten, then each "part" is added up to have the whole number.

```python
number_1 = Deci('122312.34saf45')
number_2 = Inte('4534jkj123')

print(type(number_1.to_float()),' ',number_1.to_float(),' ',type(number_2.to_int()),' ',number_2.to_int())
#output
>>><class 'float'>   122312.3445   <class 'int'>   4534123
```
to_numeric_lib has a function to compare whether an Inte or a Deci object is equal, less or greater than other objects or Strings.

```python
Integer_1 = Inte('4534jkj123')
Integer_2 = Inte('1321s3')
Deci_1 = Deci('1.23213safd')

# comp method compares objects of the same type
Integer_1.comp(Integer_2)
print('\n')
'''
compD method compares an Inte object with a Deci object,
Deci objects have a compI method that works in the same way
but with Inte objects.
'''
Integer_1.compD(Deci_1)
print('\n')
# comps compares an object with a string
Integer_1.comps('4635345asdsad')

#output
>>>"4534123  is greater than  13213"


>>>"4534123  is greater than  1.23213"


>>>"4534123  is less than  4635345"
```
## missing functionalities
Like the dot, comma is accepted as decimal point so in new releases this function will be added.

Thousand separators are another way to represent large numbers, each country has its own rules for thousand separators and decimal separators so this functionality could be added in the future.

Please make sure to update tests as appropriate.

## License
to define
