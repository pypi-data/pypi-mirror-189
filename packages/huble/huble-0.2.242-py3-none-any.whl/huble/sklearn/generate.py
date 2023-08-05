from .process.handler import PreprocessHandler
from .train.handler import ModelHandler
from .essentials.handler import EssentialsHandler
from .graph import Graph


def generate_file(graph, target_column, task_type, colab=False):
    g = Graph(len(graph["nodes"]))
    map = {}
    j = 0
    while j < (len(graph["nodes"])):
        for i in graph["nodes"]:
            map[(i["id"])] = j
            j += 1
    map2 = {y: x for x, y in map.items()}
    for i in graph["edges"]:
        g.addEdge(map[i["source"]], map[i["target"]])
    res = g.topologicalSort()
    steps = []
    for i in res:
        steps.append(map2[i])
    steps_list = {}
    for i in steps:
        for j in range(len(graph["nodes"])):
            if i == graph["nodes"][j]["id"]:
                steps_list[(graph["nodes"][j]["data"]["name"])] = graph["nodes"][j]["data"]["node_type"]
    if colab:
        output_file = "/content/output.py"
    else:
        output_file = "output.py"
    preprocess_handler = PreprocessHandler()
    train_handler = ModelHandler()
    essentials_handler = EssentialsHandler()
    with open(output_file, "w") as f:
        f.write("import huble\n")
        f.write("from huble import Dataset\n")
        f.write("def run_experiment(experiment):\n")

        for i in steps_list:
            for node in graph["nodes"]:
                if i == node["data"]["name"]:
                    print(node["data"]["name"])
                    if steps_list[i] == "preprocess":
                        f.write(
                            "\t"
                            + preprocess_handler.return_function(
                                function_name=node["data"]["name"], params=node["data"]["parameters"]
                            )
                        )
                        f.write("\n")
                    elif (
                        steps_list[i] == "classification_model"
                        or steps_list[i] == "regression_model"
                        or steps_list[i] == "clustering_model"
                        or steps_list[i] == "model"
                    ):
                        f.write(
                            "\t"
                            + train_handler.return_function(
                                function_name=node["data"]["name"], params=node["data"]["parameters"]
                            )
                        )
                        f.write("\n")
                    elif steps_list[i] == "essential":
                        f.write(
                            "\t"
                            + essentials_handler.return_function(
                                function_name=node["data"]["name"], params=node["data"]["parameters"]
                            )
                        )
                        f.write("\n")
                    elif steps_list[i] == "evaluate_model":
                        f.write(
                            f"\tmetrics = huble.sklearn.evaluate_model(model=Model, test_dataset=test_dataset, target_column= '{target_column}', task_type='{task_type}' )"
                        )
                        f.write("\n")
                    elif steps_list[i] == "primary_dataset":
                        # TODO: Add support for other datasets
                        f.write(f"\tdata = Dataset('{node['data']['url']}')\n")
        f.write("\texperiment.upload_metrics(metrics)")
