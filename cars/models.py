# Есть автомобильный завод,
# нужна система для хранения стоимости деталей машины и расчета итоговой стоимости автомобиля.
# Каждая деталь имеет:
#   1) Тип (фара, решётка, ручка и т.д.)
#   2) цену
#   3) необходимое количество на один автомобиль,
#   4) набор индивидуальных параметров.
#
# Задача:
# Подготовить таблицы базы данных для расчета стоимости автомобиля.
# Учитывать, что стоимость автомобиля состоит из стоимости деталей и наценки производителя.
# Все расчеты необходимо описать внутри классов django моделей.
# Для упрощения можно сделать базу данных, исходя из того, что автомобиль состоит из капота, фары, руля и кресла.
# Расчеты и результаты лучше всего хранить в ещё одной отдельной таблице

from django.db import models


# Название параметра
class ParamName(models.Model):
    name = models.CharField("Название", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


# Параметр
class Param(models.Model):
    name = models.ForeignKey(
        "ParamName",
        on_delete=models.PROTECT,
        verbose_name="Название",
        related_name="param_name",
    )
    value = models.CharField("Значение", max_length=50, null=False)

    def __str__(self):
        return f"{self.name} - {self.value}"


# Тип детали
class DetailType(models.Model):
    name = models.CharField("Название", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


# Деталь
class Detail(models.Model):
    name = models.CharField("Название", max_length=50, null=False)
    detail_type = models.ForeignKey(
        "DetailType",
        on_delete=models.PROTECT,
        verbose_name="Тип детали",
        related_name="detail_type",
    )
    price = models.DecimalField(verbose_name="Цена", max_digits=11, decimal_places=2)
    amount_per_car = models.PositiveSmallIntegerField(
        verbose_name="Количество на одну машину",
        default=0
    )
    params = models.ManyToManyField(Param)

    def __str__(self):
        return f"{self.name} [{self.detail_type}] - {self.amount_per_car} x {self.price}"


# Бренд или производитель
class Brand(models.Model):
    name = models.CharField("Название", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


# Машина
class Car(models.Model):
    toppings = None
    name = models.CharField("Название", max_length=50, null=False)
    detail_type = models.ForeignKey(
        "Brand",
        on_delete=models.PROTECT,
        verbose_name="Бренд",
        related_name="car_brand",
    )
    params = models.ManyToManyField(Detail)

    def __str__(self):
        return f"{self.name}"


# Цена машины
class CarPrice(models.Model):
    car = models.OneToOneField(
        "Car",
        on_delete=models.PROTECT,
        verbose_name="Машина",
        related_name="car",
    )
    cost_price = models.DecimalField(verbose_name="Себестоимость", max_digits=17, decimal_places=2, default=0)
    margin = models.DecimalField(verbose_name="Наценка", max_digits=5, decimal_places=2, default=1.1)
    price = models.DecimalField(verbose_name="Цена машины", max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.car.name} - {self.price} [{self.cost_price}]"

    def save(self, *args, **kwargs):
        details = self.car.params.all()
        self.cost_price = sum(list(map(
            lambda x: x.price * x.amount_per_car,
            details
        )))
        self.price = self.cost_price * self.margin

        super(CarPrice, self).save(*args, **kwargs)
