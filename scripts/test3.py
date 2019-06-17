import unreal

material_factory = unreal.MaterialFactoryNew()

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
my_new_asset = asset_tools.create_asset('Blades_Material', "/Game/Slicer/", None, material_factory)
my_new_asset = asset_tools.create_asset('Body_Material', "/Game/Slicer/", None, material_factory)

unreal.EditorAssetLibrary.save_loaded_asset(my_new_asset)
