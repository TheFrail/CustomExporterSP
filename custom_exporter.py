# Painter API import
import substance_painter
import substance_painter_plugins

#3rd party UI lib import
from PySide6.QtWidgets import QWidget, QGridLayout, QCheckBox, QComboBox, QPushButton, QLabel
from PySide6 import QtCore

#Global variable
custom_exporter = None


class CustomExporter:
   def __init__(self):
      self.initialization()
    

   def initialization(self):
      self.init_widget_window()
      self.connect_slots()
      self.show_ui_widget()


   def init_widget_window(self):
      self.widget = QWidget() 
      self.widget.setObjectName("Custom Exporter")
      self.widget.setWindowTitle("Custom Exporter")   
      self.main_layout = QGridLayout(self.widget)

      # Personal Export checkbox
      self.personal_export_cb = QCheckBox("Personal Export")
      self.main_layout.addWidget(self.personal_export_cb)
      
      #Asset Type label
      self.asset_type_lbl = QLabel("Asset Type:")
      self.main_layout.addWidget(self.asset_type_lbl)
      
      # Asset Type Combo Box
      self.asset_type_cmbx = QComboBox()
      self.asset_type_cmbx.addItems(["Props", "Weapons", "Characters"])
      self.main_layout.addWidget(self.asset_type_cmbx)

      #Export Button 
      self.export_btn = QPushButton("Export")
      self.main_layout.addWidget(self.export_btn)


      #Test Button
      self.info_btn = QPushButton("Info")
      self.warning_btn = QPushButton("Warning")
      self.error_btn = QPushButton("Error")

      self.main_layout.addWidget(self.info_btn)
      self.main_layout.addWidget(self.warning_btn)
      self.main_layout.addWidget(self.error_btn)



   def connect_slots(self):
      self.export_btn.clicked.connect(self.on_export_requested)
      self.personal_export_cb.stateChanged.connect(self.on_toggle_personal_export)
      self.asset_type_cmbx.currentIndexChanged.connect(self.on_asset_type_chaged)

      self.info_btn.clicked.connect(self.on_info_clicked)
      self.warning_btn.clicked.connect(self.on_warning_clicked)
      self.error_btn.clicked.connect(self.on_error_clicked)

   def show_ui_widget(self):
      plugin = substance_painter_plugins.plugins.get("Custom Exporter", None)
      if plugin is not None:
         #Refresh widget
         self.delete_widget()
         self.init_widget_window()       

      substance_painter.ui.add_dock_widget(self.widget)
      self.widget.show()

   def delete_widget(self):
      if self.widget is not None:
         substance_painter.ui.delete_ui_element(self.widget)

   def on_export_requested(self):
      print("Export button clicked")

   def on_toggle_personal_export(self, state):
      check_state = QtCore.Qt.CheckState(state)

      if check_state == QtCore.Qt.CheckState.Checked:
        print("Personal Export checkbox is checked")
      else:
        print("Personal Export checkbox is unchecked")

   def on_asset_type_chaged(self, current_index):
      current_asset_type_text = self.asset_type_cmbx.itemText(current_index)
      print(f"asset Type has been changed. Now it's set to {current_asset_type_text}")

   def on_info_clicked(self):
      substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", "This is an Info log")

   def on_warning_clicked(self):
      substance_painter.logging.log(substance_painter.logging.WARNING, "Custom Exporter", "This is an Warning log")

   def on_error_clicked(self):
      substance_painter.logging.log(substance_painter.logging.ERROR, "Custom Exporter", "This is an Error log")





def start_plugin():
   global custom_exporter
   custom_exporter = CustomExporter()

def close_plugin():
   global custom_exporter
   custom_exporter.delete_widget()

   if __name__ == "__main__":
      start_plugin()
   