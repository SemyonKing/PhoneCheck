# Путиводитель для Никиты ( ˘ ³˘)♥︎

----

Я всё проверял с помощью `PostMan`. Выбирал тип запроса `POST`,
 потом выбирал вкладку `Body`. В ней я выбрал `row` и написал:

```json
{
	"phone": "+7 (996) 911 82 87"
}
```

После выполнения запроса должно прийти это:

```json
{
	"valid": "true"
}
```

Если номер не будет следовать маске `+7 (___) ___-__-__` то выдаст это:

```json
{
	"valid": "false"
}
```