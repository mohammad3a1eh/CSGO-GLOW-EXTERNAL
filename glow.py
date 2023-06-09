import pymem
import pymem.process
import keyboard
import time
from csgo import *






def glow():
    try:
        pm = pymem.Pymem("csgo.exe")


        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        
        
        glow_manager = pm.read_uint(client + dwGlowObjectManager)
        for i in range(1, 32):
            entity = pm.read_uint(client + dwEntityList + i * 0x10)
            if entity > 0:
                entity_team_id = pm.read_uint(entity + m_iTeamNum)
                entity_glow = pm.read_uint(entity + m_iGlowIndex)
    
                if entity_team_id == 3:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, 1.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, 0.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, 0.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, 0.7)
                    pm.write_bool(glow_manager + entity_glow * 0x38 + 0x28, True)
                    pm.write_bool(glow_manager + entity_glow * 0x38 + 0x29, False)
    
                if entity_team_id == 2:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, 0.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, 1.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, 0.0)
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, 0.7)
                    pm.write_bool(glow_manager + entity_glow * 0x38 + 0x28, True)
                    pm.write_bool(glow_manager + entity_glow * 0x38 + 0x29, False)
        time.sleep(0.001)
    except Exception as error:
        print(error)
        
        
if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("alt"):
            glow()