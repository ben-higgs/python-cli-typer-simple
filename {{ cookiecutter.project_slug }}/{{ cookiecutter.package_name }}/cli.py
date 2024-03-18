from typer import Typer

app = Typer(
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]}
)


@app.command()
def main():
    print("Hello, cli")


if __name__ == '__main__':
    app()
