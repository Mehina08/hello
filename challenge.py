print("challenge #1:")
non="TOUT BAGAY POSIB DEPIW VLE YO \n"
mo=non.lower()
print(mo)

###################

print("challenge #2:")
b="tout rete pozitif "
c=b.split()
print(c)
print("\n")

#####################

print("challenge#3:")
mo= "bonjou, jodi a se mardi.\n"
a=mo.title()
print(a)

#####################

print("Challlenge#5:")
ch="Lew pa gen manman, ou tete grann"
chenn= ch.replace("a","@")
print(chenn)
print("\n")

###################

print("Challenge#6:")
kar="I believe i can fly, i believe i can touch the sky."
k=''.join(reversed(kar))
print(k)
print("\n")

##################

print("Challenge#7:")
va="Mwen pa gen problèm ak pèsòn"
for i in va:
    i=va.index("a")
print(i)
print("\n")

#########!##########

print("Challenge#8:")
pa= "rayi chen an di danl blan"
sum=0
for k in range(len(pa)):
    if pa[k]=="a":
         sum+=k
print (sum)
print("\n")

######################

print("Challenge#9:")
x="Men nan men , an nou rebati Ayiti."
char="a"
y=[a for a , c in enumerate(x) if c == char]
print(y)
print("\n")

############!#!!!#####

print("Challenge#10:")
z="Aimez vous les uns les autres"
t=z.replace(" ", "")
print(t)
print("\n")

######___Master List ___########

print("Challenge #1 ---->MASTER: LISTE: ")
nonb=[2,4,6,18,25,27,99,88,111]
p=[]
for i in nonb:
    if i % 2==0:
        p.append(i)
print(p)
print("\n")
  
######################

print("challenge #2:")
lis_antye=[2,4,6,8,10,12,14,16,18,20]
print([str(x) for x in lis_antye ])
print("\n")

############!#!!!#####

print("Challenge#3:")
po="oma,pwason, ekrevis,lanbi"
print(po.upper())
print("\n")

############!#!!!#####

print("Challenge#4: ")
f=[10,5,20,"Claude",15,"Lion",30,25,"Marjorie"]
r=[]
for i in f:
    if i ==3:
        r.append(i)
        print(r.append(i))

############!#!!!#####

print("Challenge#6 ")
liste=[1990,2000,1978,1578,23,67,89,1,200,3,48,5,6,7,88,7,23,2,2000,89,1999,1990,23,66,100,4,5,9,101,100,7,8,44,6,5,4,2000]

print(list(set(liste)))
print("\n")

############!#!!!#####

print("Challenge#7:")
lis_1=[2,5,7,8,0,34,67,88,100,12,1]
lis_2=[2,88,76,12,0,7,8,1,34,79,90]
lis_3=[]
for i in lis_1:
    if i in lis_2:
        lis_3.append(i)
print(lis_3)
print("\n")

############!#!!!#####

print("Challenge#8:")
lis_1=[2,5,7,8,0,34,67,88,100,12,1]
lis_2=[2,88,76,12,0,7,8,1,34,79,90]
lis_4=[]
for i in lis_1:
    if i not in lis_2 :
        lis_4.append(i)
print(lis_4)
print("\n")

########################

print("CHALLEMGE#9: ")
info={ "Nom":"Charles", "Prenom":"Caroline","Âge":"28 ans", "Adresse":"Delmas 41B", "Plat prefere":"Riz, lalo et purée de pois" }
print(info.values())
print(info.keys())
print("\n")

##########################

print("Challenge#10:")
x=[9,8,7,6,5,4,3,2,1]

y=[2,4,6,8,10,12,14,16,18,20,21,22,23,24]

z=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

resultat=x+y+z

print(list(set(resultat)))


