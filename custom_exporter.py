# Painter API import
import substance_painter

#3rd party UI lib import
from PySide6.QtWidgets import QWidget, QGridLayout, QCheckBox, QComboBox, QPushButton

#Global variable
custom_exporter = None


class CustomExporter:
   def __init__(self):
    self.widget = QWidget()
    self.widget.setWindowTitle("Custom Exporter")
    

    self.main_layout = QGridLayout(self.widget)

    # Personal Export checkbox
    self.personal_export_cb = QCheckBox("Personal Export")
    self.main_layout.addWidget(self.personal_export_cb)

    substance_painter.ui.add_dock_widget(self.widget)


   def delete_widget(self):
      if self.widget is not None:
         substance_painter.ui.delete_ui_element(self.widget)

def start_plugin():
   global custom_exporter
   custom_exporter = CustomExporter()

def close_plugin():
   global custom_exporter
   custom_exporter.delete_widget()

   if __name__ == "__main__":
      start_plugin()
   