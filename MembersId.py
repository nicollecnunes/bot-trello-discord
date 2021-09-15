def GetMemberId(name):
    #ids do trello x nome da pessoa (cadastro)
    ids = {
        "nic": "5f162c7700438007ea6cfd24",
        "nicolle": "5f162c7700438007ea6cfd24",
    }

    try:
        return (ids[name])
    except:
        return "error"
