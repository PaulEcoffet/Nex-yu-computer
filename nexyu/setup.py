import os
if os.name == "nt":
    from cx_Freeze import setup, Executable
    main = Executable("main.py",
                    icon="../res/icon.ico",
                )
    setup(
        name="Nex yu computer",
        version="0.1",
        description="Nex yu computer is the computer part of Nex yu",
        executables=[main],
    )
