
import bpy
from bpy.props import *


#
#    Menu in Tools region
#
class ToolsPanel(bpy.types.Panel):
    bl_label = "Hello from Toolsi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "bli"
    
    number = 1
    
    def draw(self, context):
        layout = self.layout
        
        split = layout.split()
        
        col = split.column()
        sub = col.column(align=True)
        
        rd = context.scene.render
        sub.prop(context.scene, "nbDupli", text="Number")
        
        col = split.column()
        sub = col.column(align=True)
        sub.operator("object.dupli_x")


class ObjectMoveX(bpy.types.Operator):
    """My Object Duplicate Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.dupli_x"        # unique identifier for buttons and menu items to reference.
    bl_label = "Duplicate"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False,
                                                           "mode": 'TRANSLATION'},
                                      TRANSFORM_OT_translate={"value": (3, 0, 0),
                                                              "constraint_axis": (True, False, False),
                                                              "constraint_orientation": 'GLOBAL',
                                                              "mirror": False,
                                                              "proportional": 'DISABLED',
                                                              "proportional_edit_falloff": 'SMOOTH',
                                                              "proportional_size": 1,
                                                              "snap": False,
                                                              "snap_target": 'CLOSEST',
                                                              "snap_point": (0, 0, 0),
                                                              "snap_align": False,
                                                              "snap_normal": (0, 0, 0),
                                                              "gpencil_strokes": False,
                                                              "texture_space": False,
                                                              "remove_on_cancel": False,
                                                              "release_confirm": False})

        return {'FINISHED'}            # this lets blender know the operator finished successfully.


bpy.types.Scene.nbDupli = IntProperty(name="Number",
                                      description="How many duplications",
                                      min=1, max=1000,
                                      default=2)
    

def register():
    bpy.utils.register_class(ToolsPanel)
    bpy.utils.register_class(ObjectMoveX)


def unregister():
    bpy.utils.unregister_class(ToolsPanel)
    bpy.utils.unregister_class(ObjectMoveX)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
