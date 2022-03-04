#  File: Cipher.py
#  Description: code and decode strings
#  Student's Name: Michael Walter
#  Student's UT EID: MJW3895
#  Course Name: CS 303E 
#  Unique Number: 50180
#  Date Created: 4/16/20
#  Date Last Modified:4/16/20

def encode(plaintext,key):
            a = ""
            s = "abcdefghijklmnopqrstuvwxyz"
            sentence = ""
            for i in range(0,len(plaintext)):
                    a = plaintext[i]
                    str1 = " " 
                    #print(pt)
                    for x in range(0,len(key)):
                            if a == s[x]:
                                    sentence += key[x]
                            if a.isupper()== True and a.lower() == s[x]:
                                    sentence += key[x].upper()
                    if a.isalpha()== False:
                            sentence += a
            return sentence
def decode(ciphertext, key):
            a = ""
            s = "abcdefghijklmnopqrstuvwxyz"
            sentence = ""
            for i in range(0,len(ciphertext)):
                    a = ciphertext[i]
                    for x in range(0,len(key)):
                            if a == key[x]:
                                    sentence += s[x]
                            if a.isupper()== True and a.lower() == key[x]:
                                    sentence += s[x].upper()
                    if a.isalpha()== False:
                            sentence += a
            return sentence

def main():
    plaintextMessages = [
    ["This is the plaintext message.",
     "bcdefghijklmnopqrstuvwxyza"],
    ["Let the Wookiee win!",
     "epqomxuagrdwkhnftjizlcbvys"],
    ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
     "hnftjizlcbvysepqomxuagrdwk"],
    ["I used to think I was indecisive, but now I'm not too sure.",
     "mqncdaigyhkxflujzervptobws"],
    ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
     "bludcmhojaifxrkzenpsgqtywv"] ]

    codedMessages = [
    ["Uijt jt uif dpefe nfttbhf.",
     "bcdefghijklmnopqrstuvwxyza"],
    ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
     "epqomxuagrdwkhnftjizlcbvys"],
    ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
     "hnftjizlcbvysepqomxuagrdwk"],
    ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
     "mqncdaigyhkxflujzervptobws"] ]




    first = plaintextMessages[0]
    second = plaintextMessages[1]
    third = plaintextMessages[2]
    fourth = plaintextMessages[3]
    fifth = plaintextMessages[4]
    ciphertext1 = encode(first[0],first[1])
    ciphertext2 = encode(second[0],second[1])
    ciphertext3 = encode(third[0],third[1])
    ciphertext4 = encode(fourth[0],fourth[1])
    ciphertext5 = encode(fifth[0],fifth[1])
    firstcoded = codedMessages[0]
    secondcoded = codedMessages[1]
    thirdcoded = codedMessages[2]
    fourthcoded = codedMessages[3]
    codetext1 = decode(firstcoded[0],firstcoded[1])
    codetext2 = decode(secondcoded[0],secondcoded[1])
    codetext3 = decode(thirdcoded[0],thirdcoded[1])
    codetext4 = decode(fourthcoded[0],fourthcoded[1])
    print("plaintext:	",first[0])
    print("encoded: 	",ciphertext1)
    print("re-decoded:	",decode(ciphertext1,first[1]))
    print("\n"*3)
    print("plaintext:	",second[0])
    print("encoded: 	",ciphertext2)
    print("re-decoded:	",decode(ciphertext2,second[1]))
    print("\n"*3)
    print("plaintext:	",third[0])
    print("encoded: 	",ciphertext3)
    print("re-decoded:	",decode(ciphertext3,third[1]))
    print("\n"*3)
    print("plaintext:	",fourth[0])
    print("encoded:		",ciphertext4)
    print("re-decoded:	",decode(ciphertext4,fourth[1]))
    print("\n"*3)
    print("plaintext:	",fifth[0])
    print("encoded: 	",ciphertext5)
    print("re-decoded:	",decode(ciphertext5,fifth[1]))
    print("\n"*3)
    print("encoded:		",firstcoded[0])
    print("decoded:		",codetext1)
    print("\n"*3)
    print("encoded:		",secondcoded[0])
    print("decoded:		",codetext2)
    print("\n"*3)
    print("encoded:		",thirdcoded[0])
    print("decoded:		",codetext3)
    print("\n"*3)
    print("encoded:		",fourthcoded[0])
    print("decoded:		",codetext4)


main()
