def GetName(ctx):
    name = str({ctx.author}) + ""
    name = name.split("'")
    return name[1]