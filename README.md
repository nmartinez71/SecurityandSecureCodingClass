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