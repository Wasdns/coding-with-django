from flask import Markup, url_for, g
from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Float, Text
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction

class College(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Major(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class MClass(Model):
    __tablename__ = 'mclass'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Teacher(Model):
    id = Column(Integer, primary_key=True)
    work_num = Column(String(30), unique=True, nullable=False) 
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False) 
    college = relationship("College")
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False) 
    department = relationship("Department")
    tel_num = Column(String(30), unique=True, nullable=False) 
    birthday = Column(Date)

    def __repr__(self):
        return self.name

assoc_teacher_student = Table('teacher_student', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('teacher_id', Integer, ForeignKey('teacher.id')),
                                      Column('student_id', Integer, ForeignKey('student.id'))
)

class Student(Model):
    id = Column(Integer, primary_key=True)
    stu_num = Column(String(30), unique=True, nullable=False) 
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)
    college = relationship("College")
    major_id = Column(Integer, ForeignKey('major.id'), nullable=False)
    major = relationship("Major")
    mclass_id = Column(Integer, ForeignKey('mclass.id'), nullable=False)
    mclass = relationship("MClass")
    teachers = relationship('Teacher', secondary=assoc_teacher_student, backref='student')
    tel_num = Column(String(30), unique=True, nullable=False) 
    birthday = Column(Date)

    def __repr__(self):
        return self.name

