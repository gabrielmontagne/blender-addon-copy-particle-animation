from bpy.props import StringProperty, BoolProperty, IntVectorProperty, IntProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
import bpy

bl_info = {
    'name': 'Copy particle animation',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Copy and keyframe the position and rotation of particles onto selected objects',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-copy-particle-animation/issues'
}

size = 20

class ANIM_OP_copy_particle_animation(Operator):
    """Copy particle animation"""
    bl_idname = 'rojored.copy_particle_anim'
    bl_label = 'Copy particle animation'
    bl_options = {'UNDO', 'PRESET'}

    particle_indices: IntVectorProperty(name='particle indices', size=size, default=range(size))
    frame_start: IntProperty(name='start frame', default=1)
    frame_end: IntProperty(name='end frame', default=100)
    frame_step: IntProperty(name='frame step', default=1)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):

        scene = context.scene
        current_frame = scene.frame_current
        source_object = bpy.context.active_object
        target_objects = [o for o in bpy.context.selected_objects if o is not source_object]

        for frame in range(self.frame_start, self.frame_end, self.frame_step):

            scene.frame_set(frame)
            degp = bpy.context.evaluated_depsgraph_get()
            particle_system = source_object.evaluated_get(degp).particle_systems[0]
            particles = particle_system.particles

            for o, i in zip(target_objects, self.particle_indices):
                p = particles[i]

                o.location = p.location
                o.rotation_quaternion = p.rotation

                o.keyframe_insert('location')
                o.keyframe_insert('rotation_quaternion')
                o.rotation_mode = 'QUATERNION'

        scene.frame_set(current_frame)

        return {'FINISHED'}

def register():
    register_class(ANIM_OP_copy_particle_animation)

def unregister():
    unregister_class(ANIM_OP_copy_particle_animation)
