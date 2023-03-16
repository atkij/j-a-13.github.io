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
| `1` | `0` | `0` | `0` | `1` | `0` | `0` | `0` |

`-128 + 32 = -120`

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

## Computer Structure

### Von Neumann Architechture

In 1945, Von Neumann proposed a computer architecture consisting of 4 different parts:

 - CA - Central Arithmetic Logic Unit

 - CC - Central Control Unit

 - Memory

 - Input and Output channels

```
+-------------------+
|                   |
|  Backing Storage  |
|                   |
+-------------------+
     |    ^
     |    |
     v    |
+----------------------------------+
| +-------------+     +----------+ |
| |             |---->|          | |
| |  Processor  |     |  Memory  | |
| |             |<----|          | |
| +-------------+     +----------+ |
+----------------------------------+
     ^    |
     |    |
     |    v
+----------------------------+
|                            |
|  Input/Output Devices  |
|                            |
+----------------------------+
```

### Stored Program Concept

Von Neumann also came up with the Stored Program Concept.  This means that all instructions should be stored in binary inside memory.

### Fetch-Execute Cycle

The fetch=execute cycle is a series of steps that the processor follows to execute an instruction.

1. The memory address of the next instruction is placed on the address bus

2. The read line is activated

3. The instruction is transferred to the processor on the data bus

4. The instruction is then decoded and executed

### Memory Write Operation

To write data to memory the processor follows these steps.

1. Set up the MAR (Memory Address Register) with the address to be written to

2. Set up the MDR (Memory Data Register) with the data to be written

3. The address bus is then set up with the address to be written to from the MAR

4. The data is copied from the MDR to the data bus

5. The write control line is activated

6. Data on the data bus is then placed in the specified memory address

### Memory Read Operation

To read data from memory the processor follows these steps.

1. Place the address to be read from in the MAR (Memory Address Register)

2. The address bus is then set up with th address from the MAR

3. The read control line is activated

4. The data bus is set up with data to be read

5. The data from the data bus is then placed in the MDR (Memory Data Register)

6. Data is then decoded and executed

### The Processor

The processor is the main part of a computer.  It is the part that performs the instructions required for the computer to function.

```
+-------------------------------------+
|            The Processor            |
| +---------------------------------+ |
| |          Control Unit           | |
| +---------------------------------+ |
| +---------------------------------+ |
| | Arithmetic and Logic Unit (ALU) | |
| +---------------------------------+ |
| +---------------------------------+ |
| |            Registers            | |
| +---------------------------------+ |
+-------------------------------------+
```

#### Control Unit

The control unit controls the CPU and makes sure that instructions are fetched, decoded and executed in the correct order.

#### Aritmetic and Logic Unit

The ALU main job is arithmetic like addition subtraction, multiplication and division.  It also performs logic operations such as AND, OR, or NOT which may be used in programming (while loops, if statements).  The ALU also has a register called the Accumulator or, as Intel calls it, the EAX.  This is used to store the results of calculations.

#### Registers

The registers store small temporary pieces of data.  Because they are located inside the processor, they are very fast to access.  There are multiple different types of registers which all do different jobs.

| Register Name | Description |
|:--------------|:------------|
| Instruction Pointer | Holds the address in memory of the next instruction to be executed |
| Return Instruction Pointer | Holds the address in memory of the instruction to be executed after a called procedure is finished |
| Memory Address Register (MAR) | This is used to hold the address of the memory the processor next needs to access.  This is connected to the address bus |
| Memory Data Register (MDR) | This is used to hold the data read from or being written to memory.  This is connected to the data bus |

### Buses

Buses are wires that connect different parts of a processor and all have different jobs.

```
         +----------------------------------+
         |            Control Bus           |
         |                                  v
+-----------------+               +-------------------+
|                 |   Data Bus    |                   |
|                 |<------------->|                   |
|    Processor    |               |    Main Memory    |
|                 |  Address Bus  |                   |
|                 |-------------->|                   |
+-----------------+               +-------------------+
         |
         |                   +------------------------+
         |                   |                        |
         +------------------>|  Input/Output Devices  |
             Control Bus     |                        |
                             +------------------------+
```
#### Data Bus

The data bus carries data to and from the CPU and memory.  The data bus is bi-directional because the processor can read and write data in memory.

#### Address Bus

The address bus carries the address of the memory location to be read from or written to.  The address bus is uni-directional because only the processor can set a memory location - memory can't return one for the processor.

#### Control Bus

This bus doesn't carry any data.  Instead, it can send status signals to carry out different operations.  For example, the control bus connecting the memory can tell the memory to read data or write data.

| Control Line | Function |
|:-------------|:---------|
| Read | When active, tells the CPU is reading data from memory |
| Write | When active, tells the CPU is writing data to memory |
| Clock | This allows the processor to synchronise with another device |
| Reset | This tells the processor to reboot |

#### Bus Width

When a computer is referred to as 32 bit or 64 bit, this is actually the word length of the computer.  A word is the largest binary number that the processor can manipulate in one operation.

