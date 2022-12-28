class Public_Sample_AccessModifier:


publicObj=Public_Sample_AccessModifier("Python",6)
publicObj.display_Public_class_method()

class protected_sample_class:
    _tutor=None
    _place=None
    _experience=None

    def __init__(self,tutor,place,experience):
        self._tutor=tutor
        self._place=place
        self._experience=experience
    def _displayTutorDetails(self):
        print("Tutor: {} - place: {} - Experience: {}".format(self._tutor,self._place,self._experience))

class Derived_Protected_Class(Protected_Sample_class):
    def display_protected_method_variables(self):
        self._displayTutorDetails()
class Non_Derived_Class(Derived_Protected_Class):
    def