from remittance import AmountRange, TransferType


class RemitlyFee(object):
    """
    Reemitly fee details
    """
    express_rate = {
        AmountRange.v_0_to_499.value: 3.99,
        AmountRange.v_500_to_999.value: 3.99,
        AmountRange.v_1000_to_1999.value: 3.99,
        AmountRange.v_above_2000.value: 3.99
    }

    economy_rate = {
        AmountRange.v_0_to_499.value: 0,
        AmountRange.v_500_to_999.value: 0,
        AmountRange.v_1000_to_1999.value: 0,
        AmountRange.v_above_2000.value: 0
    }

    fee = {TransferType.bank_account.value: economy_rate,
           TransferType.debit_card.value: express_rate}


class RiaFee(object):
    """
    Ria fee details
    """
    express_rate = {
        AmountRange.v_0_to_499.value: 3,
        AmountRange.v_500_to_999.value: 7,
        AmountRange.v_1000_to_1999.value: 11,
        AmountRange.v_above_2000.value: 18
    }

    economy_rate = {
        AmountRange.v_0_to_499.value: 1,
        AmountRange.v_500_to_999.value: 1,
        AmountRange.v_1000_to_1999.value: 1,
        AmountRange.v_above_2000.value: 1
    }

    fee = {TransferType.bank_account.value: economy_rate,
           TransferType.debit_card.value: express_rate}


class WesternUnionFee(object):
    """
    Western union fee details
    """
    express_rate = {
        AmountRange.v_0_to_499.value: 2.99,
        AmountRange.v_500_to_999.value: 2.99,
        AmountRange.v_1000_to_1999.value: 2.99,
        AmountRange.v_above_2000.value: 2.99
    }

    economy_rate = {
        AmountRange.v_0_to_499.value: 0,
        AmountRange.v_500_to_999.value: 0,
        AmountRange.v_1000_to_1999.value: 0,
        AmountRange.v_above_2000.value: 0
    }

    fee = {TransferType.bank_account.value: economy_rate,
           TransferType.debit_card.value: express_rate}


class XoomFee(object):
    """
    Xoom union fee details
    """
    express_rate = {
        AmountRange.v_0_to_499.value: 2.99,
        AmountRange.v_500_to_999.value: 4.99,
        AmountRange.v_1000_to_1999.value: 0,
        AmountRange.v_above_2000.value: 0
    }

    economy_rate = {
        AmountRange.v_0_to_499.value: 2.99,
        AmountRange.v_500_to_999.value: 4.99,
        AmountRange.v_1000_to_1999.value: 0,
        AmountRange.v_above_2000.value: 0
    }

    fee = {TransferType.bank_account.value: economy_rate,
           TransferType.debit_card.value: express_rate}
