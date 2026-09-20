from pyscript import display, document


def create_order(e):

    subtotal = 0


   

    rose = 150

    tulip = 180

    sunflower = 200

    lavender = 170

    mixed = 250


    

    if document.getElementById('rose').checked:

        subtotal = subtotal + rose


    if document.getElementById('tulip').checked:

        subtotal = subtotal + tulip


    if document.getElementById('sunflower').checked:

        subtotal = subtotal + sunflower


    if document.getElementById('lavender').checked:

        subtotal = subtotal + lavender


    if document.getElementById('mixed').checked:

        subtotal = subtotal + mixed




    tax = subtotal * 0.12


  

    total = subtotal + tax


  

    display(f'Subtotal: ₱{subtotal:.2f}', target='subtotal')

    display(f'Tax: ₱{tax:.2f}', target='tax')

    display(f'Total: ₱{total:.2f}', target='total')