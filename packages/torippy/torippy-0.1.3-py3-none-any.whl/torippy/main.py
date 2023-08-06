from gui import screenshot_2click


if __name__ == "__main__":
    img = screenshot_2click()
    img.save("temp/sample.png")
