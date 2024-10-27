from web_maker.tree_of_thoughts.thought_node import ThoughtNode
from web_maker.gpt.main_model import GptService
import prompts

class TreeOfThought:
    def __init__(self, root_prompt=None, ongoing_prompt_template=None, ai_service=None, max_iterations=3, max_tokens=250, model="gpt-3.5-turbo"):
        self.root = ThoughtNode(root_prompt)
        self.max_iterations = max_iterations
        self.ai_service = ai_service or GptService(model=model)
        self.current_thoughts = [self.root]
        self.max_tokens = max_tokens
        self.prompt_template = ongoing_prompt_template

    def call_llm(self, prompt):
        try:
            response = self.ai_service.query_gpt(
                prompt,
                max_tokens=self.max_tokens,
            )
            return response
        except Exception as e:
            print(f"Error calling LLM: {e}")
            return []
        
    # def explore_thoughts(self, thought_nodes):
    #     new_thought_nodes = []
    #     for thought_node in thought_nodes:
    #         prompt = f"Given the current thought: '{thought_node.thought}', provide two concise next thoughts that evolve this idea further."
    #         response = self.call_llm(prompt)
    #         if response:
    #             new_thought_node = ThoughtNode(response)
    #             thought_node.children.append(new_thought_node)
    #             new_thought_nodes.append(new_thought_node)
    #     return new_thought_nodes
    

    def explore_thoughts(self, thought_nodes, num_thoughts=2):
        new_thought_nodes = []
        for thought_node in thought_nodes:
            # Fill in the template with the current thought and desired number of thoughts
            prompt = self.prompt_template.format(
                current_thought=thought_node.thought,
                num_thoughts=num_thoughts
            )
            response = self.call_llm(prompt)
            if response:
                # Split and process the response as before
                thoughts = [line.strip('- ').strip() for line in response.strip().split('\n') if line.strip()]
                for thought in thoughts:
                    if self.is_valid_task(thought):
                        new_thought_node = ThoughtNode(thought)
                        thought_node.children.append(new_thought_node)
                        new_thought_nodes.append(new_thought_node)
        return new_thought_nodes
    
    def is_valid_task(self, task):
        invalid_keywords = ['virtual reality', 'AI', 'machine learning', 'blockchain', 'augmented reality']
        if any(keyword in task.lower() for keyword in invalid_keywords):
            return False
        return True
    
    def run(self):
        iteration = 0
        while self.current_thoughts and iteration < self.max_iterations:
            print(f"Iteration {iteration + 1}:")
            self.current_thoughts = self.explore_thoughts(self.current_thoughts)

            for thought_node in self.current_thoughts:
                print(f"Explored Thought: {thought_node.thought}")
            iteration += 1


    def update_starting_thought(self, new_thought):
        self.root = ThoughtNode(new_thought)
        self.current_thoughts = [self.root]

    def print_tree(self, node, level=0):
        indent = ' ' * (level * 2)
        thought_lines = node.get_thought().split('\n')
        for idx, line in enumerate(thought_lines):
            if idx == 0:
                print(f"{indent}- {line}")
            else:
                print(f"{indent}  {line}")
        for child in node.children:
            self.print_tree(child, level + 1)