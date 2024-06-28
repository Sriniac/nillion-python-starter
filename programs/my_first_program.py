from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    factor = SecretInteger(Input(name="factor", party=party1))
    is_factor_mod=my_int1%factor
    is_factor_condition=is_factor_mod>=Integer(1)
    
    output=is_factor_condition.if_else(Integer(0),Integer(1))

    return [Output(output, "Is Factor", party1)]