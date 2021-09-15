def GetMemberId(name):
    ids = {
        "nic": "5f162c7700438007ea6cfd24",
        "nicolle": "5f162c7700438007ea6cfd24",
    }

    try:
        return (ids[name])
    except:
        return "error"
