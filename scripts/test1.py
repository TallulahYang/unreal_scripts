# -*- coding: utf-8 -*-
import unreal
baseurl = "E:/savvy/unreal_scripts/assets/" 
asset_path = '/Game/Slicer'
unreal.EditorAssetLibrary.make_directory(asset_path)
 
#now we make an import task and access it's options, which are similar to the import UI
task = unreal.AssetImportTask()
 
#now let's set some import options on the task class
task.filename = baseurl + 'Slicer/slicer.fbx'
task.destination_path = asset_path
task.destination_name = 'slicer_run'
task.replace_existing = True
task.automated = True
#save the file when it is imported, that's right!
task.save = True

task.options = unreal.FbxImportUI() 
task.options.import_as_skeletal = True
task.options.override_full_name = True
task.options.mesh_type_to_import = unreal.FBXImportType.FBXIT_SKELETAL_MESH
 
task.options.skeletal_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)
task.options.skeletal_mesh_import_data.set_editor_property('use_t0_as_ref_pose', True)
task.options.skeletal_mesh_import_data.set_editor_property('preserve_smoothing_groups', 1)
task.options.skeletal_mesh_import_data.set_editor_property('import_meshes_in_bone_hierarchy', False)
task.options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
task.options.skeletal_mesh_import_data.set_editor_property('threshold_position',  0.00002)
task.options.skeletal_mesh_import_data.set_editor_property('threshold_tangent_normal', 0.00002)
task.options.skeletal_mesh_import_data.set_editor_property('threshold_uv', 0.000977)
task.options.create_physics_asset = False
task.options.import_animations = False
task.options.skeletal_mesh_import_data.set_editor_property('convert_scene', True)
task.options.skeletal_mesh_import_data.set_editor_property('force_front_x_axis', False)
task.options.skeletal_mesh_import_data.set_editor_property('convert_scene_unit', False)

normal_import_method = unreal.FBXNormalImportMethod.FBXNIM_IMPORT_NORMALS_AND_TANGENTS
normal_generation_method = unreal.FBXNormalGenerationMethod.MIKK_T_SPACE
 
task.options.skeletal_mesh_import_data.set_editor_property('normal_generation_method', normal_generation_method)
task.options.skeletal_mesh_import_data.set_editor_property('normal_import_method', normal_import_method)

imported_asset = unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
#let's check what files were imported/created:
imported_skelmesh = task.imported_object_paths