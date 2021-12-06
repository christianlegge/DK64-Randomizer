@echo off
echo Started: %date% %time%
mkdir obj

python build\compile.py
build\armips.exe asm/jump_list.asm
python build\build.py
build\armips.exe asm/main.asm -sym rom\dk64-randomizer-base-dev.sym
rmdir /s /q .\obj > NUL
python build\correct_file_size.py
build\n64crc.exe rom\dk64-randomizer-base-dev.z64
python build\dump_pointer_tables_vanilla.py
python build\dump_pointer_tables_modified.py
del rom\dk64-randomizer-base-temp.z64
del rom\dk64-randomizer-base.z64

echo Completed: %date% %time%