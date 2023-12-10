## THIS SOURCECODE IS LICENSED BY THE UNLICENSE LICENSE
## SELLING THIS CODE IS FORBIDDEN. ITS ONLY FOR PRIVATE USE
## SELLING THIS WILL RESULT IN A DMCA TAKEDOWN

## the owner was violating isaac's human rights, isaac cannot have a free will in the server because the owner is gonna tell him do this and this or you wont get owner role back etc. More about this:
## https://firox.xyz/starsource
## https://github.com/Firoxus/star-sourcecode

## full credit for this code goes to isaac
## discord: isaac_official


import subprocess
import platform
import json as jsond
import time
import os
import zipfile

def Is_Package_Installed(package):
    try:
        __import__(package)
        return True
    except:
        return False
    
    
def Install_Init_Package():
    try:
        __import__("colorama")
        return True
    except:
        subprocess.run(f"pip install colorama", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    
if Is_Package_Installed("colorama"):
    from colorama import Fore, Back, Style
else:
    Install_Init_Package()
    from colorama import Fore, Back, Style
     

def Install_Init_Stuffs():
    try:
        local_appdata = os.getenv("LOCALAPPDATA")
        download_path = local_appdata + "\\Star_Optimizer\\"
        
        exe_path = os.path.join(download_path, "nvidiaProfileInspector.exe")
        if os.path.exists(exe_path):
            print(f"{Fore.GREEN}[-]{Fore.WHITE} NvidiaProfileInspector.exe is already present in the destination directory, Skipping.")
        else:
            os.makedirs(download_path, exist_ok=True)
            
            zip_file_path = os.path.join(local_appdata, "NvidiaProfileInspector.zip")
            
            response = requests.get("https://github.com/Orbmu2k/nvidiaProfileInspector/releases/latest/download/nvidiaProfileInspector.zip", stream=True)
            with open(zip_file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)
                    
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(download_path)
                
            os.remove(zip_file_path)
            
            print(f"{Fore.GREEN}[-]{Fore.WHITE} Installed NvidiaProfileInspector.exe.")
            
            
    except:
        print(f"{Fore.RED}[-]{Fore.WHITE} Unable to install required assets, Please contact the owners / developers.")
        
        time.sleep(3)
        
        os.exit()
    
    
    
def Check_OS():
    import os 
    if os.name == 'nt':
        return "Windows"
    else:
        return "Unknown"
    


    
    
if Is_Package_Installed("pywin32"):
    if Check_OS() == "Windows":
        import win32security
    else:
        pass
else:
    subprocess.run(f"pip install pywin32", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if Check_OS() == "Windows":
        import win32security
    
    
if Is_Package_Installed("requests"):
    import requests
else:
    subprocess.run(f"pip install requests", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import requests

    

    
    
class keyauth:


    def __init__(self):
        self.name = ""

        self.ownerid = ""

        self.version = ""
        self.hash_to_check = ""
        self.init()

    sessionid = enckey = ""
    initialized = False

    def init(self):

                
        post_data = {
            "type": "init",
            "ver": self.version,
            "hash": "",
            "enckey": "",
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        if response == "KeyAuth_Invalid":
            print("The application doesn't exist")
            time.sleep(3)
            os._exit(1)

        json = jsond.loads(response)
        
    

        if json["message"] == "invalidver":
            if json["download"] != "":
                print("New Version Available")
                download_link = json["download"]
                os.system(f"start {download_link}")
                time.sleep(3)
                os._exit(1)
            else:
                print("Invalid Version, Contact owner to add download link to latest app version")
                time.sleep(3)
                os._exit(1)

        if not json["success"]:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

        self.sessionid = json["sessionid"]
        self.initialized = True
        
        if json["newSession"]:
            time.sleep(0.1)
            
        return json
    
    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = subscriptions = ""
    
    user_data = user_data_class()
    
    def __load_user_data(self, data):
        self.user_data.username = data["username"]
        self.user_data.ip = data["ip"]
        self.user_data.hwid = data["hwid"] or "N/A"
        self.user_data.expires = data["subscriptions"][0]["expiry"]
        self.user_data.createdate = data["createdate"]
        self.user_data.lastlogin = data["lastlogin"]
        self.user_data.subscription = data["subscriptions"][0]["subscription"]
        self.user_data.subscriptions = data["subscriptions"]
        
    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            time.sleep(3)
            os._exit(1)
    
    def license(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = self.others.get_hwid()

        post_data = {
            "type": "license",
            "key": key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
            return json
        else:
            return json
            
    class others:
        @staticmethod
        def get_hwid():
            if platform.system() == "Linux":
                with open("/etc/machine-id") as f:
                    hwid = f.read()
                    return hwid
            elif platform.system() == 'Windows':
                winuser = os.getlogin()
                sid = win32security.LookupAccountName(None, winuser)[0]  # You can also use WMIC (better than SID, some users had problems with WMIC)
                hwid = win32security.ConvertSidToStringSid(sid)
                return hwid
            elif platform.system() == 'Darwin':
                output = subprocess.Popen("ioreg -l | grep IOPlatformSerialNumber", stdout=subprocess.PIPE, shell=True).communicate()[0]
                serial = output.decode().split('=', 1)[1].replace(' ', '')
                hwid = serial[1:-2]
                return hwid
            
    def __do_request(self, post_data):
        try:
            response = requests.post(
                "https://keyauth.win/api/1.2/", data=post_data, timeout=10
            )
            
            if post_data["type"] == "log": return response.text        
            
            return response.text
        except requests.exceptions.Timeout:
            print("Request timed out. Server is probably down/slow at the moment")


def Installer(req):
    nums_in_list = len(req)
    current_num = 0
    
    for requirement in req:
        current_num += 1
        try:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Installing Package '{requirement}' ({current_num}/{nums_in_list})")
            subprocess.run(f"pip install {requirement}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Package, Skipping.")
            
    time.sleep(1)
            
    subprocess.call("cls", shell=True)

def MainLoop():    
    import webbrowser
    
    
    subprocess.call("cls", shell=True)
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    new_men = customtkinter.CTk()
    new_men.title("Star")
    
    import ctypes
    user32 = ctypes.windll.user32

    
    new_men.geometry(f"{int(user32.GetSystemMetrics(0) * 0.9)}x{int(user32.GetSystemMetrics(1) * 0.8)}")
    new_men.resizable(False, False)
    new_men.attributes("-topmost", True)
    new_men.state('zoomed')
    
    
    #OPTIMIZE_OPTIONS = ['Simple', 'Mediocre', 'Advanced']
    OPTIMIZE_OS = False
    OPTIMIZE_REG = False
    OPTIMIZE_XTB = False
    OPTIMIZE_PB = False
    OPTIMIZE_FS = False
    OPTIMIZE_CRP = False
    OPTIMIZE_IT = False
    OPTIMIZE_NV = False
    OPTIMIZE_FOC = False
    OPTIMIZE_RAM = False
    OPTIMIZE_BCD = False
    
    #opti = customtkinter.StringVar(value=OPTIMIZE_OPTIONS[0])
    clean_os = customtkinter.BooleanVar(value = OPTIMIZE_OS) # Done
    opt_reg = customtkinter.BooleanVar(value = OPTIMIZE_REG) # Done
    opt_xtb = customtkinter.BooleanVar(value = OPTIMIZE_XTB) # Done
    opt_pb = customtkinter.BooleanVar(value = OPTIMIZE_PB) # Done
    opt_fs = customtkinter.BooleanVar(value = OPTIMIZE_FS) # Done
    opt_crp = customtkinter.BooleanVar(value = OPTIMIZE_CRP) # Done
    opt_it = customtkinter.BooleanVar(value = OPTIMIZE_IT) # Done
    opt_nv = customtkinter.BooleanVar(value = OPTIMIZE_NV) # Done
    opt_foc = customtkinter.BooleanVar(value = OPTIMIZE_FOC) # Done
    opt_ram = customtkinter.BooleanVar(value = OPTIMIZE_RAM) # Done
    opt_bcd = customtkinter.BooleanVar(value = OPTIMIZE_BCD)
    
    def CreateRestorePoint():
        print(f"{Fore.GREEN}[-]{Fore.WHITE} Creating Restore Point Named 'Star'.")
            
            
        subprocess.call('powershell -ExecutionPolicy Bypass -Command "Checkpoint-Computer -Description \'star\' -RestorePointType \'MODIFY_SETTINGS\'"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


        print(f"{Fore.GREEN}[-]{Fore.WHITE} Finished Creating Restore Point.")
            
        time.sleep(5)
            
        subprocess.call("cls", shell=True) 
    
    def UseRestorePoint():
        subprocess.run('rstrui.exe', shell=True)
    
    def OpenDiscord():    
        webbrowser.open("https://discord.gg/optimizer", new=0, autoraise=True)
    
    def Optimize():       
        
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Beginning...")
        #customtkinter.CTkLabel(master=master, text= "Status : .", font=("Calibri Bold", 50), text_color="#F3EDEC").pack(pady=12, padx=10)

        
        subprocess.call("cls", shell=True) 
        
        if opt_crp.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Creating Restore Point Named 'star'.")
            
            try:
                subprocess.call('powershell -ExecutionPolicy Bypass -Command "Checkpoint-Computer -Description \'star\' -RestorePointType \'MODIFY_SETTINGS\'"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Creating Restore Point.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Create A Restore Point.")
            
            time.sleep(5)
            
            subprocess.call("cls", shell=True)    
        
        
        optimization_reg_commands = [
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d "38" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "LargeSystemCache" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnablePreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "GPUPreemptionLevel" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableAsyncMidBufferPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableMidGfxPreemptionVGPU" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableMidBufferPreemptionForHighTdrTimeout" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableSCGMidBufferPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "PerfAnalyzeMidBufferPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableMidGfxPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableMidBufferPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "EnableCEPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "DisableCudaContextPreemption" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "DisablePreemptionOnS3S4" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "ComputePreemptionLevel" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v "DisablePreemption" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v "DpiMapIommuContiguous" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "MoveImages" /t REG_DWORD /d "0" /f',
            'for /f "skip=1" %%i in (\'wmic os get TotalVisibleMemorySize\') do if not defined TOTAL_MEMORY set "TOTAL_MEMORY=%%i" & set /a SVCHOST=%%i+1024000',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v "SvcHostSplitThresholdInKB" /t REG_DWORD /d "!SVCHOST!" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnableSuperfetch" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKCU\\Control Panel\\Desktop" /v "AutoEndTasks" /t REG_SZ /d "1" /f',
            'Reg.exe add "HKCU\\Control Panel\\Desktop" /v "HungAppTimeout" /t REG_SZ /d "1000" /f',
            'Reg.exe add "HKCU\\Control Panel\\Desktop" /v "WaitToKillAppTimeout" /t REG_SZ /d "2000" /f',
            'Reg.exe add "HKCU\\Control Panel\\Desktop" /v "LowLevelHooksTimeout" /t REG_SZ /d "1000" /f',
            'Reg.exe add "HKCU\\Control Panel\\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v "WaitToKillServiceTimeout" /t REG_SZ /d "2000" /f',
            'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Reliability" /v "TimeStampInterval" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Reliability" /v "IoPriority" /t REG_DWORD /d "3" /f',
            'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\csrss.exe\\PerfOptions" /v "CpuPriorityClass" /t REG_DWORD /d "4" /f',
            'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\csrss.exe\\PerfOptions" /v "IoPriority" /t REG_DWORD /d "3" /f',
            'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d "10" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\DXGKrnl" /v "MonitorLatencyTolerance" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\DXGKrnl" /v "MonitorRefreshLatencyTolerance" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "ExitLatency" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "ExitLatencyCheckEnabled" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "Latency" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "LatencyToleranceDefault" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "LatencyToleranceFSVP" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "LatencyTolerancePerfOverride" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "LatencyToleranceScreenOffIR" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "LatencyToleranceVSyncEnabled" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "RtlCapabilityCheckLatency" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyActivelyUsed" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyIdleLongTime" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyIdleMonitorOff" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyIdleNoContext" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyIdleShortTime" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultD3TransitionLatencyIdleVeryLongTime" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceIdle0" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceIdle0MonitorOff" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceIdle1" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceIdle1MonitorOff" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceMemory" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceNoContext" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceNoContextMonitorOff" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceOther" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultLatencyToleranceTimerPeriod" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultMemoryRefreshLatencyToleranceActivelyUsed" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultMemoryRefreshLatencyToleranceMonitorOff" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "DefaultMemoryRefreshLatencyToleranceNoContext" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "Latency" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "MaxIAverageGraphicsLatencyInOneBucket" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "MiracastPerfTrackGraphicsLatency" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "MonitorLatencyTolerance" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "MonitorRefreshLatencyTolerance" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power" /v "TransitionLatency" /t REG_DWORD /d "1" /f'
        ]
        if opt_reg.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Optimizing registry.")
            
            try:
                for cmd in optimization_reg_commands:
                    subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Optimizing registry.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Optimize registry.")
            
            time.sleep(4)
            
            subprocess.call("cls", shell=True)
            
        cleanup_commands = [
            'del /s /f /q c:\\windows\\temp.',
            'del /s /f /q C:\\WINDOWS\\Prefetch',
            'del /s /f /q %temp%.',
            'del /s /f /q %systemdrive%\\*.tmp',
            'del /s /f /q %systemdrive%\\*._mp',
            'del /s /f /q %systemdrive%\\*.log',
            'del /s /f /q %systemdrive%\\*.gid',
            'del /s /f /q %systemdrive%\\*.chk',
            'del /s /f /q %systemdrive%\\*.old',
            'del /s /f /q %systemdrive%\\recycled\\*.*',
            'del /s /f /q %systemdrive%\\$Recycle.Bin\\*.*',
            'del /s /f /q %windir%\\*.bak',
            'del /s /f /q %windir%\\prefetch\\*.*',
            'del /s /f /q %LocalAppData%\\Microsoft\\Windows\\Explorer\\thumbcache_*.db',
            'del /s /f /q %LocalAppData%\\Microsoft\\Windows\\Explorer\\*.db',
            'del /f /q %SystemRoot%\\Logs\\CBS\\CBS.log',
            'del /f /q %SystemRoot%\\Logs\\DISM\\DISM.log',
            'deltree /y c:\\windows\\tempor~1',
            'deltree /y c:\\windows\\temp',
            'deltree /y c:\\windows\\tmp',
            'deltree /y c:\\windows\\ff*.tmp',
            'deltree /y c:\\windows\\recent',
        ] 
        if clean_os.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Cleaning OS.")
            
            try:
                for cmd in cleanup_commands:
                    subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Cleaning OS.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Clean OS.")
            
            time.sleep(4)
            
            subprocess.call("cls", shell=True)
            
        xbt_commands = [
            "Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage",
            "Get-AppxPackage -allusers *3DBuilder* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *bing* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *bingfinance* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *bingsports* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *BingWeather* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *CommsPhone* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Drawboard PDF* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Facebook* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Getstarted* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Microsoft.Messaging* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *MicrosoftOfficeHub* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Office.OneNote* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *OneNote* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *people* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *SkypeApp* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *solit* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Sway* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *Twitter* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *WindowsAlarms* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *WindowsPhone* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *WindowsMaps* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *WindowsFeedbackHub* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *WindowsSoundRecorder* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *windowscommunicationsapps* | Remove-AppxPackage",
            "Get-AppxPackage -allusers *zune* | Remove-AppxPackage",
            "sc config xbgm start= disabled >nul 2>&1",
            "sc config XblAuthManager start= disabled",
            "sc config XblGameSave start= disabled",
            "sc config XboxGipSvc start= disabled",
            "sc config XboxNetApiSvc start= disabled"
        ]
        if opt_xtb.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Removing Xbox Tool Bar and Unnecessary Apps.")
            
            try:
                for cmd in xbt_commands:
                    subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Xbox Tool Bar and Unnecessary Apps.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Remove Xbox Tool Bar and Unnecessary Apps.")
                            
            time.sleep(4)
            
            subprocess.call("cls", shell=True)
        
        FileLink = "https://cdn.discordapp.com/attachments/1148654588979847361/1175784370393600050/GameUserSettings.ini?ex=656c7d86&is=655a0886&hm=99a8085a7d39642e1905af3f84b7b4330de1b4121ff9786509c270b6ae902074&"
        if opt_fs.get() == True:
            
            
            
            #print(f"{Fore.GREEN}[-] {Fore.WHITE}Modifying Game Settings.")
            
            #try:
                #DownloadedReq = requests.get(FileLink)
                #if DownloadedReq.status_code == 200:
                    #local_appdata = os.getenv("LOCALAPPDATA")
                    #fortnite_path = local_appdata + "\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini"
                    
                    #print(fortnite_path)
                    
                    #with open(fortnite_path, "wb") as file:
                        #file.write(DownloadedReq.content)
                        
                    #print(f"{Fore.GREEN}[-] {Fore.WHITE}Modified Game Settings.")
            #except:
                #print(f"{Fore.RED}[-] {Fore.WHITE}Could not Modify Game Settings.")
                
            time.sleep(4)
            
            subprocess.call("cls", shell=True)
            
        PowFileLink = "https://cdn.discordapp.com/attachments/1148654588979847361/1175600733962371192/star.pow?ex=656bd280&is=65595d80&hm=c4cabdc2652ef890efeea1faf8706f79557e9bd17e59bd4121d9587f0b0f6b71&"
        if opt_pb.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Modifying Power Plan Settings.") 
            
            try:
                DownloadedReq = requests.get(PowFileLink)
                if DownloadedReq.status_code == 200:
                    local_appdata = os.getenv("LOCALAPPDATA")
                    save_path = local_appdata + "\\Star_Optimizer\\"
                    
                    save_path = os.path.join(save_path, "Star.pow")
                    
                    with open(save_path, "wb") as file:
                        file.write(DownloadedReq.content)
                    
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Downloaded Power Plan File, Importing.") 
                    
                    run_cmd = subprocess.run(f'powercfg -import "{save_path}"', shell=True, capture_output=True)
                    
                    try:
                        output_str = run_cmd.stdout.decode("utf-8")

                        guid_index = output_str.find("GUID:")

                        if guid_index != -1:
                            guid = output_str[guid_index + 5:].strip()
                            print(f"{Fore.GREEN}[-] {Fore.WHITE}Recieved GUID, Activating.")   
                            
                            subprocess.run(f'powercfg  /SETACTIVE {guid}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            
                            time.sleep(1)
                            
                            print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Power Plan, Finished.")   
                            
                            os.remove(save_path)
                        else:
                            print(f"{Fore.RED}[-] {Fore.WHITE}Unable to extract GUID from the output.")   
                    except:
                        print(f"{Fore.RED}[-] {Fore.WHITE}Unable to extract GUID from the output.")   
                    
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not modify Power Plan Settings.")                
            time.sleep(4)    
            subprocess.call("cls", shell=True)
        
        if opt_it.get() == True:
            query_command = 'Reg query "HKLM\System\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}" /t REG_SZ /s /e /f "Intel" | findstr "HKEY"'
            intel_req = subprocess.run(query_command, shell=True, capture_output=True, text=True)

            try:
                if intel_req.returncode == 0:
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Optimizing Intel GPU.")
                    for subkey in intel_req.stdout.splitlines():
                        subprocess.run(f'Reg.exe add "{subkey}" /v "Disable_OverlayDSQualityEnhancement" /t REG_DWORD /d "1" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "IncreaseFixedSegment" /t REG_DWORD /d "1" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "AdaptiveVsyncEnable" /t REG_DWORD /d "0" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "DisablePFonDP" /t REG_DWORD /d "1" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "EnableCompensationForDVI" /t REG_DWORD /d "1" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "NoFastLinkTrainingForeDP" /t REG_DWORD /d "0" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "ACPowerPolicyVersion" /t REG_DWORD /d "16898" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        subprocess.run(f'Reg.exe add "{subkey}" /v "DCPowerPolicyVersion" /t REG_DWORD /d "16642" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Done Optimizing Intel GPU.")
                    
                    time.sleep(4)
                    
            
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could Not Tweak Intel GPU, Make sure you have an Intel GPU.")
                
                time.sleep(4)
                
            subprocess.call("cls", shell=True)
                
        nip_link = "https://cdn.discordapp.com/attachments/1148654588979847361/1175857223591800942/StarNvidia.nip?ex=656cc160&is=655a4c60&hm=1a2c6571680eb05ce28276e26e78f265a81da572ef682881896d7e4c5fef38d3&"
        if opt_nv.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Optimizing Nvidia GPU.")
            
            try:
                DownloadedReq = requests.get(nip_link)
                if DownloadedReq.status_code == 200:
                    local_appdata = os.getenv("LOCALAPPDATA")
                    save_path = os.path.join(local_appdata + "\\Star_Optimizer\\", "StarNvidia.nip")
                    nvidia_savepath = local_appdata + "\\Star_Optimizer\\"
                    
                    
                    with open(save_path, "wb") as file:
                        file.write(DownloadedReq.content)
                        
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Downloaded Nvidia File, Importing.")

                
                subprocess.run(f'start "" "{nvidia_savepath}\\nvidiaProfileInspector.exe" "{save_path}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                nvidia_res = subprocess.run('wmic path win32_videocontroller get PNPDeviceID', shell=True, capture_output=True)
                
                stdout_str = nvidia_res.stdout.decode('utf-8')
                
                import re
                
                pnp_device_ids = re.findall(r'PCI\\VEN_[A-Fa-f\d]{4}&DEV_[A-Fa-f\d]{4}', stdout_str)
                
                print(pnp_device_ids)
                for pnp_device_id in pnp_device_ids:
                    reg_commands = [
                        f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\{pnp_device_id}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties" /v "MSISupported" /t REG_DWORD /d "1" /f',
                        f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\{pnp_device_id}\\Device Parameters\\Interrupt Management\\Affinity Policy" /v "DevicePriority" /t REG_DWORD /d "0" /f'
                    ]

                    for reg_command in reg_commands:
                        subprocess.run(reg_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        
                subprocess.run('timeout /t 1 /nobreak > NUL', shell=True)
                                
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Executing Registry Commands for Nvidia GPU.")

                
                nvidia_commands = [
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "D3PCLatency" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "F1TransitionLatency" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "LOWLATENCY" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "Node3DLowLatency" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PciLatencyTimerControl" /t REG_DWORD /d "20" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMDeepL1EntryLatencyUsec" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RmGspcMaxFtuS" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RmGspcMinFtuS" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RmGspcPerioduS" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMLpwrEiIdleThresholdUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMLpwrGrIdleThresholdUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMLpwrGrRgIdleThresholdUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMLpwrMsIdleThresholdUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "VRDirectFlipDPCDelayUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "VRDirectFlipTimingMarginUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "VRDirectJITFlipMsHybridFlipDelayUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "vrrCursorMarginUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "vrrDeflickerMarginUs" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "vrrDeflickerMaxUs" /t REG_DWORD /d "1" /f',
                    'timeout /t 1 /nobreak > NUL',
                    'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "NvBackend" /f',
                    'Reg.exe add "HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS" /v "EnableRID66610" /t REG_DWORD /d "0" /f',
                    'Reg.exe add "HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS" /v "EnableRID64640" /t REG_DWORD /d "0" /f',
                    'Reg.exe add "HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS" /v "EnableRID44231" /t REG_DWORD /d "0" /f',
                    'schtasks /change /disable /tn "NvTmRep_CrashReport1_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NvTmRep_CrashReport2_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NvTmRep_CrashReport3_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NvTmRep_CrashReport4_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NvDriverUpdateCheckDaily_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NVIDIA GeForce Experience SelfUpdate_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'schtasks /change /disable /tn "NvTmMon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"',
                    'timeout /t 1 /nobreak > NUL',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "DisableWriteCombining" /t REG_DWORD /d "1" /f',
                    'timeout /t 1 /nobreak > NUL',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "DisablePreemption" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "DisableCudaContextPreemption" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "EnableCEPreemption" /t REG_DWORD /d "0" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "DisablePreemptionOnS3S4" /t REG_DWORD /d "1" /f',
                    'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm" /v "ComputePreemption" /t REG_DWORD /d "0" /f',
                    'timeout /t 1 /nobreak > NUL'
                ]
                
                for cmd in nvidia_commands:
                    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                os.remove(save_path)    
                
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Optimizing Nvidia GPU.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Optimize Nvidia GPU.")
            
            time.sleep(4)
            
            subprocess.call("cls", shell=True)
        
        if opt_foc.get() == True:
            try:
                subprocess.call('Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\FortniteClient-Win64-Shipping.exe\PerfOptions" /v "CpuPriorityClass" /t REG_DWORD /d "3" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Fortnite is now highest on CPU priority.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could make Fortnite highest on CPU priority.")
            
            time.sleep(3)
            
            subprocess.call("cls", shell=True)
              
        ram_commands = [
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "DpiMapIommuContiguous" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control" /v "SvcHostSplitThresholdInKB" /t REG_DWORD /d "!SVCHOST!" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v "EnableSuperfetch" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "ClearPageFileAtShutdown" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "LargeSystemCache" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "NonPagedPoolQuota" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "NonPagedPoolSize" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PagedPoolQuota" /t REG_DWORD /d "0" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PagedPoolSize" /t REG_DWORD /d "192" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SecondLevelDataCache" /t REG_DWORD /d "1024" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SessionPoolSize" /t REG_DWORD /d "192" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SessionViewSize" /t REG_DWORD /d "192" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SystemPages" /t REG_DWORD /d "4294967295" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PhysicalAddressExtension" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "FeatureSettings" /t REG_DWORD /d "1" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "FeatureSettingsOverride" /t REG_DWORD /d "3" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "FeatureSettingsOverrideMask" /t REG_DWORD /d "3" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "IoPageLockLimit" /t REG_DWORD /d "16710656" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PoolUsageMaximum" /t REG_DWORD /d "96" /f',
            'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "Start" /t REG_DWORD /d "4" /f'
        ]
        if opt_ram.get() == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Optimizing RAM.")
            
            try:
                result = subprocess.run('wmic os get TotalVisibleMemorySize', stdout=subprocess.PIPE, shell=True, text=True)
                lines = [line.strip() for line in result.stdout.strip().split('\n')[1:] if line.strip()]
                            
                svchost = int(lines[0].strip()) + 1024000
                
                
                subprocess.run(f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v "SvcHostSplitThresholdInKB" /t REG_DWORD /d "{svchost}" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                for cmd in ram_commands:
                    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Optimizing RAM.")
            except:
                print(f"{Fore.RED}[-] {Fore.WHITE}Could not Optimize RAM.")
            
            time.sleep(3)
            
            subprocess.call("cls", shell=True)
            
        opt_bcd_Cmds = [
            'bcdedit /set disabledynamictick yes >nul 2>&1',
            'bcdedit /deletevalue useplatformclock  >nul 2>&1',
            'bcdedit /set useplatformtick yes  >nul 2>&1'
        ]
        if opt_bcd == True:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Optimizing BCD.")
            
            for cmd in opt_bcd_Cmds:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(1)
                
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Optimizing BCD.")
            
                    
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished Optimizing.")
                
        time.sleep(4)
                
        
        
        subprocess.call("cls", shell=True)
    
    class Panel(customtkinter.CTkFrame):
        def __init__(self, parent):
            super().__init__(master=parent)
            self.pack(fill='x', pady=4, ipady=8)

    class SegmentedPanel(Panel):
        def __init__(self, parent, text, data_var, options):
            super().__init__(parent = parent)
            
            customtkinter.CTkLabel(self, text = text, font=("Calibri Bold", 20), text_color="#F3EDEC").pack()
            customtkinter.CTkSegmentedButton(self, variable = data_var, values = options).pack(expand = True, fill = 'both', padx=4, pady=4)
            
    class SwitchPanel(Panel):
        def __init__(self, parent, *args):
            super().__init__(parent = parent)
            
            for var, text in args:
                switch = customtkinter.CTkSwitch(self, text = text, variable = var)
                switch.pack(side= 'top', expand = True, fill = 'both', padx = 5, pady = 10)
          
    class Menu(customtkinter.CTkTabview):
        def __init__(self, parent):
            super().__init__(master = parent, width=int(user32.GetSystemMetrics(0) * 0.9), height =int(user32.GetSystemMetrics(1) * 0.8))
            self.grid(row=0, column=0,  sticky="nsew")
                
                
                
            self.add('Optimization')
            self.add('Restoration')
            self.add('Credits')
            
            Main_Men(self.tab('Optimization'))
            Res_Men(self.tab('Restoration'))
            Cre_Men(self.tab('Credits'))
           
            
            
    class Main_Men(customtkinter.CTkFrame):
        def __init__(self, parent):
            super().__init__(master=parent, fg_color='transparent')
            self.pack(expand=True, fill='both')
            
            
            customtkinter.CTkLabel(master=self, text= "Optimizer", font=("Calibri Bold", 50), text_color="#F3EDEC").pack(pady=12, padx=10)
            #SegmentedPanel(self, 'Optimization Type', opti, OPTIMIZE_OPTIONS)
            SwitchPanel(self, (opt_crp, 'Create Restore Point - Creates a restore point before optimizing (RECOMMENDED, WE ARE NOT LIABLE FOR DAMAGE)'), (clean_os, 'Clean OS -  Cleans all unused files that can cause bloating.'), (opt_reg, 'Optimize Registry - Optimises all registry info relating to fortnite and FPS boosting.'), (opt_xtb, 'Disable Xbox ToolBar - Disables Toolbar, Helps FPS as toolbar uses alot of preformance.'), (opt_pb, 'Power Plan - Makes it so your PC boots with the best mode.'), (opt_fs, 'Edit Game Settings [DISABLED] - Edits the actual game settings in order to give you the best FPS boost.'), (opt_it, 'Optimzie Intel GPU - Only use this if you have an Intel GPU.'), (opt_nv, 'Optimize Nvidia GPU - Only use this if you have an Nvidia GPU.'), (opt_foc, 'High Priority Fortnite - Makes fortnite on the highest priority on CPU, Makes textures load better and boosts FPS.'), (opt_ram, 'Optimize RAM - Makes your RAM run Fortnite smoothly.'), (opt_bcd, "BCD Edit"))
            customtkinter.CTkButton(master=self, text="Optimize", width=user32.GetSystemMetrics(0)-350,  height=50, command=Optimize).pack(pady=12, padx=10)
            
            
    class Res_Men(customtkinter.CTkFrame):
        def __init__(self , parent):
            super().__init__(master=parent, fg_color='transparent')     
            self.pack(expand=True, fill='both')
            
            customtkinter.CTkLabel(master=self, text= "Restorer", font=("Calibri Bold", 50), text_color="#F3EDEC").pack(pady=12, padx=10)
            customtkinter.CTkButton(master=self, text="Create Restore Point", width=user32.GetSystemMetrics(0)-350, height=50, command=CreateRestorePoint).pack(pady=12, padx=10)
            customtkinter.CTkButton(master=self, text="Use Restore Point", width=user32.GetSystemMetrics(0)-350, height=50, command=UseRestorePoint).pack(pady=12, padx=10)
    
    class Cre_Men(customtkinter.CTkFrame):
        def __init__(self , parent):
            super().__init__(master=parent, fg_color='transparent')     
            self.pack(expand=True, fill='both')
            
            customtkinter.CTkLabel(master=self, text= "Credits", font=("Calibri Bold", 50), text_color="#F3EDEC").pack(pady=12, padx=10)
            customtkinter.CTkLabel(master=self, text= "Developed And Programmed By - isaac_official", font=("Calibri Bold", 30), text_color="#F3EDEC").pack(pady=12, padx=10)
            customtkinter.CTkLabel(master=self, text= "Managed and Tested By - 3d12", font=("Calibri Bold", 30), text_color="#F3EDEC").pack(pady=12, padx=10)
            customtkinter.CTkButton(master=self, text="Join The Discord!", width=user32.GetSystemMetrics(0)-350, height=50, command=OpenDiscord).pack(pady=12, padx=10)      
                
    Menu(new_men)
    
    new_men.mainloop()
    
                

if Check_OS() == "Windows":
    

    if Install_Init_Package() == True:
        
        keyauthapp = keyauth()
        
        time.sleep(3)
        
        Install_Init_Stuffs()
        
        
        Installer(["pywin32", "customtkinter", "webbrowser"])
        
        
        if Is_Package_Installed("customtkinter"):
            import customtkinter
        else:
            print(f"{Fore.RED}[-] {Fore.WHITE}Package 'customtkinter' Is Not Installed, Re-Run The Program.")
            time.sleep(3)
            os.exit()
            
            
            
            
        
            
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Please Input Your Key On The UI.")
        
            

            
        #######################################################
        
        
        
        
            
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        root = customtkinter.CTk()
        root.title("star")
        root.geometry("340x240")
        
        
        
        
        ########################################################

        def Login(key):
            #TODO: Create License Login
            res = keyauthapp.license(key)
            
            if res['success'] == True:
                if res['message'] == "Logged in!":
                    subprocess.call("cls", shell=True)
                                        
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Key Valid, You Have {int(res['info']['subscriptions'][0]['timeleft']) // 60} minutes left.")
                    
                    root.destroy()
                    
                    time.sleep(1)
                                            
                    MainLoop()
                    
                else:
                    print(f"{Fore.RED}[-] {Fore.WHITE}Key Invalid.")
                    return
            else:
                print(res)
                print(f"{Fore.RED}[-] {Fore.WHITE}Key Invalid.")
                return
            
        def Submit_Login():
            license_key = entry.get()
            Login(license_key)
            
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=5, padx=5, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text= "Authorization System", font=("Calibri Bold", 30), text_color="#F3EDEC")
        label.pack(pady=12, padx=10)

        entry = customtkinter.CTkEntry(master=frame, corner_radius=3, placeholder_text="License Key", justify="left",)
        entry.pack(pady=20, padx=10)

        loginbtn = customtkinter.CTkButton(master=frame, text="Submit", command=Submit_Login)
        loginbtn.pack(pady=12, padx=10)

        root.mainloop()
        
        
                
        
        #######################################################
        
else:
    
    print(f"{Fore.RED}[-] {Fore.WHITE}Unsupported OS.")
