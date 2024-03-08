#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#funciones propias

def validarDNI(d):
    dni_arr=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F' ,'P', 'D','X','B','N' ,'J', 'Z' ,'S' , 'Q', 'V', 'H', 'L','C','K','E']
    dniNum=int(d[0:8])
    dniresto=dniNum%23

    if dni_arr[dniresto] == str(d[8]):
        return ("Bienvenido")
    else:
        return ("No Bienvenido")
    
'''
resultado =validarDNI('05326343A')
print(resultado)
'''