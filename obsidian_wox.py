#encoding=utf8

import os
from wox import Wox,WoxAPI
from datetime import date


#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Main(Wox):
    
  obsidian_vault =os.path.join("P:\\", "obsidian")
  journal_folder = "Journal"
  timing_format="%Y-%m-%d"
  journalfile = os.path.join(obsidian_vault, journal_folder, date.today().strftime(timing_format)+'.md')
  message=""

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  # query is default function to receive realtime keystrokes from wox launcher
  def query(self,query):
   # results has a confirmation where key was added
    results = []
    results.append({
        "Title": "Obsidian Journal",
        "SubTitle": "Append to Journal today: {}".format(query),
        "IcoPath":"Images/obsidian_logo.png",
        "ContextData": "ctxdata",
        "JsonRPCAction": {
            'method': 'take_action',
            'parameters': ["{}".format(query)],
            'dontHideAfterAction': True
        }
    })
    
      
    return results

    # context_menu is default function called for ContextData where `data = ctxData`
  def context_menu(self, data):
      results = []
      results.append({
          "Title": "Context menu entry",
          "SubTitle": "Data: {}".format(data),
          "IcoPath":"Images/obsidian_logo.png"
      })
      return results

  def take_action(self, SomeArgument):

    if os.path.isfile(Main.journalfile):
      try:
        f = open(Main.journalfile, "a")
        f.write(SomeArgument + "\n")
      except IOError:
        print("File not accessible")
      finally:
        f.close()
    else:
      try:
        f = open(Main.journalfile, "w")
        f.write(SomeArgument + "\n")
      except IOError:
        print("File not accessible")
      finally:
        f.close()

    return None

  #Following statement is necessary
if __name__ == "__main__":
  Main()