from devoud.browser import *


class Session(QObject):
    def __init__(self, parent):
        super().__init__(parent)

    def restore(self):
        if self.parent().FS.get_option('restoreTabs'):
            with Path(self.parent().FS.config_dir(), 'tabs.csv').open(newline='') as tabs_file:
                try:
                    tabs = list(csv.reader(tabs_file))
                    if not tabs:
                        return self.parent().load_home_page()
                    self.parent().tab_widget.currentChanged.disconnect()
                    for tab in range(len(tabs) - 1):
                        self.parent().tab_widget.create_tab(title=tabs[tab][0], url=tabs[tab][1], switch=False, load=False)
                    self.parent().tab_widget.setCurrentIndex(int(tabs[-1][0]))  # последняя посещенная вкладка
                    self.parent().tab_widget.current().load()
                    self.parent().tab_widget.currentChanged.connect(self.parent().tab_widget.tab_changed)
                    print('[Вкладки]: Предыдущая сессия восстановлена')
                except Exception as read_error:
                    print(f'[Вкладки]: Произошла ошибка при чтении файла, ошибка: {read_error}')
                    self.parent().load_home_page()
        else:
            self.parent().load_home_page()

    def save(self) -> None:
        if self.parent().FS.get_option('restoreTabs'):
            with Path(self.parent().FS.config_dir(), 'tabs.csv').open('w', newline='') as tabs_file:
                tabs = []
                for tab_index in range(self.parent().tab_widget.count()):
                    page = self.parent().tab_widget.widget(tab_index)
                    tabs.append([page.title, page.url])
                tabs.append(str(self.parent().tab_widget.currentIndex()))  # последняя посещенная вкладка
                writer = csv.writer(tabs_file)
                writer.writerows(tabs)
                print('[Вкладки]: Текущая сессия сохранена')
