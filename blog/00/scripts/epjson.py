import json

with open( "1ZoneUncontrolled.epJSON") as f:
    ep_model = json.load(f)

ep_model["Building"]['Simple One Zone (Wireframe DXF)']['north_axis'] = 45

with open( "1ZoneUncontrolled_out.epJSON", "w") as f:
    output_epjson = json.dump(ep_model, f, indent = 4)
