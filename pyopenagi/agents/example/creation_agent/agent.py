from ...react_agent import ReactAgent

class CreationAgent(ReactAgent):
    def __init__(self,
                 agent_name,
                 task_input,
                 agent_process_factory,
                 log_mode: str
        ):
        ReactAgent.__init__(self, agent_name, task_input, agent_process_factory, log_mode)
        # self.workflow_mode = "automatic"
        self.workflow_mode = "manual"

    def manual_workflow(self):
        workflow = [
            {
                "message": "Gather content requirements (platform, topic, style)",
                "tool_use": []
            },
            {
                "message": "Develop content concept and key messages",
                "tool_use": []
            },
            {
                "message": "Generate engaging text content",
                "tool_use": []
            },
            {
                "message": "Create visually appealing images",
                "tool_use": ["text_to_image"]
            },
            {
                "message": "Optimize content for platform and engagement",
                "tool_use": []
            }
        ]
        return workflow

    def run(self):
        return super().run()
