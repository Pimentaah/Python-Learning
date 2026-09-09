def calcular_desconto():
    desconto = preco * (porcentagem / 100)
    preco_final = preco - desconto
    return preco_final
    
preco = float(input("Qual é o preço do produto: "))
porcentagem = float(input("Qual a porcentagem do desconto: "))

print (f"O valor do produto é {preco} mas com desconto de {porcentagem} o valor resultou em {calcular_desconto()}")
    
    
   