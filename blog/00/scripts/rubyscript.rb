require 'json'

File.open("1ZoneUncontrolled.epJSON") do |f|
  $ep_model = JSON.load(f)
end

$ep_model['Building']['Simple One Zone (Wireframe DXF)']['north_axis'] = 45

File.open("1ZoneUncontrolled_out1.epJSON", 'w') do |f|
  f.write(JSON.pretty_generate($ep_model))
end
