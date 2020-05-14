from remittance import (
    AmountRange, TransferType, RemitlyFee,
    WesternUnionFee, RiaFee, XoomFee
)


class BuildImage:
    """
    Build new html image with the given information
    """
    def __init__(self, page, rates):
        self.page = page
        self.rates = rates

    def get_image(self):
        """
        Build and return new html page
        :return:
        """
        self.page = self.page % (
            self.rates.remitly_rate[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            RemitlyFee.fee[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            self.rates.remitly_rate[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            RemitlyFee.fee[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            self.rates.remitly_rate[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            RemitlyFee.fee[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            self.rates.remitly_rate[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            RemitlyFee.fee[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            self.rates.ria_rate[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            RiaFee.fee[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            self.rates.ria_rate[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            RiaFee.fee[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            self.rates.ria_rate[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            RiaFee.fee[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            self.rates.ria_rate[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            RiaFee.fee[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            self.rates.xoom_rate[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            XoomFee.fee[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            self.rates.xoom_rate[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            XoomFee.fee[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            self.rates.xoom_rate[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            XoomFee.fee[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            self.rates.xoom_rate[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            XoomFee.fee[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            self.rates.wu_rate[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            WesternUnionFee.fee[TransferType.bank_account.value][AmountRange.v_0_to_499.value],
            self.rates.wu_rate[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            WesternUnionFee.fee[TransferType.bank_account.value][AmountRange.v_500_to_999.value],
            self.rates.wu_rate[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            WesternUnionFee.fee[TransferType.bank_account.value][AmountRange.v_1000_to_1999.value],
            self.rates.wu_rate[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            WesternUnionFee.fee[TransferType.bank_account.value][AmountRange.v_above_2000.value],
            self.rates.remitly_rate[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            RemitlyFee.fee[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            self.rates.remitly_rate[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            RemitlyFee.fee[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            self.rates.remitly_rate[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            RemitlyFee.fee[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            self.rates.remitly_rate[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            RemitlyFee.fee[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            self.rates.ria_rate[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            RiaFee.fee[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            self.rates.ria_rate[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            RiaFee.fee[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            self.rates.ria_rate[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            RiaFee.fee[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            self.rates.ria_rate[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            RiaFee.fee[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            self.rates.xoom_rate[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            XoomFee.fee[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            self.rates.xoom_rate[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            XoomFee.fee[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            self.rates.xoom_rate[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            XoomFee.fee[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            self.rates.xoom_rate[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            XoomFee.fee[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            self.rates.wu_rate[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            WesternUnionFee.fee[TransferType.debit_card.value][AmountRange.v_0_to_499.value],
            self.rates.wu_rate[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            WesternUnionFee.fee[TransferType.debit_card.value][AmountRange.v_500_to_999.value],
            self.rates.wu_rate[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            WesternUnionFee.fee[TransferType.debit_card.value][AmountRange.v_1000_to_1999.value],
            self.rates.wu_rate[TransferType.debit_card.value][AmountRange.v_above_2000.value],
            WesternUnionFee.fee[TransferType.debit_card.value][AmountRange.v_above_2000.value]
        )
        return self.page
