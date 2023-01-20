from model_checking import modelCheck

if __name__ != "__main__":
    print("Driver run from external context. terminated")
    exit(0)

print("Driver start.")

modelCheck()
