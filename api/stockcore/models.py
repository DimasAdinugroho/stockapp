# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aces(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACES'


class Adro(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADRO'


class Agii(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGII'


class Agro(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGRO'


class Aisa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AISA'


class Alto(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALTO'


class Antm(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANTM'


class Apic(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APIC'


class Apln(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APLN'


class Army(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARMY'


class Arna(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARNA'


class Asgr(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASGR'


class Asmi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASMI'


class Asri(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASRI'


class Bbhi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BBHI'


class Bbkp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BBKP'


class Bcip(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCIP'


class Bell(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BELL'


class Best(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BEST'


class Bjtm(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BJTM'


class Bksl(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BKSL'


class Bmtr(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMTR'


class Bnga(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BNGA'


class Bnli(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BNLI'


class Boga(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOGA'


class Brpt(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BRPT'


class Bsde(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BSDE'


class Btek(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BTEK'


class Bull(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BULL'


class Bumi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUMI'


class Bvic(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BVIC'


class Bwpt(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BWPT'


class Cint(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CINT'


class Cleo(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLEO'


class Ctra(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRA'


class Dild(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DILD'


class Dmas(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DMAS'


class Doid(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOID'


class Dsfi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DSFI'


class Elsa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ELSA'


class Eraa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERAA'


class Finn(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FINN'


class Forz(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORZ'


class Giaa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GIAA'


class Gjtl(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GJTL'


class Gmfi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GMFI'


class Gpra(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPRA'


class Hoki(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOKI'


class Home(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOME'


class Iikp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IIKP'


class Inpp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INPP'


class Inta(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTA'


class Issp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ISSP'


class Jpfa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JPFA'


class Jrpt(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JRPT'


class Kbli(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KBLI'


class Kija(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KIJA'


class Klbf(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KLBF'


class Kras(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KRAS'


class Kren(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KREN'


class Lpkr(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LPKR'


class Lsip(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LSIP'


class Mark(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARK'


class Mbss(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MBSS'


class Mcor(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MCOR'


class Mdki(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MDKI'


class Mdln(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MDLN'


class Medc(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDC'


class Meta(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'META'


class Mika(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MIKA'


class Mlpl(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MLPL'


class Mncn(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MNCN'


class Mpmx(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MPMX'


class Mppa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MPPA'


class Mtwi(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MTWI'


class Myor(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MYOR'


class Myrx(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MYRX'


class Nobu(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOBU'


class Oasa(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OASA'


class Okas(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OKAS'


class Panr(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PANR'


class Pbrx(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PBRX'


class Pgas(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PGAS'


class Pnbn(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PNBN'


class Pnlf(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PNLF'


class Ppro(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PPRO'


class Psab(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSAB'


class Ptro(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PTRO'


class Pwon(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PWON'


class Rals(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RALS'


class Ranc(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RANC'


class Rbms(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RBMS'


class Same(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAME'


class Scma(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCMA'


class Ship(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHIP'


class Sido(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIDO'


class Sima(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIMA'


class Simp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIMP'


class Smcb(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMCB'


class Smdr(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMDR'


class Smmt(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMMT'


class Smra(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMRA'


class Soci(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOCI'


class Sril(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SRIL'


class Ssia(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SSIA'


class Ssms(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SSMS'


class Tara(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TARA'


class Tele(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TELE'


class Tins(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TINS'


class Tmas(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMAS'


class Tram(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRAM'


class Trim(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIM'


class Tris(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIS'


class Weha(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WEHA'


class Wika(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WIKA'


class Womf(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WOMF'


class Wood(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WOOD'


class Wsbp(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WSBP'


class Wskt(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WSKT'


class Wton(models.Model):
    itemtime = models.DateTimeField(db_column='itemTime', primary_key=True)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice')  # Field name made lowercase.
    itemchange = models.DecimalField(db_column='itemChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemturnover = models.BigIntegerField(db_column='itemTurnover', blank=True, null=True)  # Field name made lowercase.
    itemmarketcap = models.BigIntegerField(db_column='itemMarketcap', blank=True, null=True)  # Field name made lowercase.
    itemvolume = models.BigIntegerField(db_column='itemVolume', blank=True, null=True)  # Field name made lowercase.
    itemfreq = models.IntegerField(db_column='itemFreq', blank=True, null=True)  # Field name made lowercase.
    itemask = models.IntegerField(db_column='itemAsk', blank=True, null=True)  # Field name made lowercase.
    itembid = models.IntegerField(db_column='itemBid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WTON'
