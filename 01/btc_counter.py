# На вход принмаю такие значения: 
# countBtc - int 
# rate - float
# countBtc must be a int
def btc_cost_counter(countBtc, rate):
    
    if not isinstance(countBtc, int):
        return "countBtc must be a int"

    if not isinstance(rate, float):
        return "rate must be a float"
    
    return countBtc*rate