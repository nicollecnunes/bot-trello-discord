def GetName(ctx):
    #pega o nome do autor que mandou a mensagem no discord
    name = str({ctx.author}) + ""
    name = name.split("'")
    return name[1]