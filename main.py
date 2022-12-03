import argparse
import openai
import pprint
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help='normal | code', required=True)
    parser.add_argument('-i', '--input', help='Input file or text')

    parser.add_argument('-o', '--output', help='Output file')
    return parser.parse_args()


def main():
    args = parse_args()
    openai.api_key = "API_KEY"

    # List available engines and create a dictionary of engine IDs and descriptions -> bug need to fix,
    # why does engines contain object and data? engines = openai.FineTune.list() engine_dict = {} for engine in
    # engines: engine_dict[engine.id] = engine.description

    # print("Available engines:")
    # for i, (engine_id, engine_description) in enumerate(engine_dict.items()):
    #     print(f"{i+1}. {engine_id} - {engine_description}")
    #
    # engine_index = int(input("Enter the number of the engine you want to use: ")) - 1
    # selected_engine = list(engine_dict.keys())[engine_index]

    prompt = ""
    if args.type == "normal":
        # If the user provided "normal" as the type, use the prompt as-is
        # Open the file and read its contents
        if os.path.exists(args.input):
            with open(args.input, "r") as file:
                prompt = file.read()
        else:
            prompt = args.input
    elif args.type == "code":
        # If the user provided "code" as the type, add a prefix to the prompt
        with open(args.input, "r") as file:
            prompt = prompt = "Explain what the following code does: \n\n" + file.read()

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=4000-len(prompt),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response in a readable and pretty way
    # print(response.choices[0].text)
    lines = response.choices[0].text.split('\n')

    # Loop over the lines in the string
    for line in lines:
        pprint.pprint(line.replace("\n\n", ""))
    # If the user provided an output file path, create a file at that path
    if args.output:
        with open(args.output, "w") as file:
            file.write(response.choices[0].text)


if __name__ == "__main__":
    main()
