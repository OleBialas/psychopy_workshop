from psychopy import visual

win = visual.Window()
fps = win.getActualFrameRate()
print(f"The measured frame rate is {fps} Hz")
print(f"Thus, 1 frame lasts for {1/fps} s")
win.close()
