from pyscript import display, document


def skumaker(e):
    flowertype = document.getElementById('flowertype').value
    bouquets = document.getElementById('bouquets').value.strip()
    quantity = document.getElementById('quantity').value

    if bouquets == "" or quantity == "":
        display(
            "Please enter the product name and stock quantity.",
            target="details"
        )
        display(
            "Your SKU will appear here.",
            target="sku"
        )

        return
    
    bouquetsku = bouquets.upper()[:3]

    quantitysku = quantity[:2]

    sku = flowertype + bouquetsku + quantitysku

    display(sku,target="sku")

    display(
        f"flowertype: {flowertype} | Product: {bouquets} | Stock: {quantity}", target="details")