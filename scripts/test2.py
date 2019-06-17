from os import listdir
from os.path import isfile, join
import unreal

baseurl = "E:/savvy/unreal_scripts/assets/" 
dir =baseurl + "Slicer/Textures"
files = [f for f in listdir(dir) if isfile(join(dir, f))]
AssetTools = unreal.AssetToolsHelpers.get_asset_tools()

import_tasks = []
for f in files:
     print join(dir, f)
     AssetImportTask = unreal.AssetImportTask()
     AssetImportTask.set_editor_property('filename', join(dir, f))
     AssetImportTask.set_editor_property('destination_path', '/Game/Slicer/Textures')
     AssetImportTask.set_editor_property('save', True)
     import_tasks.append(AssetImportTask)

AssetTools.import_asset_tasks(import_tasks)



