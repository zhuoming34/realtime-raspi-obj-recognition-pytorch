"""
ImageNet labels
"""
from os import system
from json import loads
from constants import IMAGENET_LABEL_FILE

def load_imagenet_labels(label_file: str = IMAGENET_LABEL_FILE) -> dict:
    """
    Load 1000 imagenet labels from and return a dictionay
    """
    assert label_file

    with open(label_file) as f:
        labels = f.read()

    return loads(labels)


def show_top_estimations(output, classes: dict, number_of_classes: int = 5) -> str:
    assert len(classes) >= number_of_classes

    top = list(enumerate(output[0].softmax(dim=0)))
    top.sort(key=lambda x: x[1], reverse=True)

    top_one_est = classes[str(top[0][0])] 

    #system('clear')
    print(f"{'-'*20}\n {top_one_est}\n{'-'*20}")
    for idx, val in top[:number_of_classes]:
        print(f"{val.item()*100:.2f}% {classes[str(idx)]}")

    return top_one_est
