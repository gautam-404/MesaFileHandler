from MesaHandler.MesaProjHandler import ProjectOps
from MesaHandler import MesaAccess


work = ProjectOps()        ## Use ProjectOps("your_project") for a custom project name  
work.create()              ## Use boolean arguments 'overwrite' and 'clean' to work on existing projects

work.loadProjInlist("relative/path/to/inlist_custom_project")
# work.loadPGstarInlist("relative/path/to/inlist_custion_pgstar")

object = MesaAccess()
object["initial_mass"] = 5

work.make()
# work.run()
# work.rerun("x450")
# work.clean()              ## Clean the project