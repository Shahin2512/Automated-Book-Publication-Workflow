import typer
from ai_pipeline.writer import ai_write
from ai_pipeline.reviewer import ai_review

app = typer.Typer()

@app.command()
def run():
    with open("scrape/chapter1.txt",encoding="utf-8") as f: orig = f.read()
    spun = ai_write(orig)
    typer.echo("--- AI-WRITTEN DRAFT ---")
    typer.echo(spun)
    if typer.confirm("Edit AI content manually and press y when done?"):
        edit_txt = typer.prompt("Paste edited text")
    else:
        edit_txt = spun
    review = ai_review(edit_txt)
    typer.echo("--- AI REVIEW ---")
    typer.echo(review)
    if typer.confirm("Accept reviewed text as final?"):
        with open("human_loop/data/final.txt", "w", encoding="utf-8") as f:
            f.write(edit_txt)
        typer.echo("Saved final version.")

if __name__ == "__main__":
    app()
