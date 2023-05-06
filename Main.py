import tkinter as tk
import Info

class Lifecycle(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x600")
        self.bg = "#212121"
        self.fg = "#ffffff"
        self.title("Interactive Waterfall Model")
        self.iconbitmap("logo.ico")
        self.minsize(width=800,height=600)
        self.maxsize(width=800,height=600)
        self.infoTitle = None
        self.information = None
        self.page = None
        self.config(background=self.bg)
        self._frame = None
        self.switchFrame(MainPage)

    def switchFrame(self, frameClass):
        newFrame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = newFrame
        self._frame.pack()

class MainPage(tk.Frame):
    def __init__(self, master):
        self.title = None
        self.information = None
        tk.Frame.__init__(self, master, bg=master.bg)
        imgCanvas = tk.Canvas(self, width=800, height=600, bg=master.bg, highlightthickness = 0, bd = 0)
        imgCanvas.pack()
        title = tk.Label(text = "Waterfall Life Cycle", bg=master.bg, fg=master.fg, font=("Arial 25 underline"))
        imgCanvas.create_window(400, 25, window=title)
        self.img = tk.PhotoImage(file="Waterfall Assets/WaterfallModel.png")
        imgCanvas.create_image(400, 300, image=self.img)
        
        # Image Buttons
        self.reqImg = tk.PhotoImage(file="Waterfall Assets/Req.png")
        reqButton = tk.Button(self, anchor = 'w', width=240, height=80, image=self.reqImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "req"))
        imgCanvas.create_window(5, 10, anchor = 'nw', window=reqButton)

        self.desImg = tk.PhotoImage(file="Waterfall Assets/Des.png")
        desButton = tk.Button(self, anchor = 'w', width=240, height=80, image=self.desImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "des"))
        imgCanvas.create_window(140, 134, anchor = 'nw', window=desButton)

        self.impImg = tk.PhotoImage(file="Waterfall Assets/Imp.png")
        impButton = tk.Button(self, anchor = 'w', width=240, height=80, image=self.impImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "imp"))
        imgCanvas.create_window(275, 258, anchor = 'nw', window=impButton)

        self.verImg = tk.PhotoImage(file="Waterfall Assets/Ver.png")
        verButton = tk.Button(self, anchor = 'w', width=240, height=80, image=self.verImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "ver"))
        imgCanvas.create_window(411, 384, anchor = 'nw', window=verButton)

        self.maiImg = tk.PhotoImage(file="Waterfall Assets/Mai.png")
        maiButton = tk.Button(self, anchor = 'w', width=240, height=80, image=self.maiImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "mai"))
        imgCanvas.create_window(550, 508, anchor = 'nw', window=maiButton)

        self.arrowImg = tk.PhotoImage(file="Arrow.png")
        arrowButton = tk.Button(self, anchor = 'w', width=100, height=100, image=self.arrowImg,
                                bg=master.bg, highlightthickness = 0, bd = 0,
                                command = lambda: master.switchFrame(ProjectCycle))
        imgCanvas.create_window(690, 240, anchor = 'nw', window=arrowButton)

    def infoDef(self, master, op):
        if op == "req":
            master.infoTitle = "Requirements"
            master.information = Info.req
        elif op == "des":
            master.infoTitle = "Design"
            master.information = Info.des
        elif op == "imp":
            master.infoTitle = "Implementation"
            master.information = Info.imp
        elif op == "ver":
            master.infoTitle = "Verification"
            master.information = Info.ver
        elif op == "mai":
            master.infoTitle = "Maintenance"
            master.information = Info.mai
        master.page = "water"
        self.master.switchFrame(InfoFrame)

class ProjectCycle(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=master.bg)

        canvas = tk.Canvas(self, width=800, height=600, bg=master.bg, highlightthickness = 0, bd = 0)
        canvas.pack()
        title = tk.Label(text = "Project Management Life Cycle", bg=master.bg, fg=master.fg, font=("Arial 25 underline"))
        canvas.create_window(400, 25, window=title)

        # Image Buttons
        self.iniImg = tk.PhotoImage(file="Project Assets/Ini.png")
        iniButton = tk.Button(self, anchor = 'w', width=129, height=133, image=self.iniImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "ini"))
        canvas.create_window(25, 300, anchor = 'w', window=iniButton)

        self.plaImg = tk.PhotoImage(file="Project Assets/Pla.png")
        plaButton = tk.Button(self, anchor = 'w', width=129, height=133, image=self.plaImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "pla"))
        canvas.create_window(180, 300, anchor = 'w', window=plaButton)

        self.exeImg = tk.PhotoImage(file="Project Assets/Exe.png")
        exeButton = tk.Button(self, anchor = 'w', width=129, height=133, image=self.exeImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "exe"))
        canvas.create_window(335, 300, anchor = 'w', window=exeButton)

        self.monImg = tk.PhotoImage(file="Project Assets/Mon.png")
        monButton = tk.Button(self, anchor = 'w', width=129, height=133, image=self.monImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "mon"))
        canvas.create_window(490, 300, anchor = 'w', window=monButton)

        self.cloImg = tk.PhotoImage(file="Project Assets/Clo.png")
        cloButton = tk.Button(self, anchor = 'w', width=129, height=133, image=self.cloImg,
                              bg=master.bg, highlightthickness = 0, bd = 0,
                              command = lambda: self.infoDef(master, "clo"))
        canvas.create_window(645, 300, anchor = 'w', window=cloButton)

        self.arrowImg = tk.PhotoImage(file="ArrowLeft.png")
        arrowButton = tk.Button(self, anchor = 'w', width=100, height=100, image=self.arrowImg,
                                bg=master.bg, highlightthickness = 0, bd = 0,
                                command = lambda: master.switchFrame(MainPage))
        canvas.create_window(10, 500, anchor = 'nw', window=arrowButton)

    def infoDef(self, master, op):
        if op == "ini":
            master.infoTitle = "Initiation"
            master.information = Info.ini
        elif op == "pla":
            master.infoTitle = "Planning"
            master.information = Info.pla
        elif op == "exe":
            master.infoTitle = "Execution"
            master.information = Info.exe
        elif op == "mon":
            master.infoTitle = "Monitoring and Controlling"
            master.information = Info.mon
        elif op == "clo":
            master.infoTitle = "Closing"
            master.information = Info.clo
        master.page = "project"
        self.master.switchFrame(InfoFrame)

class InfoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=master.bg)

        canvas = tk.Canvas(self, width=800, height=600, bg=master.bg, highlightthickness = 0, bd = 0)
        canvas.pack()

        title = tk.Label(text = master.infoTitle, bg=master.bg, fg=master.fg, font=("Arial 25 underline"))
        canvas.create_window(400, 25, window=title)
        info = tk.Label(text = master.information, bg=master.bg, fg=master.fg, font=("Arial", 14))
        canvas.create_window(400, 60, window=info, anchor=tk.N)

        if master.page == "project":
            backButton = tk.Button(self, anchor = "w", text = "Back", width=8, height=2,
                                   command = lambda: master.switchFrame(ProjectCycle))
        else:
            backButton = tk.Button(self, anchor = "w", text = "Back", width=8, height=2,
                                   command = lambda: master.switchFrame(MainPage))
        canvas.create_window(725, 550, anchor='nw', window=backButton)
        

lifecycle = Lifecycle()
lifecycle.mainloop()
