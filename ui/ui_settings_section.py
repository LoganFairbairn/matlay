import bpy
from . import ui_section_tabs

def draw_ui_settings_section(self, context):
    ui_section_tabs.draw_section_tabs(self, context)

    # Render engine so users can swap through the interface.
    layout = self.layout
    scale_y = 1.4
    row = layout.row()
    row.scale_y = scale_y
    row.operator("matlay.append_workspace", icon='IMPORT')

    row = layout.row()
    row.scale_y = scale_y
    row.prop(bpy.context.scene.render, 'engine')
