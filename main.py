import openai
import typer
from rich import print
from rich.table import Table

from config import api_key

def main():
    openai.api_key = api_key

    print("[bold green]ChatGPT API con Python[/bold green]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")
    print(table)

    context = {"role": "system", "content": "Eres un asistente muy util"}
    messages= [context]

    while True:

        content = __prompt()

        if content == "new":
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre que quieres hablar?")

    if prompt == "exit":
        salida = typer.confirm("¿Estas seguro?")
        if salida:
            print("[bold red]Hasta luego![/bold red]")
            raise typer.Abort()

        return __prompt()

    return prompt
if __name__ == "__main__":
    typer.run(main)