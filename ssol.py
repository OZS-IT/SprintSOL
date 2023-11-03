from ssol_fun import *
from os import path
import csv
tek={}
stanjeLige={}
kat=set()
for j in range(1,17):
    dat="./Registracije/registracije"+str(j)+".csv"
    if not path.isfile(dat):
        break
    tekmaRegistracije=j
    #Na kateri še ne šteje za točkovanje.
    #Še ni vključeno, vljuči enkrat.
    with open(dat,'r',encoding="utf-8") as f:
        for i in f:
            a=i.split(";")
            st=a[0]
            ime=a[1]
            priimek=a[2]
            klub=a[3]
            kate=a[4]
            s=presledki(sumniki(a[1]+a[2]))
            s=s.lower()
            if kate[-1] == "\n":
                kate = kate[:-1]
            kat.add(kate)
            if ime=="Žiga" and priimek=="Groff":
                st="483"
            elif ime == "Cesare" and priimek == "Tarrabocchia":
                klub = "OK Azimut"
            elif ime == "Andraž" and priimek == "De Luisa":
                klub = "OK Azimut"
            if s not in tek.keys():
                tek[s]=[kate,ime,priimek,tekmaRegistracije,klub,st]
    for i in kat:
        stanjeLige[i]={}
    for i in tek.keys():
        b=tek[i]
        stanjeLige[b[0]][i]={"ime":b[1],"priimek":b[2],"klub":b[4],0:0,"tekmaRegistracije":b[3]}

st_tekem=0
IP=1
zadnja=16
for st_lige in range(1,12):
    if st_lige==zadnja:#Nočemo, da se zgodi v sol, je pa na voljo.
        IP=1.15
    if path.isfile('./Rezultati/SSOL'+str(st_lige)+'.csv'):
        print("Berem rezultate za SSOL" + str(st_lige))
        c=rezultati(st_lige,stanjeLige,kat,tek)
        stanjeLige=izracunLige(c,st_lige,stanjeLige,IP,kat,tek)
        #print(stanjeLige["M55"])
        #print(stanjeLige["M21E"]["jurezmrzlikar"])
        st_tekem+=1
        vCsv(stanjeLige,st_tekem,kat,tek)
if path.isfile('./Resna stanja/SSOL'+str(st_tekem)+'.csv'):
    g=open('ssol_2024.csv','w',encoding='utf-8')
    with open('./Resna stanja/SSOL'+str(st_tekem)+'.csv','r',encoding='utf-8') as f:
        for i in f.readlines():
            g.write(i)
    g.close()
