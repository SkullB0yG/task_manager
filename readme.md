# Task Manager

## Descripciòn 

Este es un sencillo administrador de tareas en Python que te permite crear, ver, eliminar y marcar tareas como completas a través de la línea de comandos. El proyecto guarda las tareas en un archivo llamado *`pending_taskd`*

### Caracteristicas

- Crear tareas
- Ver todas las tareas pendientes
- Eliminar tareas por ID
- Marcar tareas como completas 


## Requisitos

- Python 3.x

## Intalaciòn

### Linux
Clona el repositorio e instala Python 3 si no está instalado.

```bash 
git clone https://github.com/tu_usuario/task-manager.git
cd task-manager
```

```bash
python --version
```

```bash 
sudo apt install python3
```

dale permisos de ejecucion al fichero task.py para poderlo ejecutar mas facil 
tambien le puedes hacer un alias en el archivo *`.zshrc`* si usas `Zsh` para `bash` el fichero se llama *`.bashrc`*. 

``` bash 
sudo chmod +x task.py
```

### Opcional 

crea el alias para la ejecucion del script desde el `.zshrc` o `bashrc`

``` bash
alias tasks="ruta donde se encuentra el fichero task.py" 
```

## Uso

para ejecutar el archivo sin alias 

```bash 
python task.py
```

### Comandos disponibles 

| Comando    | Descripciòn |
|------------|------------|
| `view`     | Muestra todas las tareas pendientes junto con sus IDs.   |
| `create`   | Crea una nueva tarea. Debes pasar la tarea como argumento. Ejemplo: create `comprar_leche'.  |
| `delete`   | Elimina una tarea por su ID. Debes pasar el ID como argumento. Ejemplo: `delete 1`.|
| `comlete`  | Marca una tarea como completa. Debes pasar la tarea como argumento. Ejemplo: `complete comprar_leche` |
| `clear`    | Limpia la consola.|
| `quit`     | Sale del programa. |
| `--help`   | Muestra la ayuda con los comandos disponibles.|

### Ejemplo de uso

1. Crear una tarea:

``` bash
create estudiar_sql 
```

2. Ver las tareas pendientes:

```bash
view
```

3. Marcar una tarea como completa:

```bash 
complete estudiar_sql
```

4. Eliminar una tarea: 

```bash
delete 0
```

# Compatibilidad con windows 

Para hacer que el comando *`clear`* funcione en windows, cambia la linea  `os.system("clear")` por `os.system("cls")`

``` python
elif order_commant[0] == "clear":
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
```

