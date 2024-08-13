
##:lewa gora minimapy GH na 2560x1480 :142,118
##:prawy dol Gvar_Hamryd na 2560x1480 :685,931
##lew gora lisciaste rozstaje na 2560x1480 :7,253
##prawy dol lisciaste rozstaje na 2560x1480 :820,796

##: Matecznik szelesu: 
##: te same wymiary minimapy i pixeli


class MapProperties:
    def __init__(self, start_coords, end_coords, map_size, transitions, mob_locations, next_map_coords):
        self.startMiniMap = start_coords
        self.endMiniMap = end_coords
        self.mapSize = map_size
        self.transitions = transitions
        self.mob_locations = mob_locations
        self.nextMapCoords = next_map_coords

    def getStartMiniMap(self):
        return self.startMiniMap
    
    def getEndMiniMap(self):
        return self.endMiniMap
    
    def getMapSize(self):
        return self.mapSize
    
    def getTransitions(self):
        return self.transitions
    
    def getMobLocations(self):
        return self.mob_locations

    def getNextMapCoords(self):
        return self.nextMapCoords

map_data = {
    "Gvar Hamryd": MapProperties(
        start_coords=[142, 118],
        end_coords=[685, 931],
        map_size=[64, 96],
        transitions=[[63,42],[63,41],[11,0],[12,0],[0,79],[0,80]],  
        mob_locations=[[25,15],[52,43],[53,36],[54,23],[46,19],[44,42],[39,46],[42,54],[45,52]
            ,[55,53],[53,60],[48,67],[40,68],[38,75],[32,73],[31,80],[37,85],[45,86]
            ,[22,88],[12,89],[17,82],[8,79],[15,72],[16,63],[12,69],[48,83],[35,77]
            ,[33,61],[34,49],[26,42],[20,49],[3,59],[4,68],[9,67],[14,47],[44,66],[17,51]
            ,[6,43],[19,32],[8,30],[16,24],[8,17],[17,14],[13,5],[30,47]
            ,[59,42],[55,28],[53,17],[50,51],[38,51],[37,57],[38,63],[29,64]
            ,[23,73],[49,77],[23,83],[3,80],[7,62],[12,58],[11,53],[25,46],[28,37]
            ,[24,33],[12,28],[12,13],[19,4],[56,34]],
        next_map_coords=[0, 79]  
    ),
    "Matecznik Szelestu": MapProperties(
        start_coords=[142, 118],
        end_coords=[685, 931],
        map_size=[64, 96],
        transitions=[[63,79],[63,80],[22,0],[23,0]],
        mob_locations=[[61,77],[51,78],[57,79],[40,83],[43,79],[35,82],[37,86],[32,74],[24,83],[24,83],[27,91],[22,93],[18,75]
            ,[21,79],[23,73],[16,85],[6,81],[7,76],[29,70],[26,64],[33,66],[40,67],[44,69],[50,63]
            ,[45,58],[49,55],[52,51],[36,54],[29,55],[35,46],[34,39],[25,51],[20,58],[16,59],[14,63],[7,57]
            ,[14,53],[13,47],[21,50],[17,41],[14,39],[7,38],[10,35],[17,29],[20,24],[18,18],[23,21],[27,20]
            ,[34,18],[37,21],[47,17],[36,12],[26,13],[51,24],[57,30],[58,38],[59,43],[62,47],[52,18],[56,15]
            ,[58,8],[24,6],[19,5],[50,83],[17,44]],
        next_map_coords=[23, 0]  
    ),
    "Liściaste Rozstaje": MapProperties(
        start_coords=[7, 253],
        end_coords=[820, 796],
        map_size=[96, 64],
        transitions=[[22,63],[23,63],[75,63],[76,63],[95,38],[95,39]],  
        mob_locations=[[22,57],[28,56],[14,51],[22,44],[20,48],[13,39],[8,36],[28,40],[31,43],
           [27,32],[23,27],[18,24],[17,13],[45,40],[53,47],[57,41],[63,38],[66,31],
           [68,23],[70,43],[75,52],[82,53],[74,60],],
        next_map_coords=[75, 63] 
    ),
}

playerColor = (255,255,255)
mobColor = (235,12,12)
"""
przejsciaGH = [[63,42],[63,41],[11,0],[12,0],[0,79],[0,80]]
przejsciaMS = [[63,79],[63,80],[22,0],[23,0]]
przejsciaLR = [[22,63],[23,63],[75,63],[76,63],[95,38],[95,39]]

driadyGH=[[25,15],[52,43],[53,36],[54,23],[46,19],[44,42],[39,46],[42,54],[45,52],
[55,53],[53,60],[48,67],[40,68],[38,75],[32,73],[31,80],[37,85],[45,86],
[22,88],[12,89],[17,82],[8,79],[15,72],[16,63],[12,69],[48,83],[35,77],
[33,61],[34,49],[26,42],[20,49],[3,59],[4,68],[9,67],[14,47],[44,66],[17,51],
[6,43],[19,32],[8,30],[16,24],[8,17],[17,14],[13,5],[30,47],
[59,42],[55,28],[53,17],[50,51],[38,51],[37,57],[38,63],[29,64],
[23,73],[49,77],[23,83],[3,80],[7,62],[12,58],[11,53],[25,46],[28,37]
,[24,33],[12,28],[12,13],[19,4],[56,34]]
driadyMS = [[61,77],[51,78],[57,79],[40,83],[43,79],[35,82],[37,86],[32,74],[24,83],[24,83],[27,91],[22,93],[18,75]
            ,[21,79],[23,73],[16,85],[6,81],[7,76],[29,70],[26,64],[33,66],[40,67],[44,69],[50,63]
            ,[45,58],[49,55],[52,51],[36,54],[29,55],[35,46],[34,39],[25,51],[20,58],[16,59],[14,63],[7,57]
            ,[14,53],[13,47],[21,50],[17,41],[14,39],[7,38],[10,35],[17,29],[20,24],[18,18],[23,21],[27,20]
            ,[34,18],[37,21],[47,17],[36,12],[26,13],[51,24],[57,30],[58,38],[59,43],[62,47],[52,18],[56,15]
            ,[58,8],[24,6],[19,5],[50,83],[17,44]
            ]
driadyLR =[[22,57],[28,56],[14,51],[22,44],[20,48],[13,39],[8,36],[28,40],[31,43],
           [27,32],[23,27],[18,24],[17,13],[45,40],[53,47],[57,41],[63,38],[66,31],
           [68,23],[70,43],[75,52],[82,53],[74,60],]

"""
class startMiniMap:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def getStartMiniMap(self):
        return [self.x, self.y]
    
    def setStartMiniMap(self,x,y):
        self.x = x
        self.y = y

class endMiniMap:
    def __init__(self):
        self.x = 0
        self.y = 0

    def getEndMiniMap(self):
        return [self.x, self.y]
    
    def setEndMiniMap(self,x,y):
        self.x = x
        self.y = y

class mapSize:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.stepX = 0
        self.stepY = 0

    def getMapSize(self):
        return [self.x, self.y]

    def setMapSize(self, x, y):
        self.x = x
        self.y = y

    def calculateStepX(self, startMiniMap, endMiniMap):
        self.stepX = (endMiniMap.getEndMiniMap()[0] - startMiniMap.getStartMiniMap()[0]) / self.x
        return self.stepX
    
    def calculateStepY(self, startMiniMap, endMiniMap):
        self.stepY = (endMiniMap.getEndMiniMap()[1] - startMiniMap.getStartMiniMap()[1]) / self.y
        return self.stepY

    def getStepX(self):
        return self.stepX
    
    def getStepY(self):
        return self.stepY

class CurrentMap:
    def __init__(self,name="Gvar Hamryd"):
        self.name = name

    def getMapName(self):
        return self.name
    
    def setMapName(self,name):
        self.name = name


class koordynatyGracza:
    def __init__(self): 
        self.x = 0
        self.y = 0

    def getPlayerX(self):
        return self.x
    
    def getPlayerY(self):
        return self.y
    
    def getPlayerXY(self):
        return [self.x,self.y]
    
    def setPlayerX(self,x):
        self.x = x

    def setPlayerY(self,y):
        self.y = y

    def setPlayerXY(self,x,y):
        self.x = x
        self.y = y

class koordynatyMoba:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def getMobX(self):
        return self.x
    
    def getMobY(self):
        return self.y
    
    def getMobXY(self):
        return [self.x, self.y]
    
    def setMobX(self, x):
        self.x = x
    
    def setMobY(self, y):
        self.y = y
    
    def setMobXY(self, x, y):
        self.x = x
        self.y = y

class GameState:
    def __init__(self):
        self.current_map = CurrentMap() 
        self.player_coords = koordynatyGracza() 
        self.mob_coords = koordynatyMoba() 
        self.startMiniMap = startMiniMap()
        self.endMiniMap = endMiniMap()
        self.mapSize = mapSize()

    def getGameState(self):
        return {
            "map_name": self.current_map.getMapName(),
            "player_coords": self.player_coords.getPlayerXY(),
            "mob_coords": self.mob_coords.getMobXY(),
            "start_mini_map": self.startMiniMap.getStartMiniMap(),
            "end_mini_map": self.endMiniMap.getEndMiniMap(),
            "map_size": self.mapSize.getMapSize(),
            "step_x": self.mapSize.getStepX(),
            "step_y": self.mapSize.getStepY()
        }
    def setGameState(self, game_state):
        self.current_map.setMapName(game_state["map_name"])
        self.player_coords.setPlayerXY(game_state["player_coords"][0], game_state["player_coords"][1])
        self.mob_coords.setMobXY(game_state["mob_coords"][0], game_state["mob_coords"][1])

        current_map_properties = map_data.get(game_state["map_name"])

        self.startMiniMap.setStartMiniMap(current_map_properties.getStartMiniMap()[0], current_map_properties.getStartMiniMap()[1])
        self.endMiniMap.setEndMiniMap(current_map_properties.getEndMiniMap()[0], current_map_properties.getEndMiniMap()[1])
        self.mapSize.setMapSize(current_map_properties.getMapSize()[0], current_map_properties.getMapSize()[1])

        self.mapSize.calculateStepX(self.startMiniMap, self.endMiniMap)
        self.mapSize.calculateStepY(self.startMiniMap, self.endMiniMap)


