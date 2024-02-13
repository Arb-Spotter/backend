# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exchanges(models.Model):
    exchange = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = "exchanges"


class MarketData(models.Model):
    token = models.OneToOneField(
        "Tokens", models.DO_NOTHING, db_column="token", primary_key=True
    )  # The composite primary key (token, updatedAt, exchange) found, that is not supported. The first column is selected.
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    exchange = models.TextField()
    percentage_change = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    b_a_spread = models.FloatField(blank=True, null=True)
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "market_data"
        unique_together = (("token", "updatedat", "exchange"),)


class OneDayOhlcvData(models.Model):
    token = models.OneToOneField(
        "Tokens", models.DO_NOTHING, db_column="token", primary_key=True
    )  # The composite primary key (token, updatedAt, exchange) found, that is not supported. The first column is selected.
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    exchange = models.TextField()
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "one_day_ohlcv_data"
        unique_together = (("token", "updatedat", "exchange"),)


class OneHourOhlcvData(models.Model):
    token = models.OneToOneField(
        "Tokens", models.DO_NOTHING, db_column="token", primary_key=True
    )  # The composite primary key (token, updatedAt, exchange) found, that is not supported. The first column is selected.
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    exchange = models.TextField()
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "one_hour_ohlcv_data"
        unique_together = (("token", "updatedat", "exchange"),)


class OneMinOhlcvData(models.Model):
    token = models.OneToOneField(
        "Tokens", models.DO_NOTHING, db_column="token", primary_key=True
    )  # The composite primary key (token, updatedAt, exchange) found, that is not supported. The first column is selected.
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    exchange = models.TextField()
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "one_min_ohlcv_data"
        unique_together = (("token", "updatedat", "exchange"),)


class Tokens(models.Model):
    token = models.TextField(unique=True)
    large = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    thumb = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tokens"


class TokensMarketData(models.Model):
    name = models.TextField(blank=True, null=True)
    thumb = models.TextField(blank=True, null=True)
    large = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)
    percentage_change = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    b_a_spread = models.FloatField(blank=True, null=True)
    updatedat = models.DateTimeField(
        db_column="updatedAt", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "tokens_market_data"
