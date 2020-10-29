# -*- coding: utf-8 -*-
import os

def cargar_porcentajes(archivo):
  f = open(archivo)
  lineas = [x.strip("\n") for x in f.readlines()]
  f.close()

  return [(x.split(",")[0], int(x.split(",")[1])/100) for x in lineas]

def cargar(archivo):
  f = open(archivo)
  lineas = [x.strip("\n") for x in f.readlines()]
  f.close()
  return lineas


def capturar_notas(alumnos, porcentajes, materias):
  f = open("notas.txt", "w")
  for a in alumnos:
    print("alumno: " + a)
    for m in materias:
      f.write(a)
      f.write(", " + m)
      print("materia: " + m)
      for p in porcentajes:
        valor = input(p[0] + ": ")
        f.write(", " + str(valor))
      f.write("\n")
  f.close()

def calcular_definitivas(archivo, porcentajes):
  f = open(archivo, "r")
  lineas = [x.strip("\n") for x in f.readlines()]
  f.close()

  notas = [x.split(", ") for x in lineas]

  f = open("resultados.txt", "w")
  for n in notas:
    a = n[0]
    m = n[1]
    
    parciales = n[2:]
    definitiva = 0
    for p in range(len(parciales)):
      definitiva += int(parciales[p]) * porcentajes[p][1]
    f.write(a + ", " + m + ", " + str(definitiva) + "\n")
  f.close()

porcentajes = cargar_porcentajes("porcentajes.txt")
materias = cargar("materias.txt")
alumnos = cargar("alumnos.txt")

if not os.path.exists("notas.txt"):
  capturar_notas(alumnos, porcentajes, materias)

calcular_definitivas("notas.txt", porcentajes)