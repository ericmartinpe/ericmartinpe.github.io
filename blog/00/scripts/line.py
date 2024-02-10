input_file = "1ZoneUncontrolled.idf"
output = ""
with open(input_file) as idf:
    for line in idf:
        if "!- North Axis" in line:
            output += "    45,                       !- North Axis\n"
        else:
            output += line

with open("1ZoneUncontrolled_out.idf", "w") as f:
    f.write(output)
