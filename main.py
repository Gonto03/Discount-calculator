import time

DECIMALS = 2

def calculate_discount(original_price, new_price):   # calculates the discount in percentage
    if new_price > original_price:
        print("\nO novo preço é maior que o original. Logo, não há desconto.")
        time.sleep(0.6)
        print("------------------------------------------//--------------------------------------------------\n")
        return -1
    return (1 - new_price / original_price) * 100

def valid_input(inp: str):  # reformats the input to the right format
    inp = inp.replace(',','.')
    return float(inp)


def run():
    while True:
        try:    # receiving the original price
            original_price = valid_input(input("Preço original: "))
        except ValueError:
            print("\nO valor não foi introduzido de forma correta. Por favor, repita o processo.")   
            time.sleep(0.4)
            print("------------------------------------------//--------------------------------------------------\n")
            continue

        try:    # receiving the new price
            new_price = valid_input(input("Novo preço: "))
        except ValueError:
            print("\nO valor não foi introduzido de forma correta. Por favor, repita o processo.")   
            time.sleep(0.4)
            print("------------------------------------------//--------------------------------------------------\n")
            continue
            
        discount = round(calculate_discount(original_price, new_price), DECIMALS)   # calculating the discount
        if discount == -1:
            continue
        discount = str(discount)
        discount = discount.replace('.',',')
        print(f"\n-> O desconto é de {discount}%\n")
        time.sleep(0.3)
        print("\nPrograma desenvolvido por Gonçalo Dias. Utilização autorizada a Ana Isabel Dias")
        print("------------------------------------------//--------------------------------------------------\n")
        
run()