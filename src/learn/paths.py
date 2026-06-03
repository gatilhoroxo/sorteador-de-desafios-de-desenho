from typing import Final
from pathlib import Path

# folder path categorias independentes
FPATH_CI: Final = "../data/categorias/independentes"

# lista com as categorias independentes
Lci = [
    "tema", 
    "universo", 
    "local", 
    "clima", 
    "elemento", 
    "personagem", 
    "misterio", 
    "estilo-visual", 
    "restricoes-criativas"
]

# dicionário com os caminhos independentes
Dci = {
    "tema": "/tema.txt",
    "universo": "/universo.txt",
    "local": "/local.txt",
    "clima": "/clima.txt",
    "elemento": "/elemento.txt",
    "personagem": "/personagem.txt",
    "misterio": "/misterio.txt",
    "estilo-visual": "/estilo-visual.txt",
    "restricoes-criativas": "/restricoes-criativas.txt",
}

