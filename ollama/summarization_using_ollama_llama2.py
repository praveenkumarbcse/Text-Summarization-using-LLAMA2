import click
from openai import OpenAI

@click.command()
@click.option('-t', '--textfile', type=click.Path(exists=True), help='Path to the text file to summarize.')
@click.option('-i', '--inputtext', type=str, help='Direct text input to summarize (only if no file is provided).')
@click.option('-m', '--model', default='llama2', help='Name of the Ollama model to use (e.g., "llama2", "mistral").')
def summarize(textfile, inputtext, model):
    if not textfile:
        if inputtext:
            text = inputtext
        else:
            click.echo("Please provide a text file (-t) or direct input (-i).")
            return
    else:
        with open(textfile, 'r') as file:
            text = file.read()

    try:
        click.echo(f"Loading model '{model}'...")
        client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',
        )

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n{text}"}
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )

        click.echo(f"Model '{model}' loaded successfully!")
    except Exception as e:
        click.echo(f"An error occurred: {e}")
        return

    summary = ""
    for chunk in response:
        if chunk.choices[0].delta:
            summary += chunk.choices[0].delta.content
            click.echo(chunk.choices[0].delta.content, nl=False)

if __name__ == '__main__':
    summarize()
