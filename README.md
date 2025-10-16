Module 8:

Secret Scanner Final Project

A small Python tool that scans for hardcoded secrets like API keys, passwords, tokens, and private keys within file or directories.

Features

Scans a file or directory.
Detects common secret patterns with regex
Shows filename, line number, and match
Optional File Explorer picker (Windows\Tkinter)
Shows results on Terminal.

Detection Logic

When scanning a directory it selects a file. If no file is found or cannot read the file, it will stop the program. If a file is found it will iterate through each line and compare it to the PATTERNS values which are the regexes. If it finds any matches it will display the secrets found on the Terminal. If nothing is found it will display that as well and stop the tool.

Example patterns include:

Secret Type	Example Regex
AWS Access Key	`(AKIA
Google API Key	AIza[0-9A-Za-z\-_]{35}
Slack Token	xox[baprs]-[0-9a-zA-Z]{10,48}
Private Key	`-----BEGIN (RSA
Generic Password	`(?i)(password

Scanning is offline and local.

More regexes can be added in the PATTERNS dictionary if needed.

Usage

# Launch File Explorer to pick a path (Easiest method)
python secret_scanner.py

# Scan a directory
python secret_scanner.py ./project

# Scan a single file (if in a different directory, paste the path)
python secret_scanner.py config.py


Testing

There is a test_file to test results, ensure to replace some of the values with fake ones to try out. 
Naviagate and select those files to see the results.

Notes

Never include real credentials in tests!

Module 5:

## 1. 
Flaw: 
This is an Insecure Direct Object Reference (IDOR) or broken access control issue. The endpoint returns a user object purely based on a user identifier (userid) without verifying the requester’s identity or privileges. There is no verification for whether the requester is the owner of that or an authorized role.

Fixes implemented:
Added authentication check (req.user.id).
Only allow access if the user is requesting their own profile or is an admin.
 
## 2. 
Flaw:
Similar to the 1st code vulnerability, the route returns account data based solely on the useridd path parameter. It does not contain any authentication/authorization checks and also returns sensitive fields, which significantly enlarges the damage. In short, any user could potentially gather any users information.

Fixed implementation:
Check added to ensure the logged in user can only request the information from their own user.
Removed sensitive info attached to the request.

## 3. 
Flaw: 
The code presented in the example uses MD5, an outdated hashing method especially for passwords. The implementation shown also does not have any salt capability.

Fixed implementation:
The new code switches to Python with bcrypt, which automatically generates salts for each password and deliberately runs more slowly to make brute-force attacks far less effective.

## 4.
Flaw:
The flaw are similar to the previous exmaple, except is uses SHA1 for password hashing. Also an insecure password hashing method. It suffers from the same outddated issues as the MD5.

Fixed implementation:
The implementations in this are also the same as in 4 where it uses bcrypt. 

## 5.
Flaw:
The query string has the username variable which can contain any string. Meaning that attackers can implement malicious SQL into the the query.

Fixed implementation:
The query gerts turned into a prepares statement. Which allows the username variable to just be data and not SQL, so chaarcters outisde of that wont get recognized.

## 6. 
Flaw:
The query accepts username directly as a parameter without affirming whether it is safe or not. This could lead to malicious strings being insterted as a parameter.

Fixed implementation:
If statament added to ensure the username is of valid type and characters.
Return errors if it cannot find the username.

## 7.
Flaw:
The function does not contain lines with authentication of the user and the email, thus could lead to anyone who knows the email can reset thew password. Moreover, the password is stored in plaintext and without hashing. 

Fixed implementation:
Added token implementation to limit password resetting. Password hashing implemented using bcrypt library.


## 8. 
Flaw:
The original does not use a integrity value which means the contents have a  possibility of being tampered. In summary, without integrity it cannot safely verify that the contents are not tampered.

Fixed implementation:
Integrity resource value added, although it changes depending on CDN that provides it.

## 9.
Flaw:
The url line accepts any url that is inputted which can make requests to any link potentially not safe urls.

Fixed implementation:
The fix added validates the url scheme, blocks private or local addresses, and sets a timeout to prevent the program from hanging.

## 10
Flaw:
It is implied that the password entered is compared to a password presumably pulled from a database in plaintext. Therefore, making the storage of passords unsafe and vulenrable to attacks. 


Fixed implementation:
Ensured that the passworeds are stored in a hashed format with salt. Also ensured that thew if statement checks for the hash of the password.


Module 4:

# Simple Text Processing with Encryoiton/Decryption

## Video Explanation of Script
https://drive.google.com/file/d/1batpowPo6DKzX-yphIGyB3kMgTyD5fCg/view?usp=sharing 

(Only IvyTech Members are able to view)


## Overview
1. Accepts user input (as a string).
2. Hashes the input using SHA-256.
3. Encrypts the input using AES-256 , a symmetric method.
4. Decrypts the ciphertext back into plaintext.
5. Verifies the decrypted content against the original via SHA-256 hash comparison.

---

## Security Principles

### Confidentiality
The message is encrypted using **AES-256 in CBC mode**. Only someone with the secret key and IV can decrypt the ciphertext.

### Integrity
Integrity is enforced by hashing both the original and decrypted messages using **SHA-256**. The hashes matching will prove the message is intact and unalrtered. 
### Availability
The system guarantees that as long as the AES key and IV are securely stored, the encrypted data can always be decrypted. The use of symmetric encryption ensures the solution is lightweight and efficient, maintaining availability.

---

## Entropy and Key Generation
- AES Key and IVs are generated using `os.urandom()`, which provides **cryptographically secure random numbers** from the operating system.
- High entropy ensures unpredictability, preventing attackers from guessing or brute-forcing.
- Each run produces new keys and IVs, making ciphertexts unique even for identical messages.

---

## Requirements
- Python 3
- [cryptography](https://cryptography.io/en/latest/) library

## Install dependencies:
- pip install cryptography

Module 3:

This assignment was to create different different demonstrations of encryption such as SHA256, Caeser Cipher and show the process for digital signing. The app works by accepting an input message form the user and a shift as an integer for the Caeser cipher. After inputting valid information, it will use the message to create a hash and also encrypt it using the cipher. Afterwards, it will carry out the digital signing process also using the message inputted.

The SHA256 hash process is done using the hashlib library where I directly used the SHA256 function to encode the text into a hash. The hash can be the same if the same two strings are inputted. The Caeser cipher was coded using the method in the learning materials, so it follows the method of inputting a messagea and a shift as an integer. Together with the constants they create a range of characters that the letters can shift towards. In this case, the shift can also be used to reverse the process and decode the cipher. FOr the Digital signing, we use the cryptography library to create keys (public and private) and sign them. The input message creates a signature, which can later be verified using the corresponding public key.

Module 2:

The code provides two methods of cryptography: Symmetric and Assymetric. 

For the Symmetric method, I will be using the AES algorithm with the CBC (Code Block Chaining) mode. We begin by creating the AES key and Initialization vector which are required to encode and need to be random. Then we make a message, in this case "symmetric message" making sure we use the "b" prefix to have it as a byte object since we cannot use the standard string. AFter this, we create a cipher using the AES Key and IV using the CBC mode as mentioned. An important step here is to ensure that we pad the plain text since AES method only works with 16 byte blocks of data. Finally, we encypt the padded message and then decode it by doing the reverse of the steps. We use the same key and iv to create the decryptor and then decrypt the message.

Now with the Asymmetric method, we will be using the RSA encryption method. Similarly to before, we start creating the keys needed so a Public and Private RSA Key. We make these readabale by using the PEM format which creates headers and footers in the text and allows. Once again we create a message in plain text, once again using the "b" prefix. Then we encrypt the text with padding here as well, this time we use the SHA256 padding method and the public key. Then we reverse, by decrypting the ciphertext and using the same padding method. The difference here is that we use the private key that was created earlier.



Module 1:

CIA is a shorthand in software development, that stands for Confidentiality, Integrity and Availability. This triad shows the three fundamentals in securing software and data.
Confidentiality has to do with ensuring authorization and authentication measures are in place so the correct parties are accessing the correct data and functions of software. Integrity makes sure that data is handles properly and safely without changing or damaging the "contents", or integrity as the name suggests, of the data. Availability is about the uptime of systems and how accesible it is at any given time, depending on the kind of software this can vary.   

For my application, the most present application of these concepts is Confidentaility as that is the only principle that is being tested for this application. When using the application I have tested to ensure that "admin" and "user" can only access their own functions and neither can access the other roles' functions. INtegrity and Availability cannot be measured in this example since they are not applicable.