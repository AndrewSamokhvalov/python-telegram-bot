__author__ = 'andrey.samokhvalov21@yandex.ru'

from config import *
import requests

from telegram import TelegramError


class AdServer:
    def __init__(self, token, ssp_host=SSP_HOST, ssp_port=SSP_PORT):
        self.token = token
        self.ssp_url = "http://%s:%s" % (ssp_host, ssp_port)

        settings = self.getSettings()
        if settings is not None:
            self.frequency = settings['frequency']

    def getSettings(self):
        url = "%s/%s" % (self.ssp_url, 'settings')

        payload = {
            "token": self.token
        }

        r = requests.get(url, data=payload)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            raise TelegramError('Can\'t initialize advertisement server')

    def getAd(self):
        url = "%s/%s" % (self.ssp_url, 'ad')

        payload = {
            "token": self.token
        }

        r = requests.post(url, data=payload)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            raise TelegramError('Can\'t get advertisement from SSP')


