Utilizare script-uri

encrypt : python encrypt.py parola input.txt output
decrypt : python decrypt.py parola output input_recuperat.txt
getpass ( input.txt + output ): python getpass.py input.txt output pass.txt
getpass2 ( output ): python getpass2.py output pass_output.txt

Problema 1 ( input.txt + output )

Este suficient sa rulam getpass.py cu argumentele cerute.
Script-ul citeste 30 de caractere din input.txt si output si face xor litera cu litera.
Pentru a afla parola, luam primele doua secvente alaturate de la inceput, de forma parola[0:x] si parola[x:2x] (x = range(10, 16))
Daca sunt egale, am aflat parola de lungime x.

Problema 2 ( output )

Script-ul getpass2.py se bazeaza pe ideea ca input.txt contine un text in limba romana, fiind prezente cifre si diferite simboluri.
De asemenea, stim ca parola este formata doar din litere si cifre.

Se fac 2 array-uri, passChars si characters. Primul contine litere si cifre, al doilea contine litere, caractere albe,
paranteze, ghilimele, linie de dialog, plus, egal etc.

Ne folosim de itertools, mai exact itertools.product, care face produsul cartezian cu elementele dintr-un array, de lungime repeat = x.
Variabila passW se initializeaza cu fiecare rezultat al acestui produs cartezian ( echivalentul unui for in for in for etc. ).
Citim 10000 de caractere din output ( sunt destule pentru ce avem nevoie ) si facem operatia xor, la fel ca la problema 1.

Daca noul caracter, care se gaseste acum in newChar, nu se afla in array-ul characters, atunci parola nu este corecta si trecem la urmatoarea.
De fiecare data, citim fisierul output de la inceput.

Daca toate cele 10000 de noi caractere se afla in characters, atunci putem spune ca am gasit parola. Aceasta este afisata atat in consola, cat si in fisierul pass_output.txt.
