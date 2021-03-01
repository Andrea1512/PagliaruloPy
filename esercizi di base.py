nome = input("nome")

print("ciao", nome)

2)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (nome , cognome)

3)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (len(nome), len(cognome))

4)
x = input("Inserisci il primo numero: ")
y = input("Inserisci il secondo numero: ")

if x > y: print (x , y)
else: print (y, x)

5)
colore = input("Inserisci il tuo colore preferito: ")
if colore == "rosso" or colore == "ROSSO" or colore == "Rosso": print("Bello")
else: print("Non mi piace")

6)
nome = input("Inserisci il tuo nome: ")
c=0
while(c<3): 
  print(nome)
  c+=1

7)
nome = input("Inserisci il tuo nome: ")

for x in nome:
  print(x)

8)
frutta = ("Banana", "Mela", "Ananas", "Fragola")
print(frutta[2])

9)
frutta = ("Banana", "Mela", "Ananas", "Fragola")
print(frutta)
scelta = input("Scegli uno di questi quattro: ")
if scelta == "Banana": 
  print(frutta.index("Banana"))

if scelta == "Mela": 
  print(frutta.index("Mela"))

if scelta == "Ananas": 
  print(frutta.index("Ananas"))

if scelta == "Fragola": 
  print(frutta.index("Frago

10)
list = ["Francesco", "Giacomo" , "Mattia" , "Paolo", "Leonardo"]

c = 0
while c < len(list):
  print(list[c])
  c += 1

11)
list = ["Francesco", "Giacomo" , "Mattia" , "Paolo", "Leonardo", "Marco", "Antonio", "Giuseppe", "Lucia", "Anna"]
list.sort()
c = 0
while c < len(list):
  print(list[c])
  c += 1
