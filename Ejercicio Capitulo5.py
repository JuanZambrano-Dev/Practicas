print('---- BIENVENIDO A LA PIZZERIA JP----')
print('Cada ingrediente extra tiene un costo de 3$')
print('Contamos con 3 tipos de pizza: Peperonni, 4 estaciones y hawaiana')
print('Peperonni = 300$\n4 Estaciones = 500$ \nHawaiana = 350$')

peperonni = 300
estaciones = 500
hawaiana = 350



dinero = int(input('Indique el dinero que usara para comprar la pizza: '))

pizza_solicitada = input('Indica la pizza que quieras comprar:\n')

ingredientes = []


for ingrediente_extra in range(3):
    solicitud = input('Desea añadir un ingrediente extra? Si/No. El total de ingredientes extras es de 3 \n')
    if solicitud.lower() == 'si':
        ingrediente_extra = input('Indica el nuevo ingrediente: \n')
        ingredientes.append(ingrediente_extra)
    elif solicitud.lower() == 'no':
        break
print(f'Los ingredientes que indicaste son los siguientes: {ingredientes}' )

total = 0

for costo_ingrediente in ingredientes:
    costo_ingredienteingrediente = len(ingredientes) * 3
    total += costo_ingrediente
print(f'El precio total de sus ingredientes es de: {total}$\n')

def total_pagar():
    if pizza_solicitada.lower() == 'peperonni':
        return peperonni + total
    elif pizza_solicitada.lower() == '4 estaciones':
        return estaciones + total
    elif pizza_solicitada.lower() == 'hawaiana':
        return hawaiana + total
    else:
        return 'No contamos con ese tipo de pizza'

def pagando():
    if dinero >= total_pagar():
        return dinero - total_pagar()
    else:
        return 'No tienes dinero suficiente para pagar'

print(f'El total a pagar es de: {total_pagar()}$\n')
print(f'Este es el dinero que te queda luego de pagar la pizza: {pagando()}\n')

