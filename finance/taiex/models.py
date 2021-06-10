from django.db import models


class TaiexManager(models.Manager):
    def create_taiex(
        self,
        trade_date,
        opening_price,
        highest_price,
        lowest_price,
        closing_price,
        trade_volume,
        trade_value,
        transaction,
    ):
        taiex = self.create(
            trade_date=trade_date,
            opening_price=opening_price,
            highest_price=highest_price,
            lowest_price=lowest_price,
            closing_price=closing_price,
            trade_volume=trade_volume,
            trade_value=trade_value,
            transaction=transaction,
        )
        return taiex

    def get_latest_date(self):
        latest_data = self.latest("trade_date").trade_date
        return latest_data


class Taiex(models.Model):
    trade_date = models.DateField(primary_key=True, help_text="交易日期")
    opening_price = models.FloatField(help_text="開盤價", null=True)
    highest_price = models.FloatField(help_text="最高價", null=True)
    lowest_price = models.FloatField(help_text="最低價", null=True)
    closing_price = models.FloatField(help_text="收盤價", null=True)
    trade_volume = models.BigIntegerField(help_text="成交股數", null=True)
    trade_value = models.BigIntegerField(help_text="成交金額", null=True)
    transaction = models.BigIntegerField(help_text="成交筆數", null=True)

    objects = TaiexManager()

    def __str__(self):
        return (
            f"{self.trade_date} 開盤：{self.opening_price} "
            f"最高：{self.highest_price} 最低：{self.lowest_price} "
            f"收盤：{self.closing_price}"
            f"成交股數：{self.trade_volume}"
            f"成交金額：{self.trade_value}"
            f"成交筆數：{self.transaction}"
        )

    class Meta:
        db_table = "taiex"
