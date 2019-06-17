import unreal
# Get Actor from the world
actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.SkeletalMeshActor)
print actor_list
# Get Sequencer
#sequence_asset = unreal.LevelSequence.cast(unreal.load_asset('/Game/shot'))
#print sequence_asset
level = unreal.EditorLevelLibrary.load_level("/Game/slicer")
print level
actorObj = unreal.load_asset('/Game/slicer/slicer_run')
actor = unreal.EditorLevelLibrary.spawn_actor_from_object(actorObj,(0,0,0))
print actor
green_material = unreal.EditorAssetLibrary.load_asset("/Game/slicer/Body_Material")
if green_material is None:
	print "The green material can't be loaded"
	quit()

widget_material = unreal.EditorAssetLibrary.load_asset("/Game/slicer/lambert2")
if widget_material is None:
	print "The grid material can't be loaded"
	quit()

unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors([actor], green_material, widget_material)
