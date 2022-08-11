Модели описаны в `cars/models.py`.

Расчеты стоимости авто производятся в методе `models.CarPrice.save()`.
Стоимость пересчитывается с помощью сигналов (файл `signals.py`), если изменяются поля объекта модели `Car` или модели `Detail`.

Для загрузки фикстур использовать:

```bash
python manage.py loaddata cars/fixtures/models.json
```