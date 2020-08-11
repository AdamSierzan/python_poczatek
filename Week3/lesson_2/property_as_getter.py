# Getter zwraca wartość pola prywatnego
# Jeżeli stworzyliśmy pole prywatne do którego
# chcemy zachować brak dostępu w celu edycji,
# ale jednocześnie chcemy dać możliwość "zobaczenia" 
# go bez opcji edycji, używamy gettera.

# Class Student:
#     def__init__(self):
#     self._final_grades = []

#     def get_final_grades(self):
#         return self._final_grades

# student = Student()
# print(student.get_final_grades())

# Gettera można ulepszyć poprzez dodanie property

# Class Student:
#     def__init__(self):
#     self._final_grades = []

    # @property
#     def get_final_grades(self):
#         return self._final_grades

# student = Student()
# print(student.get_final_grades())
