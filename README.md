# pass_office_thermoBox
Бюро пропусков для RGB фотографий:
Функционал:
0. ДОбовления пользователя в базу
0. Редактирования пользователя
0. Фотографирования
0. Создание модели и базы для тренировки
0. Отправка данных на удаленный сервер распознования (нужен для проекта ThermoBox, Goodline_faceID, faceId_door)

# Настроки:
0. распользаются в settings
0. PATH_DATA_BASE - Путь для базы данных SQLite
0. PATH_SAVE_MODEL - Путь где будут хранится обученные модели, классификатор каскада хаара, временные данные
0. PATH_DATASET - пользовательская база данных хранятся фотографии пользователей
0. ID_CARARA - Номер камеры в операционной системе изначально 0

# Создание Сервиса в Systemd
0. Создать файл: sudo touch /etc/systemd/system/door_server.service
0. Меняем права: sudo chmod 664 /etc/systemd/system/foo-daemon.service
0. Пример формирования: rc/door_server.service
0. перезапустить systemD: sudo systemctl daemon-reload

## Установка:
0. Создать виртуальное окружения python3 -m venv door, активировать source door/bin/activate
0. pip install -r requirements.txt
0. Запуск: pyhton run_server.py

## Описание папок проекта
0. expirements - Тестовые файлы.
0. rs - ресурсы проекта (содержат обученные модели и классификатор для поискаа лиц).
0. modul - основные компоненты с которыми работает программа

## Схема взаимодействия модулей
![alt text](https://github.com/morgonxak/termoBox/blob/9_9_20/app_thermometer/rc/git/Schema.png)

## Пины для подключения:
## Свойство
## Реле
Пин |  GPIO pin | Board pin
------------ | ------------- | ------------- 
**+** | **18** | **12**
**-** | **GND** | **14**
## Кнопка
Пин |  GPIO pin | Board pin
------------ | ------------- | ------------- 
**+** | **4** | **7**
**-** | **GND** | **9**