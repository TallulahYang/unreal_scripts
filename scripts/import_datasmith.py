import unreal

help(unreal.DatasmithScene)



baseurl = "E:/savvy/unreal_scripts/assets/" 
# Add proper file directory and open a udatasmith scene
datasmith_file =baseurl +  "slicer/PythonExample.udatasmith"
datasmith_scene = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(datasmith_file)


# check scene initialization
if datasmith_scene is None:
	print "LoadDatasmith Failed"
	quit()

#
# ** pre import **
# change the actor "Ceramic_Ceramic_Peach"'s layer
actor_label = "Teapot001"
for actor in datasmith_scene.get_all_mesh_actors():
    if actor.get_label() == actor_label:
		actor.set_layer("Teapot001")

#
# ** import **
# set the option on how to import the datasmith scene
option = unreal.DatasmithImportBaseOptions()

# import into a new level
# (since we import into a new level, you can't use Blutility because the Blutility actor will be destroyed at the creation of the new level)
option.scene_handling = unreal.DatasmithImportScene.NEW_LEVEL

# import datasmith scene in Unreal
destination_folder = "/Game/PythonExample"
result = datasmith_scene.import_scene(destination_folder, option)

if not result.import_succeed:
	print "Import Failed"
	quit()

# 
# ** post import **
# load materials
green_material = unreal.EditorAssetLibrary.load_asset("/Game/PythonExample/PythonExample/Materials/01_-_Default")
if green_material is None:
	print "The green material can't be loaded"
	quit()

widget_material = unreal.EditorAssetLibrary.load_asset("/Engine/EditorMaterials/WidgetMaterial_X.WidgetMaterial_X")
if widget_material is None:
	print "The grid material can't be loaded"
	quit()

# find all StaticMesh Actor in the Level and where the StaticMeshComponent point to the green material replace it by the grid material.
actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.StaticMeshActor)
unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors(actor_list, green_material, widget_material)
