class Pregunta:
    """
    Representa una pregunta de selección múltiple.
    """

    def __init__(self, id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
                 respuesta_correcta, dificultad, tema):
        self.id = id
        self.pregunta = pregunta
        self.opcion_a = opcion_a
        self.opcion_b = opcion_b
        self.opcion_c = opcion_c
        self.opcion_d = opcion_d
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad
        self.tema = tema

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Pregunta: {self.pregunta}\n"
            f"A) {self.opcion_a}\n"
            f"B) {self.opcion_b}\n"
            f"C) {self.opcion_c}\n"
            f"D) {self.opcion_d}\n"
            f"Respuesta Correcta: {self.respuesta_correcta}\n"
            f"Dificultad: {self.dificultad}\n"
            f"Tema: {self.tema}"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "pregunta": self.pregunta,
            "opcion_a": self.opcion_a,
            "opcion_b": self.opcion_b,
            "opcion_c": self.opcion_c,
            "opcion_d": self.opcion_d,
            "respuesta_correcta": self.respuesta_correcta,
            "dificultad": self.dificultad,
            "tema": self.tema
        }