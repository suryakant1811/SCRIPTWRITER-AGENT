from langchain_core.messages import HumanMessage
from workflow import build_graph

def main():
    graph = build_graph()

    user_input = input("Nickola Tesla inventions")

    initial_state = {
        "messages": [
            HumanMessage(content=user_input)
        ]
    }

    result = graph.invoke(initial_state)

    print("\n" + "=" * 60)
    print("HINGLISH SCRIPT")
    print("=" * 60)
    print(result["hinglish_script"])

if __name__ == "__main__":
    main()