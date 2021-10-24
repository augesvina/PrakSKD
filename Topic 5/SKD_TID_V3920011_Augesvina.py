#!/usr/bin/env python
# coding: utf-8

# In[2]:


#membuat fungsi affine cipher 
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
 
 
#membuat fungsi enkripsi dari affine cipher
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 #membuat fungsi dekripsi mengembalikan ke plaintext
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 # kode driver untuk menguji fungsi diatas
def main():
    # mendeklarasikan text dan key
    text = 'AUGESVINA SEIYUSANDA LESTARI'
    key = [7, 2]
    
    print('Plaintext : {}'.format(text))
    print('Kunci : {}'.format(key))
 
    # memanggil fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    # memanggil fungsi dekripsi
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
    main()


# In[ ]:




