##选项1：完整编辑器

###在该方法中，会启动完整虚幻编辑器，打开指定的项目，加载默认的启动关卡，然后在一切都加载就绪后立即运行Python脚本。需要让脚本与项目中或关卡中加载用时可能较长的内容交互时，该方法非常有用。在命令行中添加ExecutePythonScript参数，并将其值设置为要运行的Python脚本。例如：

` UE4Editor-Cmd.exe MyProject.uproject -ExecutePythonScript="c:\my_script.py" `


##选项2：命令行开关

###在该方法中，编辑器启动时环境最小，不包含UI或渲染。该方法执行起来非常快，但是加载脚本需要交互的关卡和其他种类资源时比较棘手。在命令行中添加以下参数：-run=pythonscript -script=<script_file>

`> UE4Editor-Cmd.exe -run=pythonscript -script="c:\\my_script.py"`