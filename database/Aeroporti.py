from dataclasses import dataclass

@dataclass(frozen=True)  #Lo rende hashable così da usarlo come nodo del grafo (l'oggetto intero)
class Aeroporti:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float