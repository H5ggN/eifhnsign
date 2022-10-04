# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
from kivy.clock import Clock
 
class Sits(Label):
   def __init__(self, total, **kwargs):
       self.current = 0
       self.total = total
       my_text = "РћСЃС‚Р°Р»РѕСЃСЊ РїСЂРёСЃРµРґР°РЅРёР№: " + str(self.total)
       super().__init__(text=my_text, **kwargs)
 
   def next(self, *args):
       self.current += 1
       remain = max(0, self.total - self.current)
       my_text = "РћСЃС‚Р°Р»РѕСЃСЊ РїСЂРёСЃРµРґР°РЅРёР№: " + str(remain)
       self.text=my_text
