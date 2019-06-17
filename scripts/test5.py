import unreal
 
 @unreal.uclass()
 class MyEditorUtility(unreal.GlobalEditorUtilityBase):
     pass
 
 editor_util = MyEditorUtility()
 print dir(editor_util)
 for sq in editor_util.get_selected_assets():
     print sq
     prange = sq.get_playback_range()
     print prange