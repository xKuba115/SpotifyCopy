import json
from tkinter import *
import customtkinter
from functools import partial
import os

################################################################ACS FUNCTIONS ################################

def createAppSettings(AllowedUsers,SecretKey,ApplicationId,DbPass,ClubName,ClubId,IpAddress,Port): 
        BaseUrl = f"http://{IpAddress}:{Port}"
        ConnectionString = f"Data Source='127.0.0.1';Port=3306;Database='DB-EFI-ACS';UID='root';PWD='{DbPass}'"
        HangfireConnectionString = f"Data Source='127.0.0.1';Port=3306;Database='DB-EFI-HangFire';UID='root';PWD='{DbPass}';Allow User Variables=True"
        AccessControlServiceOptions = {
                "BaseUrl": BaseUrl,                                       
                "HubName": "access-control-hub",                                            
                "BiometricHubName": "biometric-hub",                                      
                "SecretKey": "ddddd",                        
                "AllowedUsers": AllowedUsers,
                "UseObsoleteEndpoints": "false",                                              
                "UseHttpRequestLogging": "false",                                            
                "UseHttpResponseLogging": "false"  
        }
        AccessManagementServiceOptions = {
        "ApiUrl": "ams",                                                
        "SecretKey": SecretKey,								
        "Scope": "scope",						
        "ApplicationId": ApplicationId,						
        "TenantId": "tenat"								
        }
        InternetConnectionCheckerOptions = {
                "PublicEndpoints":
                [
                "https://amsv2.efitness.com.pl/healthcheck"
                ]

        }
        DatabaseOptions = {                                                           
                "Provider": "MySQL",
                "ConnectionString": ConnectionString
        }
        ClubOptions = {  
                "ClubName": ClubName,
                "ClubId": ClubId}
        BiometricTemplateSyncOptions = {                                              
                "Mode": 1,                                                                  
                "CronExpression": "* */5 * * * *" 
        }
        HangfireOptions = {                                                          
                "HangfireStorageType" : "MySQL",
                "HangfireConnectionString": HangfireConnectionString
        }
        NLogOptions = {
                "ConsoleLogsLevel" : "Debug",
                "DeveloperLogsLevel" : "Debug",
                "MainLogsLevel": "Debug"
        }
        Logging = {
                "LogLevel": {
                "Default": "Debug",
                "System": "Warning", "Microsoft.EntityFrameworkCore.Database" : "Warning",
                "Microsoft.EntityFrameworkCore.Query" : "Warning",
                "Microsoft.EntityFrameworkCore.ChangeTracking" : "Warning",
                "Microsoft.EntityFrameworkCore.Infrastructure" : "Warning",
                "Microsoft.EntityFrameworkCore.Model" : "Warning",
                "Microsoft.AspNetCore.Mvc" : "Warning",
                "Microsoft.AspNetCore.Routing" : "Warning",
                "Microsoft.AspNetCore.Hosting" : "Warning",
                "Microsoft": "Information",
                "Hangfire": "Warning"
                }
        }
        RabbitMqOptions = {
                "IsEnabled": "true",
                "HostName": "rabbiturl",
                "Port": 8001,
                "IsSslEnabled": "true",
                "RetryInterval": 5000,
                "PrefetchCount": 250,
                "RoutingKey": "ams"
        }
        AppSettings = {
                "AccessControlServiceOptions":AccessControlServiceOptions,
                "AccessManagementServiceOptions":AccessManagementServiceOptions,
                "InternetConnectionCheckerOptions":InternetConnectionCheckerOptions,
                "DatabaseOptions":DatabaseOptions,
                "ClubOptions":ClubOptions,
                "BiometricTemplateSyncOptions":BiometricTemplateSyncOptions,
                "HangfireOptions":HangfireOptions,
                "RabbitMqOptions":RabbitMqOptions,
                "NLogOptions":NLogOptions,
                "Logging":Logging
        }
        return json.dumps(AppSettings, indent=4)
##############################################################################################################

################################################################TKinter Settings#############################

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  
root.geometry('450x500+1500+50')
root.resizable(False, False)

###############################################################################################################

#############################################################Frame switching###################################

