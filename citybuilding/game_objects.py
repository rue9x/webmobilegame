
class LandPlot():
    def __init__(self):
        self.id = id
        self.locked = locked

class LandBuilding():
    def __init__(self):
        self.id = id
        self.level = level
        self.build_cooldown = build_cooldown
        self.upgrade_cost = 4.99
        
class InnBuilding(LandBuilding):
    def __init__(self):
        self.options = ["View Announcements", "Check Mailbox", "Hire Heroes with Renown", "Hire Heroes with Cash"]
        self.build_cooldown = 0

class BlacksmithBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Updgrade Weapon", "Upgrade building using Cash"]
        self.build_cooldown = 60

class ArmorsmithBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Updgrade Armor", "Upgrade building using Cash"]
        self.build_cooldown = 60

class GoldMineBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Check Production", "Upgrade building using Cash"]
        self.build_cooldown = 3600 # 1 hour to build

class NecropolisBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Protect Hero from Death", "Upgrade building using Cash"]
        self.build_cooldown = 21600 # 6 hour to build

class BarracksBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Store Heroes", "Upgrade building using Cash"]
        self.build_cooldown = 21600 # 6 hour to build

class SacraficialPitBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Hire Cultist", "Upgrade building using Cash"]
        self.build_cooldown = 10800 # 3 hour to build

class CastleBuilding(LandBuilding):
    def __init__(self):
        self.options = ["Hire Knight", "Upgrade building using Cash"]
        self.build_cooldown = 10800 # 3 hour to build

