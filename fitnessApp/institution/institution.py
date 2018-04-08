from abc import ABCMeta, abstractmethod


class AbstractInstitution(object):

    __metaclass__ = ABCMeta

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def institution_name(self):
        return self.name

    @property
    def category(self):
        return self._category   

    @category.setter
    def category(self, ctype):
        self._category = ctype

    @abstractmethod
    def institution_category(self):
        return self.category

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @abstractmethod
    def institution_location(self):
        return self.location

    @abstractmethod
    def contact_information(self):
        pass

    @abstractmethod
    def operation_information(self):
        pass