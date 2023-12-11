import csv

from deeppavlov import build_model, evaluate_model, configs

model = build_model("squad_ru_bert", download=True)


def load_context():
    with open("nlp/context.csv", mode="r", encoding='utf8') as file:
        print(file.name)
        return [message[0] for message in csv.reader(file)]


context = load_context()


def get_answer(question):
    result = model(context, [question])
    return result
