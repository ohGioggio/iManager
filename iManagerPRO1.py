#Import Libraries
from tkinter import * 
import pyAesCrypt
import os
import os.path

#Defining Class Section
class Global:
    def __init__(self):
        self.pathFinder()
        self.appFont()
    def appFont(self):
        global fontTitle
        global fontLabel
        global fontLabelSize
        global fontEntrySize
        global fontButton
        global fontButtonSize
        global fontTitleSize
        fontTitle = "Aware"
        fontLabel = "Arial Rounded MT Bold"
        fontLabelSize = 12
        fontEntrySize = 20
        fontButton = "a Astro Space"
        fontButtonSize = 16
        fontTitleSize = 60
    def appColorNormal(self):
        global AppBackgroundColor
        global AppButtonColor
        global AppTitleColor
        global AppTextSuccessColor
        global AppTextInvalidColor
        AppBackgroundColor = "#8acdec"
        AppButtonColor = "#47b0e1"
        AppTitleColor = "white"
        AppTextSuccessColor = "#11672c"
        AppTextInvalidColor = "#991930"
    def appColorLight(self):
        global AppBackgroundColor
        global AppButtonColor
        global AppTitleColor
        global AppTextSuccessColor
        global AppTextInvalidColor
        AppBackgroundColor = "#B2F7EF"
        AppButtonColor = "#7BDFF2"
        AppTitleColor = "#EFF7F6"
        AppTextSuccessColor = "#11672c"
        AppTextInvalidColor = "#991930"
    def appColorDark(self):
        global AppBackgroundColor
        global AppButtonColor
        global AppTitleColor
        global AppTextSuccessColor
        global AppTextInvalidColor
        AppBackgroundColor = "#231F20" #intellectual_grey
        AppButtonColor = "#AD974F" #light_gold
        AppTitleColor = "#EAEAEA" #dark_grey
        AppTextSuccessColor = "#11672c"
        AppTextInvalidColor = "#991930"
    def pathFinder(self):
        global appdata_path
        global iManagerPRO
        global account_path
        global icon_path
        global register_path
        global sources_path
        global theme_path
        appdata_path = os.getenv('LOCALAPPDATA')
        iManagerPRO_path = os.path.join(appdata_path, "iManagerPRO")
        account_path = os.path.join(iManagerPRO_path, "account") #
        if not os.path.exists(account_path):
            os.makedirs(account_path)
        icon_path = os.path.join(iManagerPRO_path, "icon") #
        register_path = os.path.join(iManagerPRO_path, "register") #
        sources_path = os.path.join(iManagerPRO_path, "sources") #
        if not os.path.exists(sources_path):
            os.makedirs(sources_path)
        theme_path = os.path.join(iManagerPRO_path, "theme") #
globalLayout = Global()

class CryptingFiles():
    def __init__(self):
        global bufferSize
        global en_pass
        bufferSize = 64 * 1024
        en_pass = "root"
    def encrypting(self, file, crypt_path):
        file_name = file + ".aes"
        file_path = os.path.join(crypt_path, file)
        file_name_path = os.path.join(crypt_path, file_name)
        pyAesCrypt.encryptFile(file_path, file_name_path, en_pass, bufferSize)
        complete_path = os.path.join(crypt_path, file)
        os.remove(complete_path)
    def decrypting(self, file, crypt_path):
        file_name = file + ".aes"
        file_path = os.path.join(crypt_path, file)
        file_name_path = os.path.join(crypt_path, file_name)
        pyAesCrypt.decryptFile(file_name_path, file_path, en_pass, bufferSize)
        complete_path = os.path.join(crypt_path, file_name)
        os.remove(complete_path)
crypting = CryptingFiles()
        
