import cx_Freeze

executables = [cx_Freeze.Executable("Snake.py")]

cx_Freeze.setup(
    name="Snake",
    options={"build_exe":{"packages":["pygame"],"include_files":["Apple.png", "snakeHead.png"]}},
    description = "Snake",
    executables = executables
    )
    

