XOR encryption :

XOR (^) is a logical operation on bits.

Return True if 1 of his 2 operations is true
Return False if 2 of his operations are both false or true

bit A  |  bit B  |  A ^ B
   0   |    0    |    0
   0   |    1    |    1
   1   |    0    |    1
   1   |    1    |    0

Same code can encrypt and decrypt --> symetric encryption

Text ^ Key = Encrypt
Encrypt ^ Key = Text

(A ^ B) ^ B = A


Example :

'H' → ASCII 72 → bin 01001000
Clé = 20 → bin 00010100


01001000
XOR
00010100
---------
01011100  (92 in decimal)


To decrypt it :

01011100 XOR 00010100 = 01001000

01001000 --> 72 in dec --> 'H'


ord() --> char to ascii
chr() --> ascii to char