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
      self.connect_widget_events()
      self.connect_painter_events()
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

   def connect_widget_events(self):
      self.export_btn.clicked.connect(self.on_export_requested)
      self.personal_export_cb.stateChanged.connect(self.on_toggle_personal_export)
      self.asset_type_cmbx.currentIndexChanged.connect(self.on_asset_type_chaged)


   def connect_painter_events(self):
      painter_connections = {
         substance_painter.event.ProjectOpened : self.on_project_opened,
         substance_painter.event.ProjectCreated : self.on_project_created,
      }

      for event, callback in painter_connections.items():
         substance_painter.event.DISPATCHER.connect(event, callback) 

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
      substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", "Export button clicked")

   def on_toggle_personal_export(self, state):
      check_state = QtCore.Qt.CheckState(state)

      if check_state == QtCore.Qt.CheckState.Checked:
        
        substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", "Personal Export checkbox is checked")
   
      else:
        substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", "Personal Export checkbox is unchecked")

   def on_asset_type_chaged(self, current_index):
      current_asset_type_text = self.asset_type_cmbx.itemText(current_index)
      substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", f"asset Type has been changed. Now it's set to {current_asset_type_text}")
      

   def on_project_opened(self, e):
      substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", f"Project {substance_painter.project.name()} opened")

   def on_project_created(self, e):
      substance_painter.logging.log(substance_painter.logging.INFO, "Custom Exporter", "Project is created")



def start_plugin():
   global custom_exporter
   custom_exporter = CustomExporter()

def close_plugin():
   global custom_exporter
   custom_exporter.delete_widget()

   if __name__ == "__main__":
      start_plugin()
   