amsFrame = customtkinter.CTkFrame(root, width=400, height=500)
serviceFrame = customtkinter.CTkFrame(root, width=400, height=500)
appSettingsFrame = customtkinter.CTkFrame(root, width=400, height=500)

def changeToAmsFrame():
    hideAllFrames()
    amsFrame.pack(fill="both", expand=1)

def changeToAppSettingsFrame():
    hideAllFrames()
    appSettingsFrame.pack(fill="both", expand=1)
    
def hideAllFrames():
    amsFrame.pack_forget()
    serviceFrame.pack_forget()
    appSettingsFrame.pack_forget()

counter = 0

def changeFrame(type):
    global counter
    if type =="next":
        counter = counter + 1
    elif type =="back":
        counter = counter - 1
    frames = [appSettingsFrame,amsFrame,serviceFrame]
    if counter >= 0:
        hideAllFrames()
        frames[counter].pack(fill="both", expand=1)


nextFrame = partial(changeFrame, "next")
backFrame = partial(changeFrame, "back")
###############################################################################################################

################################################################AppSettings Frame##############################

appSettingsFrame.pack(fill="both", expand=1)

allowedUsersLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="Allowed users:"),width=120, height=25,corner_radius=8)
allowedUsersLabel.place(x=0,y=10)
allowedUsersEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj allowedUsers")
allowedUsersEntry.pack(ipadx=10, ipady=10)

secretKeyLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="Secret key:"),width=120, height=25,corner_radius=8)
secretKeyLabel.place(x=0,y=55)
secretKeyEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj secretKey")
secretKeyEntry.pack(ipadx=10, ipady=10)


applicationIdLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="Application id:"),width=120, height=25,corner_radius=8)
applicationIdLabel.place(x=0,y=100)
applicationIdEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj applicationId")
applicationIdEntry.pack(ipadx=10, ipady=10)

dbPassLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="dbPass:"),width=120, height=25,corner_radius=8)
dbPassLabel.place(x=0,y=145)
dbPassEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj dbPass")
dbPassEntry.pack(ipadx=10, ipady=10)

clubNameLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="ClubName:"),width=120, height=25,corner_radius=8)
clubNameLabel.place(x=0,y=190)
clubNameEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj clubName")
clubNameEntry.pack(ipadx=10, ipady=10)

clubIdLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="ClubId:"),width=120, height=25,corner_radius=8)
clubIdLabel.place(x=0,y=235)
clubIdEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj clubId")
clubIdEntry.pack(ipadx=10, ipady=10)

IPAddressLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="ACS IP:"),width=120, height=25,corner_radius=8)
IPAddressLabel.place(x=0,y=280)
IPAddressEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj IP")
IPAddressEntry.pack(ipadx=10, ipady=10)

PortLabel = customtkinter.CTkLabel(master=appSettingsFrame, textvariable=StringVar(value="ACS PORT:"),width=120, height=25,corner_radius=8)
PortLabel.place(x=0,y=325)
PortEntry = customtkinter.CTkEntry(master=appSettingsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj port")
PortEntry.insert(0,"5000")
PortEntry.pack(ipadx=10, ipady=10)

######################################################################################################################

################################################################AMS Frame#############################################

def test():
    command = "test.exe"
    os.system(f"start cmd /c {command}")

PortLabel = customtkinter.CTkLabel(master=amsFrame, textvariable=StringVar(value="ACS PORT:"),width=120, height=25,corner_radius=8)
PortLabel.place(x=0,y=325)
PortEntry = customtkinter.CTkEntry(master=amsFrame, width=200, height=25, corner_radius=10, placeholder_text="Podaj port")
PortEntry.insert(0,"5000")
PortEntry.pack(ipadx=10, ipady=10)
backButton = customtkinter.CTkButton(master=amsFrame, text="Back", command=test)
backButton.place(x=20, y=20)

######################################################################################################################



################################################################Root Frame################################################################

backButton = customtkinter.CTkButton(master=root, text="Back", command=backFrame)
backButton.place(x=20, y=400)
nextButton = customtkinter.CTkButton(master=root, text="Next", command=nextFrame)
nextButton.place(x=250, y=400)

#########################################################################################################################

root.mainloop()


#pyinstaller --noconfirm --onefile --windowed --add-data "C:\Python311\Lib\site-packages\customtkinter;customtkinter"  "test.py"