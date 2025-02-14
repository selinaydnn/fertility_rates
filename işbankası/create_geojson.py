import json


turkey_regions_geojson = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[26.0, 36.0], [30.0, 36.0], [30.0, 39.0], [26.0, 39.0], [26.0, 36.0]]]}, "properties": {"Location": "Aegean"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[30.0, 36.0], [35.0, 36.0], [35.0, 39.0], [30.0, 39.0], [30.0, 36.0]]]}, "properties": {"Location": "Central"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[35.0, 36.0], [39.0, 36.0], [39.0, 39.0], [35.0, 39.0], [35.0, 36.0]]]}, "properties": {"Location": "Central Anatolia"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[39.0, 36.0], [42.0, 36.0], [42.0, 39.0], [39.0, 39.0], [39.0, 36.0]]]}, "properties": {"Location": "Central East Anatolia"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[42.0, 36.0], [45.0, 36.0], [45.0, 39.0], [42.0, 39.0], [42.0, 36.0]]]}, "properties": {"Location": "East"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[26.0, 39.0], [30.0, 39.0], [30.0, 42.0], [26.0, 42.0], [26.0, 39.0]]]}, "properties": {"Location": "West Marmara"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[30.0, 39.0], [35.0, 39.0], [35.0, 42.0], [30.0, 42.0], [30.0, 39.0]]]}, "properties": {"Location": "East Marmara"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[35.0, 39.0], [39.0, 39.0], [39.0, 42.0], [35.0, 42.0], [35.0, 39.0]]]}, "properties": {"Location": "West Black Sea"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[39.0, 39.0], [42.0, 39.0], [42.0, 42.0], [39.0, 42.0], [39.0, 39.0]]]}, "properties": {"Location": "East Black Sea"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[42.0, 39.0], [45.0, 39.0], [45.0, 42.0], [42.0, 42.0], [42.0, 39.0]]]}, "properties": {"Location": "Northeast Anatolia"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[39.0, 36.0], [42.0, 36.0], [42.0, 39.0], [39.0, 39.0], [39.0, 36.0]]]}, "properties": {"Location": "Southeast Anatolia"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[35.0, 36.0], [39.0, 36.0], [39.0, 39.0], [35.0, 39.0], [35.0, 36.0]]]}, "properties": {"Location": "Mediterranean"}},
        {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[30.0, 42.0], [35.0, 42.0], [35.0, 45.0], [30.0, 45.0], [30.0, 42.0]]]}, "properties": {"Location": "Istanbul"}}
    ]
}


geojson_path = "turkey_regions.geojson"
with open(geojson_path, "w", encoding="utf-8") as f:
    json.dump(turkey_regions_geojson, f)

print(f"GeoJSON dosyası oluşturuldu: {geojson_path}")
