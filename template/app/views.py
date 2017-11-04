from flask import render_template, flash
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView, MultipleView, MasterDetailView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from flask_appbuilder.charts.views import DirectByChartView

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask_appbuilder.widgets import ListThumbnail
from .models import College, Department, Major, MClass, Teacher, Student
from flask_appbuilder.actions import action
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget

class CollegeView(ModelView):
    datamodel = SQLAInterface(College)

class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)

class MajorView(ModelView):
    datamodel = SQLAInterface(Major)

class MClassView(ModelView):
    datamodel = SQLAInterface(MClass)

class TeacherView(ModelView):
    datamodel = SQLAInterface(Teacher)

class StudentView(ModelView):
    datamodel = SQLAInterface(Student)

db.create_all()

appbuilder.add_view(CollegeView, "College", icon="gear", category='School Manage',)
appbuilder.add_view(DepartmentView, "Department", icon="gear",category='School Manage')
appbuilder.add_view(MajorView, "Major", icon="gear", category='School Manage')
appbuilder.add_view(MClassView, "MClass", icon="gear", category='School Manage')
appbuilder.add_view(TeacherView, "Teacher", icon="gear",category='School Manage')
appbuilder.add_view(StudentView, "Student", icon="gear",category='School Manage')