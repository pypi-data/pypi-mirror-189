# qafunnypet

### Install qafunnypet from PyPi.
```bash
pip install qafunnypet
```

#### Example
```python
  from qafunnypet import Qafunnypet

  class Dog(Qafunnypet):
      def __init__(self, name, age, color=None):
          super().__init__(name, age)
          self.color = color

      def present(self):
          if self.color is None:
              pass
          else:
              print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

      def speak(self):
          print("Bark")

>>> doggy = Dog("Tim", 15, "Bronw")
>>> doggy.present()
>>> doggy.speak()

>>> some = Qafunnypet("Cuasi", 10)
>>> some.present()
>>> some.speak()
```