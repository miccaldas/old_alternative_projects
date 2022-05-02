"""Module Docstring"""
from loguru import logger
from django import forms

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


class SearchForm(forms.Form):
    query = forms.CharField()
