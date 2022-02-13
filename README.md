# Отчет

В начале этого непростого пути я решил ознакомиться с самим алгоритмом переноса стиля.

Источники:

https://www.youtube.com/watch?v=u2HDm7YSwoA&t=4045s&ab_channel=DeepLearningSchool

https://habr.com/ru/company/vk/blog/306916/

После просмотра видео и многократного прочтения статьи, я понял основной принцип работы данного алгоритма.

Следующим шагом было написание подобного алгоритма с переносом функциональности в классы.

За основу я взял следующую статью:

https://pytorch.org/tutorials/advanced/neural_style_tutorial.html

Следующим вопросом было: "А сколько эпох (шагов) модель должна работать?"

Однозначного ответа на этот вопрос нет, но я понял, что надо делать 200-500 итераций для адекватного результата, но все опять же зависит от самих изображений. Я остановился на числе 300...

Также я делал resize не 512x512, а пропорционально к изображению контента, но чтобы общее число пикселей не превышало 400000 (в начале я думал, что этого будет достаточно).

Следующей задачей было написание ассинхронного телеграм-бота. Мой выбор остановился на библиотеке aiogram, т.к. ранее я уже изучал данную библиотеку и имел какой-никакой опыт работы с ней.

Шаблоном моего бота послужил следующий источник:

https://github.com/Latand/aiogram-bot-template

Позже я добавил, как мне кажется, удобный интерфейс для работы с ботом (даже моя мама, которая ни разу не писала ботам смогла разобраться, а это многое говорит)

И вот, когда бот работал у меня локально, пришло время к последней части работы. Deploy бота на сервер.

Я решил воспользоваться сервисом под названием heroku. Видео, по которым я делал свои первые шаги в этом направлении находятся в глубинах англо-индусо-русского youtube.

Вот некоторые из них:

https://www.youtube.com/watch?v=QeTGN47WtOE&ab_channel=DonHaul

https://www.youtube.com/watch?v=JRCln3DkfBo&t=422s&ab_channel=IndieVitalja

Тут начались самые большие трудности. Самая главная из них - ограничение по памяти в 500МБ.

Вот решение, которое я использовал:

1) Уменьшение resize до 230000 пикселей

2) Установка torch и torchvision only-cpu версий

3) Скачивание только первых 5 pretrained слоев vgg19 (Источник, который помог это реализовать: https://pytorch.org/tutorials/beginner/saving_loading_models.html), это позволило сократить количество занимаемой памяти для модели с 548МБ до 2МБ. Я локально установил всю модель и скачал лишь первые слои, после сделал их загрузку в модель.
