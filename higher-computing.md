% Higher Computing
% Joel Atkinson
%

# Computer Systems

## Data Representation

### Two's Complement

The two's complement system is a method used by the computer for storing negative binary numbers.

#### Decimal to Binary

To create the binary of -120 there are 3 steps

1. Convert the positive number into binary

	`0111 1000 (120)`

2. Invert all the bits (0's to 1's and 1's to 0's)

	`1000 0111`

3. Add 1 to the right of the number (Least Significant Bit)

	```
	 1000 0111
	+0000 0001
	=1000 1000
	```

#### Binary to Decimal

To convert a two's complement number from binary to decimal simply write out the column headers except with the most significant bit as negative then add up the numbers with a 1.

| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

-128 + 32 = -120

#### Min and Max Limits

To calculate the maximum number that can be stored using the two's complement system, use the following formula:
(2^n-1^)-1
And to calculate the minimum:
-2^n-1^

### Floating Point Representation

#### Binary fractions

To store binary fractions we simply add extra column headers by dividing by 2 after the decimal point.

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 | . | 0.5 | 0.25 | 0.125 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2^7^ | 2^6^ | 2^5^ | 2^4^ | 2^3^ | 2^2^ | 2^1^ | 2^0^ | . | 2^-1^ | 2^-2^ | 2^-3^ |


To convert a fixed point binary to decimal, we just add up the column headers as before.

Because the coputer can't store decimal points in binary, we have to use floating point representation to store real numbers.

#### Storing Floating Point Numbers

A floating point number is split up into 3 parts - the sign, the mantissa and the exponent.  The sign determines whether it is a negative number or not (1 for a negative and 0 for positive just as in two's complement).  The mantissa is the whole number without the decimal point.  This is left-aligned and padded with 0's.  The exponent is used to tell the computer the position of the decimal point in the mantissa.  This right aligned and padded with 0's at the start.

| | Sign | Mantissa | Exponent |
|:-:|:-:|:-:|:-:|
| 24 bits = | 1 bit | 15 bits | 8 bits |
| 32 bits = | 1 bit | 23 bits | 8 bits |
| 64 bits = | 1 bit | 52 bits | 11 bits |

#### Converting Real Numbers to Fixed Point Binary

To convert a real number like 250.03125 to fixed point binary you must:

1. Convert the first part of the number into binary (before the decimal point)

	```
	250.03125
	250 = 1111 1010
	```

2. Convert the second part of the number into binary by multiplying until it equals 1

	```
	0.03125 * 2 = 0r0.0625  |
	0.0625  * 2 = 0r0.125   |
	0.125   * 2 = 0r0.25    |
	0.25    * 2 = 0r0.5     |
	0.5     * 2 = 1r0       v  = 0.00001
	```

3. Now join the two parts together to get:

	`11111010.00001`

#### Converting Fixed Point Binary to Floating Point

We start with a fixed point binary number such as 11.001011 to convert to 24 bit floating point representation:

1. We first move the decimal out of the number to the left and pad to the left to form the mantissa

	```
	11.001011
	⤾⤾
	110010110000000
	```

2. We then convert the number of spaces the decimal point moved to form the exponent

	It moved 2 spaces so the exponent is `00000010`

3. We then choose the sign and fill out the table

	| Sign | Mantissa | Exponent |
	|:-:|:-:|:-:|
	| `0` | `110010110000000` | `00000010` |

If the number is a small number (below 0) then the decimal point must be moved to the left so that it is in front of the first 1.  Because the decimal point has been moved the opposite direction, then it will be a negative number and must be stored using the two's complement system.

#### Bit Allocation

The higher the number of bits stored in the mantissa, the higher the precision of the number.  The more numbers after the decimal point, the greater the precision.

Increasing the exponent increases the range of numbers that can be stored as the decimal point can be moved more places to the right and left.

Single precision is a 32 bit floating point number (1 bit sign, 23 bits mantissa, 8 bits exponent) and double precision is  64 bits (1 bit sign, 52 bits mantissa, 11 bits exponent).

### Storing Text

#### ASCII

ASCII is a method of storing text digitally.  Each letter on a keyboard has it's own ASCII code which was originally stored with 7 bits but was increased to 8 bits to store more characters for more languages and symbols (known as extended ASCII).  ASCII stands for the American Standard Code for Information Interchange.

The first 32 codes are known as control codes which cannot be printed such as backspace, delete and escape.

A character set is the term for a certain way of storing text on a computer.  There are lots of different character sets for different languages.  ASCII is one character set and Unicode is another.

#### Unicode

The problem with ASCII is that there wasn't enough space to store every letter of every language's alphabet.  Unicode was invented to fix this by using more bits so it could store more letters and symbols.

Unicode is known as UTF-8, UTF-16 and UTF-32, storing 8, 16, 32 bits for each character.

The first 128 values of Unicode are the same as ASCII and then goes up to 137,439 characters!

### Graphics

#### Vector Graphics

| Advantages | Disadvantages |
|:-----------|:--------------|
| Do not lose quality when scaled | Cannot be edited at pixel level |
| Require less storage space | Cannot show photo realistic scenes easily |
| Objects are easily moved/manipulated | Will usually require special applications to open |
| Resolution independent | |

#### Bitmapped Graphics

| Advantages | Disadvantages |
|:-----------|:--------------|
| Can edit down to the individual pixel | Have a very large file size as every pixel is stored |
| Adding extra detail to the pixture does no increase the file size | When scaled larger, pictures pizelate as they are resolution dependent |
| Can create photo realistic images | |


