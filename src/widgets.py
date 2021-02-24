import sys
import string
from PyQt6.QtWidgets import QComboBox,QLabel,QMenu,QListView
from PyQt6.QtGui import QFont, QAction


class UpperComboBox(QComboBox):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("Upper_Combo_Box")
        self.addItems([i for i in string.ascii_uppercase])
        self.setFont(BoldFont())


class BoldFont(QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)


class WordLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("word_label")
        self.setText("Words")
        self.setFont(BoldFont())
        self.setIndent(8)


class MatchesLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("matches_label")
        self.setText("Matches")
        self.setFont(BoldFont())
        self.setIndent(8)


class TranslationLabel(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("translation_label")
        self.setText("Character Translation Table")
        self.setFont(BoldFont())
        self.setIndent(8)


class FileMenu(QMenu):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setTitle("File")
        exit_action = QAction(parent=self)
        exit_action.setText("Exit")
        clear_action = QAction(parent=self)
        clear_action.setText("Clear")
        self.addAction(exit_action)
        self.addAction(clear_action)
        exit_action.triggered.connect(self.destroy)
        clear_action.triggered.connect(self.clear)

    def destroy(self):
        sys.exit(self.parent.parent().app.exec)

    def clear(self):
        main_window = self.parent.parent()
        main_window.table.clear()
        main_window.old_list_view.clear()
        main_window.new_list_view.clear()
        main_window.text_browser.clear()


class WordList(QListView):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Word_List")
        self.parent =parent

class MatchesList(QListView):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Matches_List")
        self.parent =parent
