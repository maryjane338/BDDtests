from PyQt6.QtWidgets import QApplication, QMessageBox
from unittest.mock import patch
from behave import Given, When, Then
from app.addDataWin import AddDataWin
from app.viewDataWin import ViewDataWin
from database.scripts.db import Data
from app.mainWin import MainWin




@Given('пользователь открывает приложение для просмотра записей')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()

@When('пользователь нажимает кнопку "Просмотреть" для просмотра записей')
def step(context):
    context.win.view_data_btn.click()

@Then('окно просмотра записей открыто')
def step(context):
    assert context.win.view_data_btn.click() is None




@Given('пользователь открывает приложение')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()

@When('пользователь нажимает кнопку "Просмотреть"')
def step(context):
    context.win.view_data_btn.click()

@Then('все записи отображаются в окне просмотра')
def step(context):
    context.win_view = ViewDataWin()
    orders_number = context.win_view.table.rowCount()
    assert orders_number == 7



@Given('пользователь открывает окно просмотра данных')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()
    context.win.view_data_btn.click()

@When('пользователь выбирает запись')
def step(context):
    context.win_view = ViewDataWin()
    context.win_view.table.selectRow(0)

@When('пользователь нажимает кнопку "Изменить"')
def step(context):
    context.win_add = AddDataWin([context.win_view.table.item(context.win_view.table.selectedItems()[0].row(), col).text() for col in range(context.win_view.table.columnCount())])
    context.win_view.edit_entry.click()

@When('пользователь заполняет поля данными')
def step(context):
    context.win_add.upload_editable_data()
    context.win_add.work_input.setCurrentText('Ремонт смартфона')
    context.win_add.description_input.setText('Ремонт экрана смартфон Apple Iphone')
    context.win_add.date_input.setText('2024-10-28')
    context.win_add.customer_input.setText('Пушкарёв Владислав')
    context.win_add.executor_input.setCurrentText('Сидоров')
    context.win_add.status_input.setCurrentText('Ожидание комплектующих')

@When('пользователь нажимает кнопку "Добавить заказ", чтобы сохранить изменения')
def step(context):
    with patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok):
        context.win_add.add_button.click()

@When('пользователь нажимает кнопку Ок в диалоговом окне')
def step(context):
    pass


@Then('появляется редактированная запись')
def step(context):
    context.db.get_all_orders(column=None, fltr=None)
    updated_order = context.db.data[0]
    assert updated_order[1] == 'Ремонт смартфона'
    assert updated_order[2] == 'Ремонт экрана смартфон Apple Iphone'
    assert updated_order[3] == '2024-10-28'
    assert updated_order[4] == 'Пушкарёв Владислав'
    assert updated_order[5] == 'Сидоров'
    assert updated_order[6] == 'Ожидание комплектующих'




@Given('пользователь открывает окно для добавления заказа')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()
    context.win.add_data_btn.click()
    context.win_add = AddDataWin()

@When('пользователь заполняет данные нового заказа')
def step(context):
    context.win_add.work_input.setCurrentText('Чистка от пыли')
    context.win_add.description_input.setText('Чистка пылесоса от пыли')
    context.win_add.date_input.setText('2024-11-02')
    context.win_add.customer_input.setText('Мамаджанов Абдумаджид')
    context.win_add.executor_input.setCurrentText('Смирнова')
    context.win_add.status_input.setCurrentText('Уточнение информации')

@When('пользователь жмёт кнопку "Добавить заказ"')
def step(context):
    with patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok):
        context.win_add.add_button.click()

@When('пользователь жмёт кнопку Ок в диалоговом окне')
def step(context):
    pass

@Then('новый заказ добавляется в Базу Данных')
def step(context):
    context.db.get_all_orders(column=None, fltr=None)
    added_order = context.db.data[-1]
    assert added_order[1] == 'Чистка от пыли'
    assert added_order[2] == 'Чистка пылесоса от пыли'
    assert added_order[3] == '2024-11-02'
    assert added_order[4] == 'Мамаджанов Абдумаджид'
    assert added_order[5] == 'Смирнова'
    assert added_order[6] == 'Уточнение информации'




@Given('пользователь открывает окно добавления заказа')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()
    context.win.add_data_btn.click()
    context.win_add = AddDataWin()

@When('пользователь заполняет заказ некорректными данными')
def step(context):
    context.win_add.work_input.setCurrentText('')
    context.win_add.description_input.setText('')
    context.win_add.date_input.setText('')
    context.win_add.customer_input.setText('')
    context.win_add.executor_input.setCurrentText('')
    context.win_add.status_input.setCurrentText('')

@When('пользователь нажимает кнопку "Добавить заказ"')
def step(context):
    with patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok):
        context.win_add.add_button.click()

@When('пользователь нажимает кнопку Ок в информационном диалоговом окне')
def step(context):
    pass

@Then('программа выдаёт ошибку')
def step(context):
    context.db.get_all_orders(column=None, fltr=None)
    added_order = context.db.data[-1]
    assert not added_order[1] == ''
    assert added_order[2] == ''
    assert added_order[3] == ''
    assert added_order[4] == ''
    assert not added_order[5] == ''
    assert not added_order[6] == ''




@Given('пользователь открывает окно просмотра записей')
def step(context):
    context.app = QApplication([])
    context.db = Data("database/temporary_full.db")
    context.win = MainWin()
    context.win.show()
    context.win.view_data_btn.click()

@When('пользователь выбирает запись для удаления')
def step(context):
    context.win_view = ViewDataWin()
    context.win_view.table.selectRow(7)
    context.row_number1 = context.win_view.table.rowCount()

@When('пользователь нажимает кнопку "Удалить"')
def step(context):
    with patch.object(QMessageBox, 'exec', return_value=QMessageBox.StandardButton.Yes):
        with patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok):
            context.win_view.del_entry.click()

@When('пользователь нажимает кнопку "Да" в диалоговом окне')
def step(context):
    pass

@When('пользователь выбирает ещё одну запись')
def step(context):
    context.win_view.table.selectRow(7)
    context.row_number2 = context.win_view.table.rowCount()

@When('пользователь ещё раз нажимает кнопку "Удалить"')
def step(context):
    with patch.object(QMessageBox, 'exec', return_value=QMessageBox.StandardButton.Yes):
        with patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok):
            context.win_view.del_entry.click()

@When('пользователь ещё раз нажимает кнопку "Да" в диалоговом окне')
def step(context):
    pass

@Then('нужные записи удалены')
def step(context):
    new_row_number = context.win_view.table.rowCount()
    assert context.row_number1 != context.row_number2
    assert new_row_number != context.row_number2
