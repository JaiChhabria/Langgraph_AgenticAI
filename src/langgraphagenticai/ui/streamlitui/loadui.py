import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


# Creating a class
class LoadStreamLitUI:
    def __init__(self):
        self.config = Config() # Config class object
        self.user_controls = {}
