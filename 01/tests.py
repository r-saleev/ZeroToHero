import btc_counter

test_cases = {
    1 : {
        "test_data" : (1.3, 5),
        "test_result" : "countBtc must be a int",
    },
    2 : {
        "test_data" : (5,"10"),
        "test_result" : "rate must be a float",
    },
    3 : {
        "test_data" : ("5", 10),
        "test_result" : "countBtc must be a int",
    },
    4 : {
        "test_data" : (5,10.0),
        "test_result" : 50,
    },
}

def test_answer():
    for k,i in test_cases.items():
        countBtc, rate = i["test_data"]
        assert btc_counter.btc_cost_counter(countBtc, rate) == i["test_result"]