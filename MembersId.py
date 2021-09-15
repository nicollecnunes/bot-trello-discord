def GetMemberId(name):
    #ids do trello x nome da pessoa (cadastro)
    ids = {
        "nic": "5f162c7700438007ea6cfd24",
        "nicolle": "5f162c7700438007ea6cfd24",
        "yagami": "6111be461dd3b814d149c932",
        "bernardo": "6005c43f22e57e2aa1be37bc",
        "be": "6005c43f22e57e2aa1be37bc",
        "alex": "6111bd323cfb3d8f094f4319",
        "antonio": "6111bd323cfb3d8f094f4319",
        "ian": "6111e579361b382693bed48e",
        "mayan": "5f162915c054a565267ffbfb",
        "tutu": "5f162915c054a565267ffbfb"
    }

    try:
        return (ids[name])
    except:
        return "error"
