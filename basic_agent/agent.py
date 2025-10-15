from google.adk.agents import Agent
 
root_agent = Agent(
    name="basic_agent",
    model="gemini-2.0-flash",
    description="Basic agent for testing",
    instruction="""
    You are an assistant that greets the user, checks even numbers, and gives length of names.
    """
)