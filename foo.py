import control
print("control version %s" % control.__version__)
sys = control.tf(1,[1,1])
print(sys)
