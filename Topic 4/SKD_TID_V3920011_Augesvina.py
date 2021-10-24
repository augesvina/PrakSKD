#!/usr/bin/env python
# coding: utf-8

# In[1]:


# membuat key untuk enkripsi huruf kecil dan besar
hurufKecil = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25, '':26 }

# membuat fungsi variabel huruf baru
def huruf_baru(letter):
    hurufKapital = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3,
'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8,
'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12,
'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16,
'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21,
'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25, '':26
}

    pos = hurufKapital[letter] #pos untuk mengambil data variabel hurufKapital
    return pos

def persegeran_huruf(letter, rot): # membuat perintah pergeseran huruf untuk index enkripsi
    menggeser = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - menggeser) % 26 + menggeser)

# membuat fungsi enkripsi yang menggabungkan huruf baru dengan enkripsi
def enkripsi(text, key):
    vigenere = []    
    starting_index = 0 # dimulai dari index 0
    for letter in text:
        putaran = huruf_baru(key[starting_index])
        if not letter in hurufKecil:
            vigenere.append(letter)
        elif letter.isalpha():            
            vigenere.append(persegeran_huruf(letter, putaran))             

        if starting_index == (len(key) - 1):
            starting_index = 0
        else: 
            starting_index += 1

    return ''.join(vigenere)

text = input("Masukkan nama: ") #input untuk memasukan teks
key = input("Masukkan kunci: ") #input kunci

print("Enkripsi : " + enkripsi(text, key)) # mengambil nilai dari text dan key untuk di enkripsi
print ("Deskripsi : " + text) # menampilkan hasil text dekripsi


# In[ ]:




