# Social Graph from Apache Nifi

Se presenta una aplicación para descargar tweets relacionados a un tema en específico, los cuales serán cargados en una base de datos orientada a grafos (Neo4j). Para la descarga se usa ApacheNifi, con el cual se descargará a un tiempo determinado los diferentes tweets

# Herramientas para el desarrollo

|  Tool | Descripción   | Link  |
|:-:|:-:|:-:|
| Twint  | Librería en python para descargar tweets sin restricciones ni credenciales   | [twint_library]  |
| projectStructure  | Estandar para estructurar proyectos de DataScience   | [cookie_project_structure]  |
| Style Guide Code Python  | Estandar para nomenclatura de Python  | [style_guide_python]  |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |


# Pendientes 24-5-2019
- Hasta el momento se comprendió la librería para descargar tweets, ahora se debe tomar la lógica para seguidores y seguidos. Y esto pasarlo a este formato

´´´[json]

{"user":{"followers":9108,"following":853,"name":"Simon Phipps","bio":"Independent geek working for digital liberty & open source. OSI President, TDF & ORG Director. Founded Meshed Insights Ltd & Public Software. Other stuff before","id":752133,"username":"webmink"},"following":[16669912,13611,14248247,78012548,49420481,15211440,212632603,14335498,14206328,12381352,17448424,6424562,20518767,765548,4034271,16185413,12271362,14804841,1413771,15376576,36093693,818340,7617702,143883,24253645,14066062],"followers":[1433864449,335986035,1020794606,1073388199,2748339535,24360543,39554511,331262055,25386700,36965900,16288000,54702420,231845623,18691802,5159271,488417933,1097362550,13740932,90125298,6424562,49420481,152352998,4034271,8980232,15376576,51754021,8932122,609543,17778401,902438742,16185413,13611,56231291,9630822,851430115,14639127,791300,2327560616,14066062,12271362,14206328,1413771,5518682,14640060,12287422,89097137,15211440,26603208,14248247,17448424,14566379,3662432549,214141678,957117722927751168,209779726,15426758,18593319,50438579,16669912,86077357,25522270,1733530368,17023078,14684110,120269446,111457430,340753449,56469411,14804841,1540862004,472399449,69547504,17186468,13321432,14327226,768870,777747750,259927826,17026924,143883,16377075,8675652,94397736,360049309,20380353,14309129,22903583,19618391]}

´´´



Cabe destacar que este proyecto es una extensión del tutorial presentado en [esta publicación].

[twint_library]:https://github.com/twintproject/twint
[cookie_project_structure]:https://drivendata.github.io/cookiecutter-data-science/#directory-structure

[style_guide_python]:https://www.python.org/dev/peps/pep-0008/


[esta publicación]:https://medium.com/neo4j/finding-influencers-and-communities-in-the-graph-community-e3d691296325
