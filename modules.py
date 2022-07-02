import requests
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import (
    TemplateView, ListView,
    DetailView, View
)
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from importlib import reload
from django.utils import timezone
from datetime import timedelta, datetime, date
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from django.core.files.storage import default_storage
from decimal import Decimal
from colorama import Fore, Back, Style
from base64 import b64encode
from django.contrib.sites.shortcuts import get_current_site
import uuid
import json
import re
import random
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import req

# write your code below
def get_uuid(stop, first3=''):
    num = uuid.uuid4().int
    num = str(num)[:stop]
    return f'{first3}{num}'
def get_hex_uuid(stop):
    num = uuid.uuid4().hex
    num = str(num)[:stop]
    return f'{num}'
def currency_formater(amount):
    amount = round(float(amount), 1)
    amount = '{:,}'.format(amount)
    return amount
def handle_payment_proof(instance, file=None, coin_txref=None):
    if file is not None:
        filename = file.name.replace(' ','_')
        print(f'checking fileName {filename}')
        if filename in [i.payment_proof.name for i in instance.objects.all()]:
            payment_proof = None
        else:
            payment_proof = instance.objects.create(payment_proof=file)
    else:
        if coin_txref in [i.coin_txref for i in instance.objects.all()]:
            payment_proof = None
        else:
            payment_proof = instance.objects.create(coin_txref=coin_txref)
    return payment_proof
def calculate_percent(percent, amount):
    return percent*amount/100
def write_text(file, texts):
    with open(file, 'w') as f:
        f.writelines('\n'.join(texts))
def model_datetime(datetime_obj):
    return datetime(
     datetime_obj.year,
     datetime_obj.month,
     datetime_obj.day,
     datetime_obj.hour,
     datetime_obj.minute,
     datetime_obj.second,
     )
def color(color, text='color added'):
    print(color, text)

def decode(item):
    jsonDec = json.decoder.JSONDecoder()
    return jsonDec.decode(item)

def save_image_from_url(model, image_url, proxies=None, verify=None):
    r = req.requests.get(
        url=image_url,
         proxies=proxies,
         verify=verify
         )
    req.urllibinsecure

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()
    model.image.save("image.jpg", File(img_temp), save=True)
    print('Image successfully saved')

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def clean_html(text, format, to='\n'):
    """Remove html tags from a string"""
    clean = re.compile(format)
    return re.sub(clean, to, text)

def check_even_numbers(num, list):
    for num in list:
    # check
        if num % 2 == 0:
            print(num, end=" ")

def read_sentences_from_file(path_to_file, one_sentence_per_line=True):
    lines = []
    with io.open(path_to_file, mode="r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                lines.append(line.strip())
