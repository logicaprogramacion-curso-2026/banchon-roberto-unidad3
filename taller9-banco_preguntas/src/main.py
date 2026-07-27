from entidad import Pregunta

pregunta = Pregunta(
    1,
    "¿Qué función devuelve la longitud de una lista?",
    "size()",
    "len()",
    "count()",
    "length()",
    "B",
    "Fácil",
    "Funciones Built-in"
)

print(pregunta)
print()
print(pregunta.to_dict())