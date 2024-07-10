import os

import click
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option('-t', '--textfile', type=click.Path(exists=True))
@click.option('-i', '--inputtext', type=str)
def summarize(textfile, inputtext):
    if not textfile and not inputtext:
        click.echo("Please provide a text file (-t) or direct input (-i).")
        return

    text = inputtext or open(textfile, 'r').read()
    genai.configure(api_key=os.getenv("API_KEY")) # Replace with your API key
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    prompt = f"Summarize the following text in a concise and informative way:\n\n{text}"

    click.echo("Connecting to Google Gemini AI...")
    response = model.generate_content(prompt)
    if response.text:
        click.echo("Connected to Google Gemini AI!")
        click.echo("\nSummary for the given Prompt:")
        click.echo(response.text)
    else:
        click.echo("No summary could be generated.")

if __name__ == '__main__':
    summarize()