Changing the width of the data bus means that more or less data can be moved in one operation.  Increasing the width of the data bus should increase performance because less operations are required to move data.  Decreasing the bus width decreases performance as more operations are required to move data.

Increasing the width of the address bus allows more memory to be addressed as there are more addresses.  This doesn't affect performace because it will still require the same amount of operations to move memory.

### RAM

There are two main types of RAM (Random Access Memory).

 - Static RAM (SRAM)

 - Dynamic RAM (DRAM)

#### DRAM

Dynamic RAM is the main memory used in the computer and needs to be refreshed constantly.  DRAM is volatile, so if the computer is turned off, then the data in memory will be lost.  It is used more widely as it is less expensive than SRAM.

#### SRAM

Static RAM is usually reserved for cache memory as it is very fast, but also much more expensive, coming in smaller quantities.  Static RAM also does not need to be refreshed as reguarly as DRAM.  A processor can have different levels of cache memory where the lower the number the faster the memory.

### Factors Affecting Performance

There are 4 main factors that can affect the performance of a computer.

 - Number of processor cores

 - Clock speed

 - Width of the data bus

 - Cache memory

#### Number of Processor Cores

Processors can have multiple processor units (cores) inside the processor.  Each core can execute it's own individual programs.  

This means that multiple processes can be carried out concurrently, increasing performace as the processor can execute more than one instructino at a time.

#### Processor Clock Speed

The clock speed of computer, usually measured in hertz, determines how many operations can be carried out per second.  Most modern computers have a clock speed of greater than 2GHz.  This means that the processor can do 2,000,000,000 operations per second.  A single operation may require multiple instructions to be performed.

Increasing the clock speed increases performance because the computer can do the same instructions, but in less time than before.

#### Data Bus Width

Increasing the data bus width increases performace because data can be transferred to and from memory in less operations than was previously necessary.

#### Cache Memory

Increasing the cache memory increases the performance because more memory can be stored for faster access so less trips to memory are required.  Instructions like a loop will be stored in SRAM as they will be frequently accessed as they repeat.

## Enviornmental Impacts

Smart computer systems are being developed to help fight climate change.  Theses systems will help reduce toxic emissions and use of electricity or gas.

### Smart Heating Systems

Smart heating systems help control the heating and turn it off when it's not needed.

 - Activity sensors help the system learn when you want the heating to be on or off

 - Activity sensors also help adjust the heating in rooms if there's unusual activity in the house - perhaps if you're off work one day

 - The system can also read the weather forecast to adjust the heating in advance to warm up or cool down the house

 - Remote control apps allow you to control the heating system remotely so you can turn it on and off when you're not at home

Because the system can automatically turn the heating off when you're not at home, this has a positive impact on the enviornment because energy isn't being to used to unecessarily heat the house.

### Traffic Control Systems

Traffic control systems help manage the traffic in a city to reduce waiting times and impact on the enviornment.

 - Adaptive traffic signals adjust timngs of their green light cycles to match the current amount of traffic.  They continuously collect data about the approaching vehicles to adjust their timings

 - Intelligent routing systems share data about different areas - like slow areas, traffic jams and road closures - and helps reduce traffic jams because of incidents, reducing toxic emissions as cars don't have to wait.

This has a positive impact on the enviornment because it reduces waiting time in queues for cars so less energy is wasted.

### Car Management Systems

