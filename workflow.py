from langgraph.graph import StateGraph, START, END
from state import ContentState

from nodes.draft_writer import generate_draft
from nodes.editor import editor
from nodes.storyteller import storytellar
from nodes.translator import translator

def build_graph():
    """ Builds and compiles the LangGraph workflow. """
    graph = StateGraph(ContentState)

    graph.add_node("generate_draft", generate_draft)
    graph.add_node("editor", editor)
    graph.add_node("storyteller", storytellar)
    graph.add_node("translator", translator)

    graph.add_edge(START, "generate_draft")
    graph.add_edge("generate_draft", "editor")
    graph.add_edge("editor", "storyteller")
    graph.add_edge("storyteller", "translator")
    graph.add_edge("translator", END)

    return graph.compile()

