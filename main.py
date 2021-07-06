from kivy.app import App
from kivy.uix.button import Button  ##Импортирую кнопки

from kivy.config import Config

Config.set('graphics','resizable','0')#Не даем менять размер окна
Config.set('graphics','width','640')#Задаем ширину(width)
Config.set('graphics','height','480')#Задаем высоту(height)

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):

        fl = FloatLayout(size = (300,300))
        fl.add_widget(Button(text = "Первая кнопка", #Возвращаю кнопку, добавляю текст
                      font_size = 15,   #Изменяю размер шрифта
                      on_press = self.btn_press,    #Вызываю функцию, которая будет срабатывать при нажатии
                      background_color = [1, 0, 0, 1], #Меняю цвет кнопки
                      background_normal = "",##Цвет по умолчанию пустой)
                      size_hint = (.5,.25),#Задаем размеры кнопки
                      pos = (0,0)));#Задаем координаты кнопки
        return fl
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Я нажата"#Меняем текст последнего нажатого экземпляра(кнопки)
if __name__ == '__main__':  ## запускаем приложение
    MyApp().run()