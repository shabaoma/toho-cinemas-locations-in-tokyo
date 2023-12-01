import folium

# 创建地图对象
map = folium.Map(location=[35.6895, 139.7766], zoom_start=13)  # 设置初始地图中心位置和缩放级别

# Toho Cinemas的坐标数据（经度，纬度）
toho_cinemas = [
    {"name": "TOHO CINEMAS HIBIYA", "location": [35.673668795332, 139.75924361618]},
    {"name": "TOHO CINEMAS CHANTER", "location": [35.673474269241, 139.76056538674]},
    {"name": "TOHO CINEMAS SHINJUKU", "location": [35.695391403385, 139.70202698064]},
    {"name": "TOHO CINEMAS IKEBUKURO", "location": [35.73237151302, 139.715465227]},
    {"name": "TOHO CINEMAS NIHONBASHI", "location": [35.686919555227, 139.7748796308]},
    {"name": "TOHO CINEMAS UENO", "location": [35.70681110267, 139.77315310237]},
    {"name": "TOHO CINEMAS ROPPONGI HILLS", "location": [35.659561085972, 139.72940434178]},
    {"name": "TOHO CINEMAS SHIBUYA", "location": [35.659042748242, 139.6989630738]},
    {"name": "TOHO CINEMAS NISHIARAI", "location": [35.77525490588, 139.78610699217]},
    {"name": "TOHO CINEMAS MINAMIOSAWA", "location": [35.614664282485, 139.3802539663]},
    {"name": "TOHO CINEMAS FUCHU", "location": [35.671592, 139.4809148]},
    {"name": "TOHO CINEMAS TACHIKAWA TACHIHI", "location": [35.712585855097, 139.41614163802]},
    {"name": "TOHO CINEMAS KINSHICHO", "location": [35.7009585, 139.8157191]},
]

# 在地图上标注Toho Cinemas所在地
for cinema in toho_cinemas:
    folium.Marker(location=cinema["location"], popup=cinema["name"], icon=folium.Icon(color="red")).add_to(map)

# 保存地图为HTML文件
map.save("html/index.html")
