from utils import Utils
import tkinter as tk
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from tkinter.ttk import (Frame, Label)
from tkinter import (ttk, X, filedialog, messagebox, BOTH)

class UI(Frame):
    def __init__(self):
        self.utils = Utils()
        self.config = self.utils.read_json('config.ui')
        self.__entradas = {}
        self.__resp_entrada = {}
