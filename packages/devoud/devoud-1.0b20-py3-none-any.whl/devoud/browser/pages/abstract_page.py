from devoud.browser.pages import *
from devoud.browser.web.view import BrowserWebView
from devoud.browser.web.search_engines import search_engines


class AbstractPage(QWidget):
    def __init__(self, parent=None, url=None, title=None):
        super().__init__(parent)
        self.setObjectName('abstract_page')
        self.tab_widget = parent
        self.FS = self.window().FS
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.setFixedHeight(4)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.layout().addWidget(self.progress_bar, 0, 0)

        self.view_spliter = QSplitter(Qt.Vertical)
        self.layout().addWidget(self.view_spliter, 1, 0)
        self.popup_link = None

        self.url = url
        self.title = title
        self.view = None

    def data(self) -> dict:
        return {'url': self.url,
                'title': self.title,
                'type': url_type(self.url)}

    def create_web_view(self):
        if self.view is not None:
            self.view.deleteLater()
        self.view = BrowserWebView(self)
        self.view.titleChanged.connect(self.update_title)
        self.view.page().urlChanged.connect(self.url_changed)
        self.view.settings().setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
        self.view.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.view.setAttribute(Qt.WA_DeleteOnClose)
        self.view.page().fullScreenRequested.connect(self.FullscreenRequest)
        self.view.loadStarted.connect(self.loadStartedHandler)
        self.view.loadProgress.connect(self.loadProgressHandler)
        self.view.loadFinished.connect(self.loadFinishedHandler)
        self.view.page().linkHovered.connect(self.show_hovered_link)
        self.view_spliter.addWidget(self.view)
        self.popup_link = QLabel(self)
        self.popup_link.setObjectName('popup_link')
        self.popup_link.setMinimumWidth(0)
        self.popup_link.setMaximumWidth(16777215)
        self.popup_link.setText(' ')
        self.layout().addWidget(self.popup_link, 1, 0, 1, 2, Qt.AlignLeft | Qt.AlignBottom)

    @Slot(str)
    def show_hovered_link(self, url):
        if url == '':
            self.popup_link.setText('')
        else:
            self.popup_link.setText(f' {url} ')

    def create_embedded_view(self, url='devoud://void'):
        print(f'[Страница]: Открытие встроенной страницы ({url})')
        if self.view is not None:
            self.view.deleteLater()
        self.view = embedded_pages.get(url, NotFoundPage)(self)
        if self.FS.get_option('saveHistory'):
            self.window().history.append(self.data())
        self.view.setAttribute(Qt.WA_DeleteOnClose)  # ?
        self.view_spliter.addWidget(self.view)

    def load(self, url: str = None, allow_search=False):
        if url is None:
            if self.url is not None:
                url = self.url
            else:
                url = VoidPage.url

        url = redirects.get(url, url)  # если редирект не найден, то значение остается
        self.url = url

        if is_url(url):
            # если это ссылка, то блокируем поиск
            allow_search = False

        formatted_url = QUrl.fromUserInput(url).toString()
        if url_type(url) is BrowserWebView:
            self.create_web_view()
            if allow_search:
                # при разрешении вставляем текст в поисковый движок
                self.view.load(f'{search_engines[self.window().address_panel.search_box.currentText()][0]}{url}')
            else:
                self.view.load(formatted_url)
        else:
            self.create_embedded_view(url)

        self.update_title(self.view.title)

    def stop(self):
        self.view.stop()

    def reload(self):
        self.view.reload()

    def back(self):
        self.view.back()

    def forward(self):
        self.view.forward()

    def url_changed(self, url):
        if isinstance(url, QUrl):
            self.url = url.toString()
        if self.tab_widget.currentWidget() == self:
            self.window().address_line_edit.setText(self.url)
            self.window().address_line_edit.setCursorPosition(0)
            self.window().address_panel.update_bookmark_button(self.url)

    @Slot(str)
    def update_title(self, title):
        self.title = title
        index = self.tab_widget.indexOf(self)
        self.tab_widget.setTabText(index, title)
        if self.tab_widget.currentWidget() == self:
            self.window().set_title(title)

    def is_loading(self):
        return False if self.view is None else self.view.is_loading()

    @Slot("QWebEngineFullScreenRequest")
    def FullscreenRequest(self, request):
        request.accept()
        if request.toggleOn():
            self.view.setParent(None)
            self.view.showFullScreen()
        else:
            self.layout().addWidget(self.view)
            self.view.showNormal()

    @Slot()
    def loadStartedHandler(self):
        if self.isVisible():
            self.window().address_panel.show_update_button(False)
        print(f"[Страница]: Начата загрузка страницы ({self.url})")

    @Slot(int)
    def loadProgressHandler(self, progress):
        if self.isVisible():
            self.window().address_panel.show_update_button(False)
        self.progress_bar.setValue(progress)
        print(f"[Страница]: {progress}% ({self.url})")

    @Slot()
    def loadFinishedHandler(self):
        if self.FS.get_option('saveHistory'):
            self.window().history.append(self.data())
        if self.isVisible():
            self.window().address_panel.show_update_button(True)
        self.progress_bar.setValue(0)
        print(f"[Страница]: Страница загружена ({self.url})")
