from enum import Enum

from colors import bcolors


class Direction(Enum):
    """Enum Kodierung Schiffrichtungen"""

    RECHTS = "r"
    LINKS = "l"
    OBEN = "o"
    UNTEN = "u"

    @staticmethod
    def einlesen() -> "Direction":
        """Einlesen Schiffsdaten"""
        while True:
            print(
                f"{bcolors.UNDERLINE}In welche Richtung soll das Schiff platziert werden?{bcolors.RESET}\n r: rechts\n l: links\n o: oben\n u: unten"
            )
            eingabe = str(input("Richtung eingeben: ")).lower()
            try:
                if eingabe in "lrou":
                    if eingabe == "l":
                        return Direction.LINKS
                    if eingabe == "r":
                        return Direction.RECHTS
                    if eingabe == "o":
                        return Direction.OBEN
                    if eingabe == "u":
                        return Direction.UNTEN
                    raise KeyError(
                        f"{bcolors.RED}Fehler: Ungültige Richtung angegeben{bcolors.RESET}"
                    )
                print(f"{bcolors.RED}Fehler: Ungültige Eingabe{bcolors.RESET}")
                continue
            except ValueError:
                print(f"{bcolors.RED}Fehler: Ungültige Eingabe{bcolors.RESET}")
