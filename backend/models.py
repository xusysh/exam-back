# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserList(models.Model):
  username = models.CharField(max_length = 20, unique = True)
  password = models.CharField(max_length = 20)
  usertype = models.CharField(max_length = 20)
