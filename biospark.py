import json

def load_ideas():
    with open('idea_base.json', 'r') as file:
        return json.load(file)

def analyze_idea(user_input, ideas):
    user_input = user_input.lower()
    for idea_key, info in ideas.items():
        if any(keyword in user_input for keyword in info["keywords"]):
            print(f"\n Idea match found: {idea_key.title()}")
            print(f" Status: {info['status']}")
            print(f" Summary: {info['summary']}")
            print(" Steps to get started:")
            for step in info["start_steps"]:
                print(f"- {step}")
            return
    print("\n Hmm, this seems like a fresh concept! You may be the first to explore it. Start with small experiments and literature review!")

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    user_idea = input(" Enter your biology-based idea: ")
    ideas = load_ideas()
    analyze_idea(user_idea, ideas)
