
bl_info = {
    "name": "Oblique Strategies",
    "blender": (2,80,0),
    "version": (0,1),
    "category":"System"
}

import bpy
from random import randrange

class OBLIQUE_OT_strategy(bpy.types.Operator):
    """
    the perl script was not working online so this is for that
    rtqe.net
    """

    bl_label = "oblique strategy"
    bl_idname = "oblique.strategy"
    bl_options = {"REGISTER"}

    result: bpy.props.StringProperty()

    def draw(self,context):
        self.layout.label(text=self.result)

    def invoke(self,context,event):
        data = None
        with open("deck.txt") as f:
            data = f.readlines()
        if not data:
            return {"CANCELLED"}
        self.result = data[randrange(len(data))].strip()

        context.window_manager.invoke_props_dialog(self)
        return {"RUNNING_MODAL"}

    def execute(self,context):
        print(self.result)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(OBLIQUE_OT_strategy)

def unregister():
    bpy.utils.unregister_class(OBLIQUE_OT_strategy)