class TkinterConfig():
    def spacerConfig(self, spacer, h):
        spacer.config(
            text="", 
            bg=AppBackgroundColor, 
            fg=AppTitleColor, 
            width=300, 
            height=h,
            font=(fontLabel, fontLabelSize)
            )
    def titleConfig(self, title, txt, h):
        title.config(
            text=txt.upper(), 
            bg=AppBackgroundColor, 
            fg=AppTitleColor, 
            width=300, 
            height=h, 
            font=(fontTitle, fontTitleSize)
            )
    def labelConfig(self, label, txt, h):
        label.config(
            text=txt, 
            fg=AppTitleColor, 
            bg=AppBackgroundColor, 
            width=300, 
            height=h, 
            font=(fontButton, fontLabelSize)
            )
    def entryConfig(self, entry, VAR):
        entry.config(
            width=12, 
            borderwidth=0, 
            font=(fontButton, fontEntrySize), 
            textvariable=VAR, 
            bd=1
            )
    def buttonConfig(self, button, txt):
        button.config(
            bg=AppButtonColor, 
            fg=AppTitleColor, 
            activebackground=AppBackgroundColor, 
            activeforeground=AppBackgroundColor, 
            borderwidth=0,
            text=txt, 
            font=(fontButton, fontButtonSize), 
            bd=0, 
            highlightthickness=0,
            height=1, 
            width=16
            )
    def menuConfig(self, menu, txt):
        menu.config(
            bg=AppButtonColor, 
            fg=AppTitleColor, 
            activebackground=AppButtonColor, 
            activeforeground=AppTitleColor, 
            borderwidth=0,
            text=txt, 
            font=(fontButton, fontButtonSize), 
            bd=0, 
            highlightthickness=0,
            height=1, 
            width=16
            )
tkinterConfigCall = TkinterConfig()

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginScreen)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        new_frame.config(bg=AppBackgroundColor)
        self._frame.pack()
        
class LoginScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.title('iManager - Account Login')
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 1)
        loginScreenSpacer.pack()
        
        loginScreenTitle = Label(self)
        tkinterConfigCall.titleConfig(loginScreenTitle, "iManager", 2)
        loginScreenTitle.pack()
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 1)
        loginScreenSpacer.pack()
        
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()
        global username_login_entry
        global password_login_entry
    
        username_label = Label(self)
        tkinterConfigCall.labelConfig(username_label, "Username", 1)
        username_label.pack()
        
        username_login_entry = Entry(self)
        tkinterConfigCall.entryConfig(username_login_entry, username_verify)
        username_login_entry.pack()
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 1)
        loginScreenSpacer.pack()
        
        password_label = Label(self)
        tkinterConfigCall.labelConfig(password_label, "Password", 1)
        password_label.pack()
        
        password_login_entry = Entry(self, show= '*')
        tkinterConfigCall.entryConfig(password_login_entry, password_verify)
        password_login_entry.pack()
        
        global login_result
        login_result = Label(self)
        tkinterConfigCall.spacerConfig(login_result, 2)
        login_result.pack()
        
        login_button = Button(self, command=lambda: self.login_verify())
        tkinterConfigCall.buttonConfig(login_button, 'LOGIN')
        login_button.pack()
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 1)
        loginScreenSpacer.pack()
        
        #admin = Button(self, command=lambda: master.switch_frame(MainWindow))
        #tkinterConfigCall.buttonConfig(admin, 'admin')
        #admin.pack()
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 1)
        loginScreenSpacer.pack()
        
        global registration
        global verification
        register_path_name = os.path.join(register_path, "reG")
        crypting.decrypting("reG", register_path)
        registration = open(register_path_name, "r")
        verification = registration.read()

        if "0" in verification: #If the file number is 0:
        #Register Button
            register_button = Button(self, command=lambda: master.switch_frame(RegisterWindow))
            tkinterConfigCall.buttonConfig(register_button, 'REGISTER')
            register_button.pack() #Show Registration Button
            registration.close()
            crypting.encrypting("reG", register_path)
        elif "1" in verification: #If the file number is 1:
            registration.close()
            crypting.encrypting("reG", register_path)
            pass #Don't show Registration Button
        else: #Else:
            registration.close()
            crypting.encrypting("reG", register_path)
            pass #Nothing
        
        loginScreenSpacer = Label(self)
        tkinterConfigCall.spacerConfig(loginScreenSpacer, 6)
        loginScreenSpacer.pack()
        
    def login_verify(self): #Verify the Register Informations
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        username_crypt = username1 + ".aes"
        username_account_path = os.path.join(account_path, "account")
        
        #list_of_files = os.listdir(account_path)
        
        crypting.decrypting("account", account_path)
        file1 = open(username_account_path, "r")
        verify = file1.read().splitlines()
        file1.close()
        crypting.encrypting("account", account_path)
        if username1 == verify[0]:
            if password1 == verify[1]:
                self.login_success() #Call the Function related to Login Success if Username and Password Match.
            else:
                self.password_not_recognised() #Call the Function related to Invalid Password if Password is Incorrect.
        else:
            self.user_not_found() #Call the Function related to Invalid Username if Username is Incorrect.

    def login_success(self): #Update the Login status as Success
        login_result.config(text="Login Success", fg=AppTextSuccessColor)
        app.switch_frame(MainWindow)
        #select_screen() #Open the Select Screen Window

    def password_not_recognised(self): #Update the Login status as Invalid Password
        login_result.config(text="Invalid Password", fg=AppTextInvalidColor)
 
    def user_not_found(self): #Update the Login status as Invalid Username
        login_result.config(text="Invalid Username", fg=AppTextInvalidColor)

class RegisterWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager - Account Register')
        
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        
        registerWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(registerWindowSpacer, 1)
        registerWindowSpacer.pack()
        
        registerWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(registerWindowTitle, "Register".upper(), 2)
        registerWindowTitle.pack()
        
        registerWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(registerWindowSpacer, 1)
        registerWindowSpacer.pack()
        
        username_label = Label(self)
        tkinterConfigCall.labelConfig(username_label, "Username", 1)
        username_label.pack()

        username_entry = Entry(self)
        tkinterConfigCall.entryConfig(username_entry, username)
        username_entry.pack()
        
        registerWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(registerWindowSpacer, 1)
        registerWindowSpacer.pack()
        
        password_label = Label(self)
        tkinterConfigCall.labelConfig(password_label, "Password", 1)
        password_label.pack()
        
        password_entry = Entry(self, show='*')
        tkinterConfigCall.entryConfig(password_entry, password)
        password_entry.pack()
        
        global register_result
        register_result = Label(self)
        tkinterConfigCall.spacerConfig(register_result, 2)
        register_result.pack()
        
        registerWindowRegisterButton = Button(self, command=lambda: self.register_user())
        tkinterConfigCall.buttonConfig(registerWindowRegisterButton, 'REGISTER')
        registerWindowRegisterButton.pack()
        
        registerWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(registerWindowSpacer, 1)
        registerWindowSpacer.pack()
        
        registerWindowBackButton = Button(self, command=lambda: master.switch_frame(LoginScreen))
        tkinterConfigCall.buttonConfig(registerWindowBackButton, 'BACK')
        registerWindowBackButton.pack()
    
        registerWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(registerWindowSpacer, 6)
        registerWindowSpacer.pack()
    
    def register_user(self): #Save the Register Informations
        global username_info
        global password_info
        username_info = username.get()
        password_info = password.get()

        if username_info != "":
            if password_info != "":
                self.register_success()
            else:
                self.password_not_available()
        else:
            self.username_not_available()
        
    def register_success(self):
        username_path = os.path.join(account_path, "account")
        file = open(username_path, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        crypting.encrypting("account", account_path)
        register_result.config(text="Registration Completed", fg=AppTextSuccessColor)
        
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        global registration_completed
        reg_register_path = os.path.join(register_path, "reG")
        crypting.decrypting("reG", register_path)
        registration_completed = open(reg_register_path, "w")
        registration_completed.seek(0)
        registration_completed.truncate()
        registration_completed.write("1")
        registration_completed.close()
        crypting.encrypting("reG", register_path)
    def password_not_available(self):
        register_result.config(text="Invalid Password", fg=AppTextInvalidColor)
        
    def username_not_available(self):
        register_result.config(text="Invalid Username", fg=AppTextInvalidColor)
        
class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager by GioeleAllievi, Inc.')
        
        global new_source_source
        global new_source_password
        global new_source_entry
        global new_password_entry
        new_source_source = StringVar()
        new_source_password = StringVar()
        new_source_entry = StringVar()
        new_password_entry = StringVar()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()
        
        mainWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(mainWindowTitle, "iManager", 2)
        mainWindowTitle.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()
        
        mainWindowNewSourceButton = Button(self, command=lambda: master.switch_frame(NewSourceWindow))
        tkinterConfigCall.buttonConfig(mainWindowNewSourceButton, 'New Source')
        mainWindowNewSourceButton.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()
        
        mainWindowEditSourceButton = Button(self, command=lambda: master.switch_frame(EditSourceWindow))
        tkinterConfigCall.buttonConfig(mainWindowEditSourceButton, 'Edit Source')
        mainWindowEditSourceButton.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()

        mainWindowDeleteSourceButton = Button(self, command=lambda: master.switch_frame(DeleteSourceWindow))
        tkinterConfigCall.buttonConfig(mainWindowDeleteSourceButton, 'Delete Source')
        mainWindowDeleteSourceButton.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()
        
        mainWindowSearchSourceButton = Button(self, command=lambda: master.switch_frame(SearchSourceWindow))
        tkinterConfigCall.buttonConfig(mainWindowSearchSourceButton, 'Search Source')
        mainWindowSearchSourceButton.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 1)
        mainWindowSpacer.pack()
        
        mainWindowChangeThemeButton = Button(self, command=lambda: master.switch_frame(SettingsWindow))
        tkinterConfigCall.buttonConfig(mainWindowChangeThemeButton, 'Settings')
        mainWindowChangeThemeButton.pack()
        
        mainWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(mainWindowSpacer, 15)
        mainWindowSpacer.pack()

class NewSourceWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager - New Source')
        
        global new_source_source
        global new_source_password
        global new_source_entry
        global new_password_entry
        
        new_source_source = StringVar()
        new_source_password = StringVar()
        new_source_entry = StringVar()
        new_password_entry = StringVar()
    
        newSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(newSourceWindowSpacer, 1)
        newSourceWindowSpacer.pack()
        
        newSourceWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(newSourceWindowTitle, "New Source", 2)
        newSourceWindowTitle.pack()
        
        newSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(newSourceWindowSpacer, 1)
        newSourceWindowSpacer.pack()
        
        source_label = Label(self)
        tkinterConfigCall.labelConfig(source_label, "Source", 1)
        source_label.pack()

        new_source_entry = Entry(self)
        tkinterConfigCall.entryConfig(new_source_entry, new_source_source)
        new_source_entry.pack()
        
        newSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(newSourceWindowSpacer, 1)
        newSourceWindowSpacer.pack()
        
        password_label = Label(self)
        tkinterConfigCall.labelConfig(password_label, "Password", 1)
        password_label.pack()
        
        new_password_entry = Entry(self, show='*')
        tkinterConfigCall.entryConfig(new_password_entry, new_source_password)
        new_password_entry.pack()
        
        global new_source_result
        new_source_result = Label(self)
        tkinterConfigCall.spacerConfig(new_source_result, 2)
        new_source_result.pack()
        
        newSourceWindowSaveButton = Button(self, command=lambda: self.input_new_source_database())
        tkinterConfigCall.buttonConfig(newSourceWindowSaveButton, 'SAVE')
        newSourceWindowSaveButton.pack()
        
        newSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(newSourceWindowSpacer, 1)
        newSourceWindowSpacer.pack()
        
        newSourceWindowBackButton = Button(self, command=lambda: master.switch_frame(MainWindow))
        tkinterConfigCall.buttonConfig(newSourceWindowBackButton, 'BACK')
        newSourceWindowBackButton.pack()
        
        newSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(newSourceWindowSpacer, 15)
        newSourceWindowSpacer.pack()
        
    def input_new_source_database(self): #Add the New Source to Database
        new_source_username_info = new_source_source.get()
        new_source_password_info = new_source_password.get()
    
        if new_source_username_info != "":
            completeName = os.path.join(sources_path, new_source_username_info) # MODIFICARE PATH
            
            file1 = open(completeName, "w")
            file1.write(new_source_username_info + "\n")
            file1.write(new_source_password_info)
            file1.close()
            crypting.encrypting(new_source_username_info, sources_path)
            
            new_source_entry.delete(0, END)
            new_password_entry.delete(0, END)
            new_source_result.config(text="Source Saved", fg=AppTextSuccessColor)
        else:
            new_source_result.config(text="")

class EditSourceWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager - Edit Source')
        
        global edit_source_source
        global edit_source_password
        global edit_source_entry
        global edit_password_entry
        
        edit_source_source = StringVar()
        edit_source_password = StringVar()
        edit_source_entry = StringVar()
        edit_password_entry = StringVar()
    
        editSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(editSourceWindowSpacer, 1)
        editSourceWindowSpacer.pack()
        
        editSourceWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(editSourceWindowTitle, "Edit Source", 2)
        editSourceWindowTitle.pack()
        
        editSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(editSourceWindowSpacer, 1)
        editSourceWindowSpacer.pack()

        source_label = Label(self)
        tkinterConfigCall.labelConfig(source_label, "Source", 1)
        source_label.pack()

        edit_source_entry = Entry(self)
        tkinterConfigCall.entryConfig(edit_source_entry, edit_source_source)
        edit_source_entry.pack()
        
        editSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(editSourceWindowSpacer, 1)
        editSourceWindowSpacer.pack()

        password_label = Label(self)
        tkinterConfigCall.labelConfig(password_label, "Password", 1)
        password_label.pack()

        edit_password_entry = Entry(self, show='*')
        tkinterConfigCall.entryConfig(edit_password_entry, edit_source_password)
        edit_password_entry.pack()
        
        global edit_source_result
        edit_source_result = Label(self)
        tkinterConfigCall.spacerConfig(edit_source_result, 2)
        edit_source_result.pack()
        
        editSourceWindowSaveButton = Button(self, command=lambda: self.input_edit_source_database())
        tkinterConfigCall.buttonConfig(editSourceWindowSaveButton, 'SAVE')
        editSourceWindowSaveButton.pack()
        
        editSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(editSourceWindowSpacer, 1)
        editSourceWindowSpacer.pack()
        
        editSourceWindowBackButton = Button(self, command=lambda: master.switch_frame(MainWindow))
        tkinterConfigCall.buttonConfig(editSourceWindowBackButton, 'BACK')
        editSourceWindowBackButton.pack()
        
        editSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(editSourceWindowSpacer, 15)
        editSourceWindowSpacer.pack()
        
    def input_edit_source_database(self): #Edit an Existing Source in Database
        edit_source_username_info = edit_source_source.get()
        edit_source_password_info = edit_source_password.get()
        source_crypt = edit_source_username_info + ".aes"
        
        list_of_files = os.listdir(sources_path)
        if source_crypt in list_of_files:
            crypting.decrypting(edit_source_username_info, sources_path)
            completeName = os.path.join(sources_path, edit_source_username_info)
            
            file2 = open(completeName, "w")
            file2.seek(0)
            file2.truncate()
            file2.write(edit_source_username_info + "\n")
            file2.write(edit_source_password_info)
            file2.close()
            crypting.encrypting(edit_source_username_info, sources_path)
            edit_source_entry.delete(0, END)
            edit_password_entry.delete(0, END)
            edit_source_result.config(text="Source Edited", fg=AppTextSuccessColor)
        elif source_crypt == "":
            edit_source_result.config(text="", fg=AppTitleColor)
        else:
            edit_source_entry.delete(0, END)
            edit_password_entry.delete(0, END)
            edit_source_result.config(text="Source Not Found", fg=AppTextInvalidColor)
            
class DeleteSourceWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager - Delete Source')

        global delete_source_source
        global delete_source_entry
        delete_source_source = StringVar()
        delete_source_entry = StringVar()
        
        deleteSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(deleteSourceWindowSpacer, 1)
        deleteSourceWindowSpacer.pack()

        editSourceWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(editSourceWindowTitle, "Edit Source", 2)
        editSourceWindowTitle.pack()

        deleteSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(deleteSourceWindowSpacer, 1)
        deleteSourceWindowSpacer.pack()

        source_label = Label(self)
        tkinterConfigCall.labelConfig(source_label, "Source", 1)
        source_label.pack()

        delete_source_entry = Entry(self)
        tkinterConfigCall.entryConfig(delete_source_entry, delete_source_source)
        delete_source_entry.pack()
        
        global delete_source_result
        delete_source_result = Label(self)
        tkinterConfigCall.spacerConfig(delete_source_result, 2)
        delete_source_result.pack()

        deleteSourceWindowSaveButton = Button(self, command=lambda: self.input_delete_source_database())
        tkinterConfigCall.buttonConfig(deleteSourceWindowSaveButton, 'DELETE')
        deleteSourceWindowSaveButton.pack()

        deleteSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(deleteSourceWindowSpacer, 5)
        deleteSourceWindowSpacer.pack()

        deleteSourceWindowBackButton = Button(self, command=lambda: master.switch_frame(MainWindow))
        tkinterConfigCall.buttonConfig(deleteSourceWindowBackButton, 'BACK')
        deleteSourceWindowBackButton.pack()

        deleteSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(deleteSourceWindowSpacer, 15)
        deleteSourceWindowSpacer.pack()
        
    def input_delete_source_database(self): #Delete an Existing Source from Database
        delete_source_username_info = delete_source_source.get()
        source_crypt = delete_source_username_info + ".aes"
        
        list_of_files = os.listdir(sources_path)
        if source_crypt in list_of_files:
            completeName = os.path.join(sources_path, source_crypt)

            os.remove(completeName)
            delete_source_entry.delete(0, END)
            delete_source_result.config(text="Source {} Deleted".format(delete_source_username_info), fg=AppTextSuccessColor)
        elif source_crypt == "":
            delete_source_result.config(text="", fg=AppTitleColor)
        else:
            delete_source_entry.delete(0, END)
            delete_source_result.config(text="Source Not Found", fg=AppTextInvalidColor)

class SearchSourceWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=AppBackgroundColor)
        app.title('iManager - Search Source')

        global search_source_source
        global search_source_entry
        search_source_source = StringVar()
        search_source_entry = StringVar()

        searchSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(searchSourceWindowSpacer, 1)
        searchSourceWindowSpacer.pack()

        searchSourceWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(searchSourceWindowTitle, "Search Source", 2)
        searchSourceWindowTitle.pack()

        searchSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(searchSourceWindowSpacer, 1)
        searchSourceWindowSpacer.pack()

        source_label = Label(self)
        tkinterConfigCall.labelConfig(source_label, "Source", 1)
        source_label.pack()

        search_source_entry = Entry(self)
        tkinterConfigCall.entryConfig(search_source_entry, search_source_source)
        search_source_entry.pack()
        
        searchSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(searchSourceWindowSpacer, 1)
        searchSourceWindowSpacer.pack()

        searchSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(searchSourceWindowSpacer, 1)
        searchSourceWindowSpacer.pack()

        searchSourceWindowSearchButton = Button(self, command=lambda: self.input_search_source_database())
        tkinterConfigCall.buttonConfig(searchSourceWindowSearchButton, 'SEARCH')
        searchSourceWindowSearchButton.pack()
        
        global search_source_result
        search_source_result = Label(self)
        tkinterConfigCall.spacerConfig(search_source_result, 5)
        search_source_result.pack()
        
        searchSourceWindowBackButton = Button(self, command=lambda: master.switch_frame(MainWindow))
        tkinterConfigCall.buttonConfig(searchSourceWindowBackButton, 'BACK')
        searchSourceWindowBackButton.pack()
    
        searchSourceWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(searchSourceWindowSpacer, 15)
        searchSourceWindowSpacer.pack()
        
    def input_search_source_database(self): #Search an Existing Source in Database
        search_source_username_info = search_source_source.get()
        source_crypt = search_source_username_info + ".aes"
        
        list_of_files = os.listdir(sources_path)
        if source_crypt in list_of_files:
            crypting.decrypting(search_source_username_info, sources_path)
            completeName = os.path.join(sources_path, search_source_username_info)
            
            file3 = open(completeName, "r")
            search_resume = file3.read().splitlines()
            file3.close()
            crypting.encrypting(search_source_username_info, sources_path)
            search_source_entry.delete(0, END)
            search_source_result.config(text="Source: {}\nPassword: {}".format(search_resume[0], search_resume[1]), fg=AppTextSuccessColor)
        elif search_source_username_info == "":
            search_source_result.config(text="", fg=AppTitleColor)
        else:
            search_source_entry.delete(0, END)
            search_source_result.config(text="Source Not Found", fg=AppTextInvalidColor)

class SettingsWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg=AppBackgroundColor)
        app.title('iManager - Change Theme')
        
        global changed_password
        global change_password_entry
        changed_password = StringVar()
        change_password_entry = StringVar()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 1)
        settingsWindowSpacer.pack()
        
        settingsWindowTitle = Label(self)
        tkinterConfigCall.titleConfig(settingsWindowTitle, "Settings", 2)
        settingsWindowTitle.pack()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 1)
        settingsWindowSpacer.pack()
        
        change_password_label = Label(self)
        tkinterConfigCall.labelConfig(change_password_label, "Change Password", 1)
        change_password_label.pack()
        
        change_password_entry = Entry(self)
        tkinterConfigCall.entryConfig(change_password_entry, changed_password)
        change_password_entry.pack()
        
        global change_result
        change_result = Label(self)
        tkinterConfigCall.spacerConfig(change_result, 2)
        change_result.pack()
        
        settingsWindowDefaultButton = Button(self, command=lambda: self.change_password())
        tkinterConfigCall.buttonConfig(settingsWindowDefaultButton, 'CHANGE')
        settingsWindowDefaultButton.pack()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 1)
        settingsWindowSpacer.pack()
        
        change_theme_label = Label(self)
        tkinterConfigCall.labelConfig(change_theme_label, "Change Theme", 1)
        change_theme_label.pack()
        
        def select_theme(event):
            if clicked.get() == "LIGHT":
                popup.config(text = "Theme: LIGHT")
                self.change_theme_light()
            elif clicked.get() == "DEFAULT":
                popup.config(text = "Theme: DEFAULT")
                self.change_theme_default()
            elif clicked.get() == "DARK":
                popup.config(text = "Theme: DARK")
                self.change_theme_dark()
            
        options = ["LIGHT", "DEFAULT", "DARK"]
        
        global clicked
        clicked = StringVar()
        clicked.set(options[1])
        
        drop = OptionMenu(self, clicked, *options, command=select_theme)
        tkinterConfigCall.menuConfig(drop, "")
        drop.pack()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 1)
        settingsWindowSpacer.pack()
        
        global popup
        popup = Label(self)
        tkinterConfigCall.labelConfig(popup, "Theme", 2)
        popup.pack()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 1)
        settingsWindowSpacer.pack()
        
        settingsWindowBackButton = Button(self, command=lambda: master.switch_frame(MainWindow))
        tkinterConfigCall.buttonConfig(settingsWindowBackButton, 'BACK')
        settingsWindowBackButton.pack()
        
        settingsWindowSpacer = Label(self)
        tkinterConfigCall.spacerConfig(settingsWindowSpacer, 15)
        settingsWindowSpacer.pack()
    
    def change_password(self):
        new_password = changed_password.get()

        account_path_name = os.path.join(account_path, "account")
        crypting.decrypting("account", account_path)
        file4 = open(account_path_name, "r")
        account_info = file4.read().splitlines()
        file4.close()
        file4 = open(account_path_name, "w")
        file4.seek(0)
        file4.truncate()
        file4.write(account_info[0] + "\n")
        file4.write(new_password)
        file4.close()
        crypting.encrypting("account", account_path)
            
        change_result.config(text="Password Changed", fg=AppTextSuccessColor)
        change_password_entry.delete(0, END)
        
    def change_theme_light(self):
        theme_path_name = os.path.join(theme_path, "theme")
        crypting.decrypting("theme", theme_path)
        
        theme_list = open(theme_path_name, "w")
        theme_list.seek(0)
        theme_list.truncate()
        theme_list.write("light")
        theme_list.close()
        crypting.encrypting(theme_path_name, theme_path)
        check_theme_update()
        
    def change_theme_default(self):
        theme_path_name = os.path.join(theme_path, "theme")
        crypting.decrypting(theme_path_name, theme_path)
        
        theme_list = open(theme_path_name, "w")
        theme_list.seek(0)
        theme_list.truncate()
        theme_list.write("normal")
        theme_list.close()
        crypting.encrypting(theme_path_name, theme_path)
        check_theme_update()
    
    def change_theme_dark(self):
        theme_path_name = os.path.join(theme_path, "theme")
        crypting.decrypting(theme_path_name, theme_path)
        
        theme_list = open(theme_path_name, "w")
        theme_list.seek(0)
        theme_list.truncate()
        theme_list.write("dark")
        theme_list.close()
        crypting.encrypting(theme_path_name, theme_path)
        check_theme_update()
        
def check_theme_update():
    theme_path_name = os.path.join(theme_path, "theme")
    crypting.decrypting(theme_path_name, theme_path)
    theme_read = open(theme_path_name, "r")
    theme_reader = theme_read.read().splitlines()
    theme_read.close()
    crypting.encrypting(theme_path_name, theme_path)
    if "normal" in theme_reader:
        globalLayout.appColorNormal()
    elif "light" in theme_reader:
        globalLayout.appColorLight()
    elif "dark" in theme_reader:
        globalLayout.appColorDark()
check_theme_update()
    
if __name__ == "__main__":
    #App Config
    global app
    app = App()
    app.title('iManager - Account Login')
    positionRight = int(app.winfo_screenwidth()/2 - 400)
    positionDown = int(app.winfo_screenheight()/2 - 300)
    app.geometry('800x600+{}+{}'.format(positionRight, positionDown))
    app.configure(background=AppBackgroundColor)
    icon_path_name = os.path.join(icon_path, "logoGold.ico")
    app.iconbitmap(icon_path_name)
    app.resizable(False, False)
    app.mainloop()