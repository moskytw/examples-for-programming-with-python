#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_employee.py

class Employee(object):

    # use `weakref` will be better
    employees = set()

    def __init__(self, name, title, id=None):

        self.name = name
        self.title = title
        self.__class__.employees.add(self)

        if id is None:
            self._id = len(self.employees)
        else:
            self._id = id

    def get_namecard(self):
        return '{0.title} {0.name}'.format(self)

    def fire(self):
        self.__class__.employees.remove(self)
        print 'DEBUG: I am fired. (name: %s)' % self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Employee({0.name}, {0.title}, {0._id})'.format(self)

    @property
    def id(self):
        return self._id

    @classmethod
    def fire_all(cls):
        for employee in cls.employees.copy():
            employee.fire()

if __name__ == '__main__':

    andy = Employee('Andy', 'Sales')
    bob = Employee('Bob', 'Engineer')

    print andy
    print bob
    print

    print andy.id, andy.name, andy.title
    print [getattr(bob, attr_name) for attr_name in ('id', 'name', 'title')]
    print

    print andy.get_namecard()
    print bob.get_namecard()
    print

    print Employee.employees
    print

    Employee.fire_all()
