#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from .classes import MartServer


def list_marts():
    server = MartServer()
    return server.list_marts()
