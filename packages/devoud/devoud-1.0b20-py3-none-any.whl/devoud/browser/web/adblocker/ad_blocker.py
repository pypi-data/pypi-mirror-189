from braveblock import braveblock
from devoud.browser import *


class AdBlocker(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.rules = None
        self.interceptor = None

    def is_enable(self):
        return self.parent().FS.get_option('easyprivacy') or self.parent().FS.get_option('easylist')

    def add_rules(self, other_rules: list = None):
        rules = []
        if other_rules is not None:
            rules.extend(other_rules)
            print(f"[Блокировка]: Добавлены сторонние правила")
        if self.parent().FS.get_option('easyprivacy'):
            with open("./browser/web/adblocker/rules/easyprivacy.txt", encoding='utf-8') as file:
                rules.extend(file.readlines())
                print(f"[Блокировка]: Добавлены правила EasyPrivacy")
        if self.parent().FS.get_option('easylist'):
            with open("./browser/web/adblocker/rules/easylist.txt", encoding='utf-8') as file:
                rules.extend(file.readlines())
                print(f"[Блокировка]: Добавлены правила EasyList")
        self.rules = braveblock.Adblocker(rules=rules)


class RequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, rules):
        super().__init__()
        self.rules = rules
        self.resources_types = {QWebEngineUrlRequestInfo.ResourceType.ResourceTypeImage: 'image',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeScript: 'script',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeSubFrame: 'sub_frame',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeMainFrame: 'main_frame',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeMedia: 'media',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeWebSocket: 'websocket',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeStylesheet: 'stylesheet',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeCspReport: 'csp_report',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeFontResource: 'font',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypePing: 'ping',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeXhr: 'xhr',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeObject: 'object',
                                QWebEngineUrlRequestInfo.ResourceType.ResourceTypeUnknown: 'other'
                                }

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        source = info.firstPartyUrl().toString()
        resource_type = self.resources_types.get(info.resourceType(), 'other')
        if self.rules.check_network_urls(url, source, resource_type):
            print(f"[Блокировка]: {resource_type} ({url})")
            info.block(True)
