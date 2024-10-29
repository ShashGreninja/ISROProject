import folium
from folium import plugins

# Initialize the map centered on a general location on the Moon
moon_map = folium.Map(
    location=[0, 0],  # latitude and longitude
    zoom_start=3,
    tiles='Stamen Terrain'  # Stamen Terrain provides a shaded-relief effect
)

# Add Moon image overlay (replace with actual lunar tile source if available)
lunar_tile_url = 'https://moon.nasa.gov/system/resources/detail_files/254_PIA13517-full.tif'  # Sample URL for a NASA moon image
folium.raster_layers.TileLayer(
    tiles=lunar_tile_url,
    name="Lunar Surface",
    attr="NASA",
    overlay=True,
    control=True
).add_to(moon_map)

# Add a layer control to toggle between layers
folium.LayerControl().add_to(moon_map)

# 3D Effect Simulation - Adding HeatMap for Visual Relief (simulates surface terrain)
heat_data = [[lat, lon, 1] for lat in range(-90, 91, 10) for lon in range(-180, 181, 10)]
plugins.HeatMap(heat_data, radius=15, blur=10, max_zoom=5).add_to(moon_map)

# Save and display map
moon_map.save("moon_map.html")
moon_map
