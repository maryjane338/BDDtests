#language: ru
Функционал: Тестирование Базы Данных


  Сценарий: Тест открытия окна просмотра
    Дано пользователь открывает приложение
    Когда пользователь нажимает кнопку "Просмотреть"
    То окно просмотра записей открыто


  Сценарий: Отображение записей в окне просмотра данных
    Дано пользователь открывает приложение для просмотра записей
    Когда пользователь нажимает кнопку "Просмотреть" для просмотра записей
    То все записи отображаются в окне просмотра


  Сценарий: Редактирование записи
    Дано пользователь открывает окно просмотра данных
    Когда пользователь выбирает запись
    И пользователь нажимает кнопку "Изменить"
    И пользователь заполняет поля данными
    И пользователь нажимает кнопку "Добавить запись"
    И пользователь нажимает кнопку Ок в диалоговом окне
    То появляется редактированная запись


  Сценарий: Добавление заказа
    Дано пользователь открывает окно для добавления заказа
    Когда  пользователь заполняет данные нового заказа
    И пользователь жмёт кнопку "Добавить заказ"
    То новый заказ добавляется в Базу Данных


  Сценарий: Добавление некорректных данных
    Дано пользователь открывает окно добавления заказа
    Когда пользователь заполняет заказ некорректными данными
    И пользователь нажимает кнопку "Добавить заказ"
    То программа выдаёт ошибку


  Сценарий: Удаление записей
    Дано пользователь открывает окно просмотра записей
    Когда пользователь выбирает запись для удаления
    И пользователь нажимает кнопку "Удалить"
    И пользователь нажимает кнопку "Да" в диалоговом окне
    И пользователь выбирает ещё одну запись
    И пользователь ещё раз нажимает кнопку "Удалить"
    И пользователь ещё раз нажимает кнопку "Да" в диалоговом окне
    То нужные записи удалены
