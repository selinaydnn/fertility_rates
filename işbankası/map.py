import folium
import pandas as pd
import json


df_grouped = pd.read_csv("/Users/selinaydin/PycharmProjects/işbankası/source_doc/regional_fertility_rates.csv")


geojson_path = "turkey_regions.geojson"
with open(geojson_path, "r", encoding="utf-8") as f:
    turkey_regions_geojson = json.load(f)


m = folium.Map(location=[39, 35], zoom_start=6)


def get_color(value):
    if value > 80:
        return 'darkred'
    elif value > 60:
        return 'red'
    elif value > 40:
        return 'orange'
    else:
        return 'green'


for feature in turkey_regions_geojson["features"]:
    region_name = feature["properties"]["Location"]


    region_value = df_grouped[df_grouped["Location"] == region_name]["Value"].values

    if len(region_value) > 0:
        value = region_value[0]
        color = get_color(value)


        folium.GeoJson(
            feature,
            style_function=lambda feature, col=color: {
                "fillColor": col,
                "color": "black",
                "weight": 1,
                "fillOpacity": 0.6
            }
        ).add_to(m)


        coords = feature["geometry"]["coordinates"][0][0]
        popup_text = f"{region_name}: {value:.2f}"
        folium.Marker(
            location=[coords[1], coords[0]],
            popup=popup_text,
            icon=folium.DivIcon(html=f"<div style='background-color: white; padding: 5px; border-radius: 5px; font-size: 12px;'>{popup_text}</div>")
        ).add_to(m)


map_path = "turkey_fertility_map.html"
m.save(map_path)


