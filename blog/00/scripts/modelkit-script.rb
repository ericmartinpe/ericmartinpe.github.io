require("modelkit/energyplus")

iddfile = "C:/EnergyPlusV22-1-0/Energy+.idd"
$idd = OpenStudio::DataDictionary.open(iddfile)

idfpath = "1ZoneUncontrolled.idf"
idf = OpenStudio::InputFile.open($idd, idfpath)

def field_number_lookup(class_name, field_def)
  class_def = $idd.get_class_def(class_name)
  field_defs = class_def.field_definitions
  field_defs.shift if field_defs[0] == nil # Remove first item if it's blank
  field_defs.each_with_index do |f, i|
    return (i + 1) if f.name.to_s == field_def
  end
end

building = idf.find_objects_by_class_name("Building")
building[0].fields[field_number_lookup("Building", "North Axis")] = 45
idf.write("1ZoneUncontrolled_out.idf")

# building = idf.find_objects_by_class_name("Building")
# building = idf.find_object_by_class_and_name("Building","Simple One Zone (Wireframe DXF)")
# building.fields[field_number_lookup("Building", "North Axis")] = 21


# building = idf.find_objects_by_class_name("Building")
building[0].fields[2] = 45
#
# idf.write("1ZoneUncontrolled_out.idf")


# building.each do |o|
#   p o.fields[2]
# end
#
# class_def = idd.get_class_def("Building")
# field_defs = class_def.field_definitions
# field_defs.shift  # Remove first item; it's blank
# field_defs.each_with_index do |f, i|
#   puts "field=#{f.name}, #{i}"
# end
