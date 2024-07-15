import marimo

__generated_with = "0.6.19"
app = marimo.App()

@app.cell
def __(y):
    import myfile
    x, y = myfile.myfn(10)
    return x, y


if __name__ == "__main__":
    app.run()
