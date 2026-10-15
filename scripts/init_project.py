import argparse
from pathlib import Path
parser=argparse.ArgumentParser(description="Crear estructura de proyecto web sin sobrescribir")
parser.add_argument("path",type=Path)
parser.add_argument("--name",default="Proyecto web")
a=parser.parse_args()
dirs=["research/references","research/screenshots","assets/source","assets/approved","prototypes/option-01","prototypes/option-02","prototypes/option-03","prototypes/synthesis","reviews","deploy"]
for d in dirs: (a.path/d).mkdir(parents=True,exist_ok=True)
texts={"brief":"Objetivo, audiencia, propuesta, conversión, marca y restricciones.","scope":"Páginas, entregables, exclusiones y criterios de aceptación.","decisions":"| Fecha | Decisión | Fundamento | Aprobación |\n|---|---|---|---|", "feedback":"| Ronda | Página | Observación | Acción | Estado |\n|---|---|---|---|---|", "pending":"| Página | Pendiente | Responsable | Estado |\n|---|---|---|---|", "content-inventory":"| Recurso | Origen | Derechos | Selección | Ubicación | Estado |\n|---|---|---|---|---|---|", "roadmap":"| Etapa | Tareas | Validación | Estado | Commit |\n|---|---|---|---|---|", "release":"Origen, destino, procedimiento, autorización, URL y comprobaciones."}
(a.path/"docs").mkdir(parents=True,exist_ok=True)
for name,body in texts.items():
    f=a.path/"docs"/(name+".md")
    try:
        with f.open("x",encoding="utf-8") as out: out.write("# "+a.name+" — "+name+"\n\n"+body+"\n")
    except FileExistsError: pass
print("Estructura preparada en",a.path.resolve())
