import json
from collections import OrderedDict

team_data = OrderedDict()


team_data["Tiffany"] = {"StartState" : "LEFT_STAND","x":100,"y":100}
team_data["Yuna"] = {"StartState" : "RIGHT_RUN","x":200,"y":200}
team_data["Sunny"] = {"StartState" : "LEFT_RUN","x":300,"y":300}
team_data["Yuri"] = {"StartState" : "RIGHT_STAND","x":400,"y":400}
team_data["Jessica"] = {"StartState" : "LEFT_STAND","x":500,"y":500}

with open('team_data_txt.json','w',encoding="utf-8") as make_file:
    json.dump(team_data, make_file, ensure_ascii=False,indent="\t")
