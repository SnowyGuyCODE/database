def id():
  if "open notepad" in query:
    command = "notepad.exe"
    system(command)
  if "who is these" in query:
    speak("Deez Nuts")
  if "what nuts" in query:
    speak("Deez Nuts")
  if "who's these" in query:
    speak("Deez Nuts")
  if "who's deez" in query:
    speak("Deez Nuts")
  if "who is deez" in query:
    speak("Deez Nuts")
  if "these what" in query:
    speak("Deez Nuts")
  if "deez what" in query:
    speak("Deez Nuts")
  if "these who" in query:
    speak("Deez Nuts")
  if "deez who" in query:
    speak("Deez Nuts")
  if "silent mode" in query:
    speak("Lowering this program's volume.")
  if "your voice" in query:
    speak("If you want me to change my voice, you can do so by changing it in the program.")
  if "open jarvis" in query:
    speak("I highly recommend you do not proceed in this course of action. Are you sure you want to continue?")
    rq = input("(y/N): ")
    if rq == "y":
      system("cd " + MAINPATH + " && python main.py")
    elif rq == "N":
      cprint("[SYSTEM] Copy that. Aborting protocol.", "green")
    else:
      cprint(E6, "red")
  elif "open google" in query:
    command = "start https://www.google.com"
    system(command)
  elif "clear log" in query:
    clearLog()
  elif "clear the log" in query:
    clearLog()
  elif "play god of war" in query:
    speak("You should be studying to be doctor")
  elif "show me the schedule" in query:
    speak("Open it yourself.")
  elif "clear browser history" in query:
    speak("Shut the fuck up you dumb white monkey who likes oily men and plays minecraft on discord with no friends or family you dumb orphan you ain't batman or spiderman you absolute and total failure you are such a failure your nuts are gone cause they hate you and joe is not yo mama")
  elif "pause" in query:
    system("pause")
  elif "exit" in query:
    clearLog()
    looper = 10
  else:
    cprint(E1, "red")
