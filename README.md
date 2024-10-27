#Application Functionality Description:

- Takes a prompt which instructs the LLM to create a react app for a website
- Begins a Tree of Thoughts approach where development tasks are created which will be executed later
    - The basic app goal is passed in, and the LLM generates thoughts from the prompt
        - we need to decide how much to branch the tree and what depth do we go to for nodes
        - we need to decide on how we evaluate which nodes to keep and when to stop along a path
        - set up a better evaluation function for thoughts: evaluate on effort to complete task vs other tasks, score task based on how much it fits nice to have vs necessary (impact vs effort)
    - After we have created the nodes, we output a series of tasks
- Once we have the task tree, we begin to iterate through the tasks and do a code search for each task
    - For each task, we iterate through our code we have so far, and keep 60% of the allowable tokens along with our prompt
        - The tokens we keep should be the most relevant of what we have found, and we should remove things that are less relevant
        - We need a function to read files from the output folder
    - We pass the results of each search along with the task to generate files
        - we need to overwrite files that exist, or create files that dont exist
        - overwriting can sometimes be just small changes where we integrate a new component
        - We need to be able to call a function to write files from the LLM
    - After finishing a file, we do an integration test. If this passes, we continue. Otherwise we add a task to fix the file.




##Algorithm details for development task search
###Simple BFS
Inputs: num_branches, max_depth, base_thought
- We add base_thought (base prompt) to the queue of thoughts
- We decide if we have completed the task based on the current list of tasks
- From the base prompt we generate num_branches new thoughts from the base prompt
- We evaluate the new thoughts based on a metric
- We add the thoughts which pass to the queue of thoughts to process
- We repeat until there are no thoughts left, or if we reach the max_depth


###Simple DFS
- Maybe not the best approach

###A* Search
Inputs: base_thought
- We add base_thought to the queue of thoughts
- We take the top ranked thought from the queue of thoughts
- We take the top thought from the queue of thoughts
- 



##Algorithm details for code search
- We get a 