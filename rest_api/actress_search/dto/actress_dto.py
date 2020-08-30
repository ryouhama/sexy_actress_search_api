import dataclasses


@dataclasses.dataclass
class Actress:
    id: str
    name: str
    bust: str
    waist: str
    hip: str
    height: str
    imageURL_small: str
    imageURL_large: str
    listURL_digital: str
    listURL_monthly: str
    listURL_ppm: str
    listURL_mono: str
    listURL_rental: str