Car management systems help to reduce toxic emissions from cars by smartly controlling the car.

 - Start-stop systems turn the engine off when waiting at lights or in queues, reducing fuel consumption and emissions.

 - Engine control units (ECU's) use sensors to alter the engine's air to fuel ratio to optimise fuel consumption, hence reducing carbon dioxide emissions.

## Security Risks and Precautions

### Computer Misuse Act

In 1985 two hackers gained access to the email of Prince Phillip.  Back then there were no laws preventing people from hacking andd the hackers were found not guilty after appealing.  The Computer Misuse Act was then introduced in 1990 because of this incident and made the following a criminal offence.

1. Unauthorised access to computer material

	Gaining access to a computer without permission - up to 12 months prison or a £5,000 fine.

2. Unauthorised access with intent to commit or facilitate commission of further offences

	Helping to commit a crime by gaining unaithorised access to a computer - up to 10 years prison or a fine.

3. Unauthorised acts with intent to impair, or with recklessness as to impairing, operation of computer, etc

	Modification of data on a computer system without permission - planting viruses, deleting or modifying user's files.

### Tracking Cookies

Tracking cookies are a type of cookie which are used to identify users.  If the cookie exists, then customized websites can sometimes be made as the user can be identified as the cookie is sent to the webserver whenever you go to visit that site.

Tracking cookies may not seem important, but they do allow personal information to stored and exchanged between different websites to provide targetted advertisements to get you to buy stuff.

### DOS Attacks

A Denial of Service (DOS) attack is when an attempt to bring an online service/website offline by flooding the server so it can't do anything else.

#### Symptons of a DOS Attack

 - The server may have very poor performance

 - Users may be unable to access it

 - The server may crash

#### Effects of a DOS Attack

A Denial of Service attack will cause a lot of disruption to a company in many different ways.

 - Customers may not be able to access the company's website

 - Employees may be unable to work as the servers will be down

 - Depending on how long the servers are offline, the company could lose out on a lot of business

#### Costs of a DOS Attack

There will be some costs with a Denial of Service attack depending on the size and length.

 - Lost revenue due to downtime

 - Determining the nature of the attack

 - The payment for specialists to repair the servers after the attack

 - Payment for cyber securtiy experts to iplement safeguards to prevent further attacks

 - Additional admin to compensate for loss of network services

#### Types of DOS Attacks

There are many different types of Denial of Service attacks that attack the server in different ways.

 - Physical Attacks:

	A physical attack is when you physically cut the wires to a server or damage it so it can't function.  Physical attacks can also be performed by attacking other parts of a server infrastructure such as network routing.

 - Bandwidth Consumption:

	This is probably the most common type of Denial of Service attack and is where the attacker floods the server with requests and packets of information to use up all the available band width so no other data can be sent to and from the server.

 - Resource Starvation:

	Because a server doesn't have unlimited resources, the attacker will try to use up all the processing time, memory, and storage by continuously creating new accounts or spamming an email server so it uses up all it's space to store emails.  This will cause the server to stop functioning properly as it can't store anymore data or process anything else.

 - DNS Attack:

	Whenever a url is entered into a web browser, the browser makes a request to a DNS server (Domain Name Service) to find out the IP address of that website.  If an attacker was to attack a DNS server then the browser wouldn't be able to find out the company's IP address, so the users would be unable to visit their website.  An attacker may want to hack the DNS server to replace the IP address of the company's server with their own IP address to re-route all network requests to the company's server to their own.

#### Reasons of a DNS Attack

 - Financial - blackmail, competitive (disrupting business competition), hired to hack the server

 - Political - you don't agree with the other's side's views

 - Personal - you hold a grudge against a former employee, etc

#### Distrobuted DOS

A Distributed Denial of Service is when the attacker uses a network of computers sometimes known as a botnet or a zombie army.  The users of the computers participating in the attack may be unaware that they have a virus helping a DDOS attack. 

### Encryption

Encryption is when data is transformed into another form so that it is unreadable.  Data must be encrypted and decrypted with a key.

#### Symmetric Encryption

Symmetric encryption is when both parties have the same secret key and that key is used to both encrypt and decrypt the data.

| Advantages | Disadvantages |
|:-----------|:--------------|
| The key doesn't have to be sent with a message | The key has to be known by the receiver before transission |
| The system is simpler and faster | If the key is compromised, then intercepted messages can be decyphered |

#### Asymmetric Encryption

Asymmetric encryption is where two keys exist.  The public key and the private key.  The public key can only decrypt messages sent by the private key and the private key can only decrypt messages sent by the public key because both keys are linked mathematically using very large prime numbers.

```
+----------+
|          |
|  Sender  |
|          |
+----------+
    |
    | Plain text
    v
+------------+    +------------+
| Encryption |<---| Public Key |
+------------+    +------------+
    |
    | Cipher text
    v
+------------+    +-------------+
| Decryption |<---| Private Key |
+------------+    +-------------+
    |
    | Plain text
    v
+------------+
|            |
|  Receiver  |
|            |
+------------+
```

The public key is made publicly available to everyone while the private key is kept secret by the receiver.  This means everyone can send secret messages to the receiver while not being able to decrypt each other's messages.

| Advantages | Disadvantages |
|:-----------|:--------------|
| The private key never needs to be distributed | Is slower than symmetric encryption |
| Can be used to implement digital signitures | It requires far more processing power to encrypt and decrypt the content of the message |

### Digital Certificates

A digital certificate is the digital equivalent of a passport or a driving license - they are used to prove that it's really you.  Digital certificates are issued by a certification authority and contain the following information:

 - Public key

 - Owner's name

 - Expiration date and issuer

### Digital Signatures

A digital signature is a method of proving that a message has not been modified during transit.

#### Sending a Signature

1. You obtain a message hash (a unique mathematical summary of the message)

2. You encrypt the message hash with your private key

3. This signature is then attached to the message

#### Receiving a Signature

1. You hash the received message

2. You decrypt the sent message hash

3. You then compare both the message hashes and if they are the same, then the message is authentic

```
+----------+
|          |
|  Sender  |
|          |
+----------+

+------------+
|            |
|  Document  |
|            |
+------------+
    |
    |    +----------------+
    |--->| Hash algorithm |---+
    |    +----------------+   |
    |                         v
    |                   +------------+    +-------------+
    |<------------------| Encryption |<---| Private key |
    |                   +------------+    +-------------+
    |
    |
    |-----------------------+
    |                       |
    |                       v
+----------------+    +------------+    +------------+
| Hash algorithm |    | Decryption |<---| Public key |
+----------------+    +------------+    +------------+
    |                       | 
    |                       |
    v                       v
+---------------------------------+
|                                 |
|  If both hash's are equal then  |
|    the document is authentic    |
|                                 |
+---------------------------------+
+------------+
|            |
|  Receiver  |
|            |
+------------+
```
