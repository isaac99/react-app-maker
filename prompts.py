import constants

FILENAME_QUERY_PROMPT = f"Using best REACT web app architecture design practices, please break down the desired web app into the appropriate files and directories." \
                            f"The web app should be structured in a way that is easy to maintain and scale." \
                            f"Please provide a list of files and directories that should be included in the web app." \
                            f'We are trying to create a web app for: {constants.WEB_APP_DESCRIPTION}' \
                            f'As a starting point, please assume you already have the contents created by create-react-app available, so those files do not need to be created' \
                            f'All files that are suggested should contain the path of the file from the root directory of the web app so they can be located in the app structure' \
                            f'You must respond exactly in minified plain text JSON format with no formatting at all like this: {{"files": ["file1", "file2", "file3"], "directories": ["dir1", "dir2", "dir3"]}}'
                    


STEPS_QUERY_PROMPT = f"Using best REACT web app architecture design practices, please break down the desired web app into a list of tasks to complete." \
                        f"The web app should be structured in a way that is easy to maintain and scale." \
                        f"Please provide a list of specific developent tasks, which should be completed so the website will be up and running, and will meet all business goals." \
                        f"The development tasks should be actionable and specific, so that a developer could complete them without needing further clarification." \
                        f"The tasks should be related to developing a react app, deploying the app, and any other tasks that are necessary to complete the project." \
                        f"All responses should be tasks that would be carried out by a front end React developer. There should be no strategy or research tasks." \
                        f"an example of a complicated and unnecessary task would be : 8. Offer a virtual reality visualization tool that allows users to preview different design options and layouts before starting the renovation process, providing a realistic preview of the end result and enhancing decision-making." \
                        f"the site should be simple and should contain only the simplest components and pages that are necessary for the site to function." \
                        f"For example development tasks are: - Write code for a homepage which contains a navigation bar - create a seperate component for the navigation bar which can be reused across the site - implement code for an about us page - create a new file for a contact us page" \
                        f"Examples of non-development tasks are: 4. Utilize analytics tools to track user engagement and behavior on the website, allowing for data-driven optimization of the user experience. - 7. Utilize machine learning algorithms to improve the accuracy of personalized recommendations and enhance user engagement. 8. Implement user feedback mechanisms to gather insights on the effectiveness of design changes and recommendations, allowing for continuous iteration and improvement. - 9. Integrate natural language processing capabilities to analyze user feedback and sentiment, enabling more nuanced and personalized recommendations based on emotional responses." \
                        f"When writing tasks, consider if each response could be implemented directly in react code by a react developer, if not, this task is not a good one to include." \
                        f'We are trying to create a web app for: {constants.WEB_APP_DESCRIPTION}. ' \
                        f'As a starting point, please assume you already have the contents created by create-react-app available, so those files do not need to be created' \
                        # 'You must respond exactly in minified plain text JSON format with no formatting at all like this: {"steps": ["step 1 description", "step 2 description", "step 3 description",....]}'



PROMPT_TEMPLATE = (
    "Based on the current task:\n"
    "'{current_thought}'\n"
    "Please provide {num_thoughts} specific, actionable next steps that a front-end React developer could implement directly. "
    "These tasks should be simple, essential for the website's functionality, and avoid advanced features like AI, virtual reality, or blockchain. "
    "Focus on standard web development tasks. For example:\n"
    "- Create a responsive navigation bar component to be used across all pages.\n"
    "- Develop a Contact Us page with a form for inquiries."
)