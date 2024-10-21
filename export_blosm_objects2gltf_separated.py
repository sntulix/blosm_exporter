"""
export_blosm_objects2gltf_separated.py.
This script exports the city map loaded in Blosm as individual objects to gltf.
And create modelfile list.
# for Blender v3 LTS later
Date: 20231009
Update: 20241021
"""

import os
import bpy
from math import degrees

exclude_names="Cube Cube2 "
save_dir = os.path.expanduser("~/") + "Downloads/tmp/"
list_filename = "modellist.tsv"
listfile_path = save_dir + list_filename

def writeList(listfile_path, obj):
    obj.select_set(True)
    rot = obj.rotation_euler

    f = open(listfile_path, "a")
    f.write(obj.name + "\t"
        + str(obj.location[0]) + "\t" + str(obj.location[1]) + "\t" + str(obj.location[2]) + "\t"
        + str(degrees(rot[0])) + "\t" + str(degrees(rot[1])) + "\t" + str(degrees(rot[2])) + "\t"
        + str(obj.scale[0]) + "\t" + str(obj.scale[1]) + "\t" + str(obj.scale[2]) + "\t"
        + str(obj.dimensions[0]) + "\t" + str(obj.dimensions[1]) + "\t" + str(obj.dimensions[2])
        +"\n"
    )
    f.close()


def exportMesh(save_path, obj):
    ## set to origin (0,0,0) temporary.
    tmp_loc = obj.location[::]
    obj.location[0] = 0
    obj.location[1] = 0
    obj.location[2] = 0
    ## export
    bpy.ops.export_scene.gltf(filepath=save_path,
        export_current_frame=True,
        export_format='GLTF_EMBEDDED',
        export_image_format='JPEG',
        export_jpeg_quality=80,
        use_selection=True)
    ## restore location
    obj.location = tmp_loc


def export_active_object2glb(save_dir, listfile_path, obj, exclude_names=""):
    exclude_flag = False
    if exclude_names!="":
        exclude_list = exclude_names.split(' ')
        for ex_key in exclude_list:
            if ex_key != '' and ex_key in obj.name:
                exclude_flag = True

    if exclude_flag==False:
        # init file name
        save_filename = obj.name+".glb"
        save_path = save_dir + save_filename
        print(save_filename)

        # write data to the list.
        writeList(listfile_path, obj)

        # export mesh
        exportMesh(save_path, obj)


# delete old list.
if os.path.exists(listfile_path):
    os.remove(listfile_path)

# pickup MESHs only
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        bpy.ops.object.select_all(action='DESELECT')
        export_active_object2glb(save_dir, listfile_path, obj, exclude_names)
