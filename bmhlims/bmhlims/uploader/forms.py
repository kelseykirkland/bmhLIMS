from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

class SSFileName(forms.Form):
    fname = forms.CharField(_)
