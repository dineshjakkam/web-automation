from enum import Enum


class AmountRange(Enum):
    """
    Enums for amount range
    """
    v_0_to_499 = 0
    v_500_to_999 = 1
    v_1000_to_1999 = 2
    v_above_2000 = 3


class TransferType(Enum):
    """
    Enums for transfer type
    """
    debit_card = 0
    bank_account = 1


