import learn.paths as lp
import learn.categories as lc

# main
print("--- Sorteador de Desafios de Desenhos ---\n")

print("\tEscolha uma das categorias:\n")

it = 1
for item in lp.Lci:
    print(f"{it}. {item}")
    it=it+1

entrada = input("\n")

saida = lc.escolha_aleatoria_ci(lp.Lci[int(entrada)-1])

print(f"\nO resultado foi: {saida}")

