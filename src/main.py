import learn.paths as lp
import learn.categories as lc

# main
print("--- Sorteador de Desafios de Desenhos ---\n")

qtd_categorias = input("\nQuantas categorias você quer escolher? (Máx. 9)\n")

saida = ""

if qtd_categorias == "1": 
    print("\n\tEscolha uma das categorias:\n")
    it = 1
    for item in lp.Lci:
        print(f"{it}. {item}")
        it=it+1
    
    entrada = input("\n")
    sorteio = lc.escolha_aleatoria_ci(lp.Lci[int(entrada)-1])
    saida = f"{lp.Lci[int(entrada)-1]}: {sorteio}"
elif qtd_categorias == "9":
    print("\n\tTodas as categorias escolhidas\n")
    for item in lp.Lci:
        sorteio = lc.escolha_aleatoria_ci(item)
        saida += f"{item}: {sorteio}\n"

else:
    saida = "nada"




print(f"\nO resultado foi: \n{saida}")

