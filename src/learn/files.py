import paths as p

def readfile(path: str) -> str:
    with open(path, "r", encoding="utf-8") as arq:
        conteudo = arq.read()
        # print(conteudo)
    return conteudo

def filelines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as arq:
        linhas = arq.read().splitlines()
        # print(linhas)    
    return linhas


# main test
"""
path = p.FPATH_CI+p.Dci["local"]
lista = filelines(path)
print(lista)
"""

