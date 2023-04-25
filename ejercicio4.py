"""milistadefrutas = ["manzana","banana","cereza"]
print(milistadefrutas)
print(type(milistadefrutas))
print(milistadefrutas[0])
print(milistadefrutas[1])
print(milistadefrutas[2])

milistadefrutas[2] = "naranja"
print(milistadefrutas)"""

"""myFinalAnswerTuple = ("manzana","banana","piña")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

"""
mifrutafavoritadiccionario = {
    "Akua" : ["manzana","pera","limon"],
    "Saanvi" : ["manzana","banana","cereza"],
    "Paulo" : ["manzana","mango","arroz"]
}
print(mifrutafavoritadiccionario)
print(type(mifrutafavoritadiccionario))

print(mifrutafavoritadiccionario["Akua"][0])
print(mifrutafavoritadiccionario["Saanvi"][2])
print(mifrutafavoritadiccionario["Paulo"][1])
import pandas
mydb=pandas.DataFrame(mifrutafavoritadiccionario)
print(mydb)