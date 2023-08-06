from llama.engine.llama import Llama
from llama.specification.specification import Spec
from llama.specification.context import Context

global_engine = None

def get_engine():
    global global_engine
    if global_engine is None:
        global_engine = HyperLlamaEngine()

    return global_engine

class HyperLlamaEngine:
    def __init__(self):
        self.graph = Graph(self)
        self.temperature = 0.0
        self.log = []

    def get_input(self, input_spec):
        input_value = self.graph.add_node(ValueNode(input_spec))
        self.graph.set_input(input_value)
        return input_value

    def run(self, input, output_spec):
        if isinstance(input, type):
            input = self.get_input(input)

        llama_node = self.graph.add_node(LlamaNode(input.get_type(), output_spec))

        self.graph.connect(input, llama_node)

        return llama_node

    def add_metric(self, input, metric_spec):
        metric_node = self.graph.add_node(MetricNode(input.get_type(), metric_spec))

        self.graph.connect(input, metric_node)

        return metric_node

    def get_field(self, input, field_name):
        get_field_node = self.graph.add_node(GetFieldNode(input.get_type(), field_name))

        self.graph.connect(input, get_field_node)

        return get_field_node

    def check_match(self, a, b):
        check_match_node = self.graph.add_node(CheckMatchNode(a, b))

        self.graph.connect(a, check_match_node)
        self.graph.connect(b, check_match_node)

        return check_match_node

    def fit(self, examples):
        # find a matching llm to fit
        input_spec = type(examples[0]["input"])
        output_spec = type(examples[0]["output"])

        matching_node = None

        for node in self.graph.nodes:
            #print("checking node", node)
            if type(node) != LlamaNode:
                continue

            if input_spec != node.input_spec:
                continue

            if output_spec != node.output_spec:
                continue

            matching_node = node

        return matching_node.fit(examples)

    def optimize(self):
        # Generate data at higher tempurature, log it
        for i in range(3):
            self.temperature = 0.1 * (i + 1)
            self.execute()
            self.log_data()

        self.temperature = 0.0

    def execute(self):
        self.values = []
        self.graph.sort()

        for index, node in enumerate(self.graph.nodes):
            #print("executing node", node)
            inputs = self.get_node_inputs(node)
            node.set_inputs(inputs)
            value = node.execute()
            self.values.append(value)

    def get_node_inputs(self, node):
        predecessors = node.get_predecessors()

        return [self.values[predecessor] for predecessor in predecessors]

    def log_data(self):
        self.log.append(self.values)

    def get_value(self, index):
        return self.values[index]

    def get_metrics(self):
        metrics = []

        for index, node in enumerate(self.graph.nodes):
            metrics.append(self.values[index])

        return metrics

    def make_program(self, input):
        return Program(self, input)

class Program:
    def __init__(self, engine, output_value):
        self.engine = engine
        self.output_value = output_value

    def __call__(self, input):
        for node in self.engine.graph.nodes:
            if type(node) == ValueNode:
                node.value = input
                break

        return self.output_value

class Graph:
    def __init__(self, engine):
        self.engine = engine
        self.input_node = None
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        node.set_graph(self)
        self.nodes.append(node)
        return node

    def set_input(self, node):
        self.input_node = node

    def connect(self, a, b):
        self.edges.append((a.get_index(), b.get_index()))

    def sort(self):
        pass  # TODO: topologically sort the graph


class Node:
    def __init__(self):
        self.graph = None
        self.index = None

    def set_graph(self, graph):
        self.graph = graph
        self.index = len(graph.nodes)

    def get_index(self):
        assert self.index is not None
        return self.index

    def get_predecessors(self):
        predecessors = []

        for predecessor, successor in self.graph.edges:
            if successor == self.get_index():
                predecessors.append(predecessor)

        return predecessors

    def set_inputs(self, input_values):
        self.input_values = input_values

    def get(self):
        self.graph.engine.execute()
        return self.graph.engine.get_value(self.get_index())


class ValueNode(Node):
    def __init__(self, value_type):
        super().__init__()

        self.value = None
        self.value_type = value_type

    def execute(self):
        return self.value

    def get_type(self):
        return self.value_type

    def __str__(self):
        return f"Value {self.value} {self.value_type}"


class LlamaNode(Node):
    def __init__(self, input_spec, output_spec):
        super().__init__()

        self.llama = Llama()

        self.input_spec = input_spec
        self.output_spec = output_spec

    def execute(self):

        return self.llama.run(
            input=self.input_values[0],
            output_spec=self.output_spec,
            temperature=self.graph.engine.temperature,
        )

    def fit(self, examples):
        return self.llama.fit(examples)

    def get_type(self):
        return self.output_spec

    def __str__(self):
        return f"Running LLM on {self.input_spec} to {self.output_spec}"

class MetricNode(LlamaNode):
    def __init__(self, input_spec, output_spec):
        super().__init__(input_spec, output_spec)


class GetFieldNode(Node):
    def __init__(self, input_spec, field_name):
        super().__init__()

        self.input_spec = input_spec
        self.field_name = field_name

    def execute(self):
        return getattr(self.input_values[0], self.field_name)

    def __str__(self):
        return f"Getting field {self.field_name} from {self.input_spec}"


class Match(Spec):
    a: str = Context("the first string")
    b: str = Context("the second string")


class MatchResult(Spec):
    similarity: float = Context(
        "a number between 0.0 and 1.0 describing similarity of the input strings.  0.0 is no similarity, and 1.0 is a perfect match."
    )


class CheckMatchNode(Node):
    def __init__(self, a, b):
        super().__init__()

        self.llama = Llama()

        self.a = a
        self.b = b

    def execute(self):
        a = cast(self.input_values[0], str)
        b = cast(self.input_values[1], str)

        #print(f"Comparing: {a} & {b}")

        result = self.llama.run(input=Match(a=a, b=b), output_spec=MatchResult)

        #print("Match result is:", result)
        return result

    def __str__(self):
        return f"Checking {self.a} & {self.b}"


def cast(value, target_type):
    if isinstance(value, target_type):
        return value

    if isinstance(value, Spec):
        assert len(value.__fields__.keys()) == 1
        field_name = next(iter(value.__fields__.keys()))
        field_value = getattr(value, field_name)
        return cast(field_value, target_type)

    assert False
