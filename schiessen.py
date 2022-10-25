"""Schiessen"""
letters_to_numbers = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
}


class Schuss:
    """Klasse zur Implementierung der Schießfunktionen"""

    def __init__(self, posx: str, posy: int):
        self.posx = posx
        self.posy = posy

    def posx() -> int:
        """Einlesen X-Position Schuss"""
        print("Wohin soll geschossen werden")
        eingabe = str(input("X-Pos (Buchstabe) eingeben: "))

        return letters_to_numbers[eingabe]

    def posy() -> int:
        """Einlesen Y-Position Schuss"""
        eingabe = int(input("Y-Pos (Zahl) eingeben: "))

        return eingabe
