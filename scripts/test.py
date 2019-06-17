# -*- coding: utf-8 -*-
import unreal
unreal.log(unreal)


baseurl = "E:/savvy/unreal_scripts/assets/" 
sound_wav =baseurl + "test.mp3"

def importMyAssets():
    sound_task = buildImportTask(sound_wav, "/Game/Sounds")
    executeImportTasks([sound_task])

def buildImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property("automated", True)
    task.set_editor_property("destination_name", "QIU")
    task.set_editor_property("destination_path", destination_path)
    task.set_editor_property("filename", filename)
    task.set_editor_property("replace_existing", False)
    task.set_editor_property("save", True)
    return task

def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

importMyAssets()


