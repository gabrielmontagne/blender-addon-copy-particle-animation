from bpy.props import StringProperty, BoolProperty, IntVectorProperty, IntProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

bl_info = {
    'name': 'Copy particle animation',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Copy and keyframe the position and rotation of particles onto selected objects',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-copy-particle-animation/issues'
}

class ANIM_OP_copy_particle_animation(Operator):
    """Copy particle animation"""
    bl_idname = 'rojored.copy_particle_anim'
    bl_label = 'Copy particle animation'
    bl_options = {'UNDO', 'PRESET'}

    particle_indices: IntVectorProperty(name='particle indices', size=5, default=[0,1,2,3,4])
    start_frame: IntProperty(name='start frame', default=1)
    end_frame: IntProperty(name='end frame', default=100)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        print('copy particle animation')
        return {'FINISHED'}

def register():
    register_class(ANIM_OP_copy_particle_animation)

def unregister():
    unregister_class(ANIM_OP_copy_particle_animation)
