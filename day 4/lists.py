estados_do_brasil = ["Bahia", "Rio de Janeiro", "Maranhão", "Pará", "Pernambuco", "São Paulo", "Minas Gerais", "Goiás", "Mato Grosso", "Rio Grande do Sul", "Ceará", "Paraíba", "Espírito Santo", "Piauí", "Rio Grande do Norte", "Alagoas", "Sergipe", "Santa Catarina", "Amazonas", "Paraná", "Distrito Federal", "Acre", "Mato Grosso do Sul", "Rondônia", "Tocantins", "Roraima", "Amapá"]

estados_do_brasil[6] = "Caras Específicos"

estados_do_brasil.append("Guiana Brasileira")
estados_do_brasil.extend(["Uruguai", "Venezuela"])

print(estados_do_brasil)

import random

friends = ["a", "b", "c"]
print(random.choice(friends))

random_index = random.randint(0,2)
print(friends[random_index])

estados_do_brasil_atual = ["Bahia", "Rio de Janeiro", "Maranhão", "Pará", "Pernambuco", "São Paulo", "Minas Gerais", "Goiás", "Mato Grosso", "Rio Grande do Sul", "Ceará", "Paraíba", "Espírito Santo", "Piauí", "Rio Grande do Norte", "Alagoas", "Sergipe", "Santa Catarina", "Amazonas", "Paraná", "Distrito Federal", "Acre", "Mato Grosso do Sul", "Rondônia", "Tocantins", "Roraima", "Amapá"]
num_estados = len(estados_do_brasil_atual) #27
print(estados_do_brasil_atual[num_estados - 1])

#dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][2])