import random as r

from . import files as f
from . import paths as p

def escolha_aleatoria_ci(categoria: str) -> str:
    path = p.FPATH_CI+p.Dci[categoria]
    lista = f.filelines(path)
    return r.choice(lista)

